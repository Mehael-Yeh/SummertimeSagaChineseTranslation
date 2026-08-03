# zz_renpybox_sms_fix.rpy
# ============================================================
# 短信/UI 文本翻译修复（纯 tl 目录方案，不改游戏本体脚本）
# ------------------------------------------------------------
# 背景：游戏短信在 tel_chat 界面用 `text '[mesg.what!i]'` 渲染。
#   Ren'Py 的 `!i` 转换只做插值、不做字符串翻译（只有 `!t`
#   才会调用 translate_string），所以 zz_renpybox_bytecode_strings.rpy
#   里带 [saga.cast.X] 占位符的 old/new 对永远无法命中，短信
#   始终显示英文。
#
# 方案：chinese 语言激活时，
#   1. 读取 zz_renpybox_bytecode_strings.rpy 的全部 old/new 对；
#   2. 对占位符全部为 [saga.cast.X] 的纯文本条目，用 Ren'Py 插值
#      把 old 还原成运行时实际显示的英文；
#   3. 把「插值后的英文 -> 插值后的中文」注册进 config.replace_text，
#      文本渲染（插值之后）时按整串替换。
#
# 注意：Ren'Py 8.5.3 没有 `translate <lang> screen` 语法（解析器
#   只支持 strings/python/style/对话块），因此无法用屏幕覆盖把
#   `!i` 改成 `!ti`，本文件是等效且自维护的替代方案：zz 文件每次
#   重新生成后，映射会自动跟随。
# ============================================================

init -1 python:
    import re as _rb_re
    import os as _rb_os
    import renpy.substitutions as _rb_sub

    _rb_escape_re = _rb_re.compile(r'\\(.)')
    _rb_old_re = _rb_re.compile(r'^\s*old\s+"((?:\\.|[^"\\])*)"\s*$')
    _rb_new_re = _rb_re.compile(r'^\s*new\s+"((?:\\.|[^"\\])*)"\s*$')
    _rb_expr_re = _rb_re.compile(r'\[[^\]]*\]')
    _rb_cast_ref_re = _rb_re.compile(r'^\[saga\.cast\.[A-Za-z_][A-Za-z0-9_]*\]$')
    _rb_escape_map = {'n': '\n', 't': '\t', '\\': '\\', '"': '"'}

    def _rb_unescape(s):
        return _rb_escape_re.sub(
            lambda m: _rb_escape_map.get(m.group(1), m.group(1)), s
        )

    def _rb_sms_replace(s):
        if not isinstance(s, str):
            return s
        _rb_map = renpy.store.__dict__.get('_rb_sms_map') or {}
        if s in _rb_map:
            return _rb_map[s]
        _rb_prev = renpy.store.__dict__.get('_rb_sms_prev_replace')
        if _rb_prev is not None:
            return _rb_prev(s)
        return s

    def _rb_rebuild_sms_map():
        renpy.store._rb_sms_map = {}
        try:
            _rb_f = renpy.loader.load('tl/chinese/renpybox_bytecode_strings.rpy')
            try:
                _rb_raw = _rb_f.read()
            finally:
                _rb_f.close()
            if isinstance(_rb_raw, bytes):
                _rb_raw = _rb_raw.decode('utf-8', 'replace')

            _rb_pairs = []
            _rb_old = None
            for _rb_line in _rb_raw.splitlines():
                _rb_m = _rb_old_re.match(_rb_line)
                if _rb_m:
                    _rb_old = _rb_unescape(_rb_m.group(1))
                    continue
                _rb_m = _rb_new_re.match(_rb_line)
                if _rb_m and _rb_old is not None:
                    _rb_pairs.append((_rb_old, _rb_unescape(_rb_m.group(1))))
                    _rb_old = None

            for _rb_old_s, _rb_new_s in _rb_pairs:
                # 短信正文经 `text '[mesg.what!i]'` 渲染时从不走
                # translate_string，所以无论有没有 [saga.cast.X] 占位符，
                # 都要进 replace_text 映射。仅排除两类：
                # - 含 {tag} 的条目：tokenize 时被拆开，replace_text 收到
                #   的是去标签的片段，整串匹配不可靠；
                # - 含其它动态表达式（如 [renpy.random...]）的条目：
                #   提前求值有副作用，跳过。
                if '{' in _rb_old_s:
                    continue
                _rb_exprs = _rb_expr_re.findall(_rb_old_s)
                if _rb_exprs and any(
                    not _rb_cast_ref_re.match(_rb_e) for _rb_e in _rb_exprs
                ):
                    continue
                try:
                    _rb_en, _ = _rb_sub.substitute(
                        _rb_old_s, scope=None, translate=False
                    )
                    _rb_zh, _ = _rb_sub.substitute(
                        _rb_new_s, scope=None, translate=False
                    )
                except Exception:
                    continue
                if isinstance(_rb_en, str) and _rb_en and _rb_en != _rb_zh:
                    renpy.store._rb_sms_map[_rb_en] = _rb_zh
        except Exception:
            renpy.store._rb_sms_map = {}

    renpy.store._rb_sms_map = {}
    renpy.store._rb_sms_prev_replace = None

    # 调试标记：确认 init python 已执行、gamedir 路径正确（确认后删除）
    try:
        with open(
            _rb_os.path.join(
                renpy.config.gamedir, 'tl', 'chinese', '_sms_fix_debug_init.txt'
            ),
            'w',
            encoding='utf-8',
        ) as _init_dbg:
            _init_dbg.write('gamedir=%s\n' % renpy.config.gamedir)
        # 重要：立即删除文件句柄，避免它作为 store 全局变量进入存档序列化，
        # 否则保存时会报 cannot pickle 'TextIOWrapper' instances。
        try:
            del _init_dbg
        except Exception:
            pass
    except Exception:
        pass


translate chinese python:
    import traceback as _rb_tb

    # 语言激活时注册/重建（重复激活不会无限叠加包装器）
    try:
        if renpy.config.replace_text is not _rb_sms_replace:
            _rb_sms_prev_replace = renpy.config.replace_text
            renpy.config.replace_text = _rb_sms_replace
        _rb_rebuild_sms_map()
        _rb_info = 'OK map_size=%d' % len(_rb_sms_map)
    except Exception:
        _rb_info = 'ERR ' + _rb_tb.format_exc()

    # 调试输出：验证映射是否建立（确认后删除）
    try:
        with open(
            _rb_os.path.join(
                renpy.config.gamedir, 'tl', 'chinese', '_sms_fix_debug.txt'
            ),
            'w',
            encoding='utf-8',
        ) as _dbg:
            _dbg.write(_rb_info + '\n')
            _dbg.write(
                'HAS_ALL_GOOD: %s\n'
                % ('All good, dude. Got a raid scheduled, but you can always start without me.' in _rb_sms_map)
            )
            _dbg.write('HAS_MY_ROOM: %s\n' % ('My room, NOW!' in _rb_sms_map))
            for _k, _v in list(_rb_sms_map.items())[:5]:
                _dbg.write('KEY: %s\nVAL: %s\n---\n' % (_k, _v))
        # 重要：立即删除文件句柄，避免它作为 store 全局变量进入存档序列化，
        # 否则保存时会报 cannot pickle 'TextIOWrapper' instances。
        try:
            del _dbg
        except Exception:
            pass
    except Exception:
        pass
