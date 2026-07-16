# SummertimeSagaChineseTranslation
[Summertime Saga](https://summertimesaga.com/) 中文汉化文件（仅适配v21版本）
- 所有翻译采用机器翻译，可能存在部分不严谨不准确的地方，如有建议可以自行修改或提交Issues。
- 原始文本版权属于Kompas，在官方正式汉化前本文件仅做学术探讨使用，不承担相关法律责任。
### 使用说明
将文件解压后tl文件放置在游戏/game目录下，其他rpy文件直接放置在游戏/game目录下，最终游戏目录结构如下：
```
游戏根目录/
├── game/
│  ├── tl/
│     ├── chinese/
│        ├── ...
├── set_default_language_at_startup.rpy
├── hook_add_change_language_entrance.rpy
```

### 下载单文件汉化包
在仓库的 **Actions → Build Chinese RPA** 页面手动运行工作流，完成后下载页面底部生成的 artifact。将其中的 `chinese.rpa` 直接放到游戏的 `game` 目录即可。归档同时包含 `tl/chinese`、默认语言设置和语言入口脚本。

RPA 内的 Ren'Py 脚本必须先使用 Ren'Py 8.5.3 编译为 `.rpyc`。Actions 会自动完成编译、打包与校验；仓库中的 Python 命令主要用于维护和验证归档格式。

```bash
python tools/build_rpa.py --root path/to/compiled/game --compiled --output dist/chinese.rpa
```
