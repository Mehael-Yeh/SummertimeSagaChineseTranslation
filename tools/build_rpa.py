#!/usr/bin/env python3
"""Build and verify a deterministic Ren'Py RPA-3.0 translation archive."""

from __future__ import annotations

import argparse
import hashlib
import pickle
import struct
import zlib
from pathlib import Path, PurePosixPath


HEADER_SIZE = 34
KEY = 0x53534354  # "SSCT"
ROOT_FILES = (
    "set_default_language_at_startup.rpy",
    "hook_add_change_language_entrance.rpy",
)


def source_files(root: Path, compiled: bool = False) -> list[tuple[str, Path]]:
    root_names = tuple(f"{name}c" for name in ROOT_FILES) if compiled else ROOT_FILES
    files = [(name, root / name) for name in root_names]
    files.extend(
        (path.relative_to(root).as_posix(), path)
        for path in (root / "tl" / "chinese").rglob("*")
        if path.is_file()
        and (
            path.suffix.lower() not in {".rpy", ".rpym", ".rpyb", ".rpyc", ".rpymc"}
            or (compiled and path.suffix.lower() in {".rpyc", ".rpymc"})
            or (not compiled and path.suffix.lower() in {".rpy", ".rpym"})
        )
    )
    missing = [name for name, path in files if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Missing required input: {', '.join(missing)}")
    return sorted(files)


def build(root: Path, output: Path, compiled: bool = False) -> dict[str, str]:
    files = source_files(root, compiled)
    index: dict[str, list[tuple[int, int]]] = {}
    hashes: dict[str, str] = {}
    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("wb") as archive:
        archive.write(b"\0" * HEADER_SIZE)
        for name, path in files:
            data = path.read_bytes()
            offset = archive.tell()
            archive.write(data)
            index[name] = [(offset ^ KEY, len(data) ^ KEY)]
            hashes[name] = hashlib.sha256(data).hexdigest()

        index_offset = archive.tell()
        # Protocol 2 is readable by old and new Ren'Py/Python releases.
        archive.write(zlib.compress(pickle.dumps(index, protocol=2), level=9))
        archive.seek(0)
        archive.write(f"RPA-3.0 {index_offset:016x} {KEY:08x}\n".encode("ascii"))

    return hashes


def read_index(archive_path: Path) -> tuple[int, dict[str, list[tuple[int, int]]]]:
    with archive_path.open("rb") as archive:
        header = archive.readline()
        parts = header.rstrip(b"\n").split()
        if len(parts) != 3 or parts[0] != b"RPA-3.0":
            raise ValueError("Not an RPA-3.0 archive")
        index_offset = int(parts[1], 16)
        key = int(parts[2], 16)
        archive.seek(index_offset)
        index = pickle.loads(zlib.decompress(archive.read()))
    return key, index


def verify(root: Path, archive_path: Path, compiled: bool = False) -> None:
    expected = {name: path for name, path in source_files(root, compiled)}
    key, index = read_index(archive_path)
    if set(index) != set(expected):
        missing = sorted(set(expected) - set(index))
        extra = sorted(set(index) - set(expected))
        raise ValueError(f"Archive entries differ; missing={missing}, extra={extra}")

    with archive_path.open("rb") as archive:
        for name, path in expected.items():
            entries = index[name]
            if len(entries) != 1 or len(entries[0]) != 2:
                raise ValueError(f"Unsupported index entry for {name!r}")
            offset, length = (value ^ key for value in entries[0])
            archive.seek(offset)
            actual = archive.read(length)
            if actual != path.read_bytes():
                raise ValueError(f"Content mismatch for {name!r}")

    print(f"Verified {len(expected)} files in {archive_path} ({archive_path.stat().st_size} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, default=Path("dist/chinese.rpa"))
    parser.add_argument("--compiled", action="store_true", help="Pack compiled .rpyc scripts")
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    output = args.output.resolve()
    if not args.verify_only:
        hashes = build(root, output, args.compiled)
        print(f"Packed {len(hashes)} files into {output}")
    verify(root, output, args.compiled)


if __name__ == "__main__":
    main()
