# SummertimeSagaChineseTranslation
[Summertime Saga](https://summertimesaga.com/) 中文汉化文件（仅适配v21版本）
- 所有翻译采用机器翻译，可能存在部分不严谨不准确的地方，如有建议可以自行修改或提交Issues。
- 原始文本版权属于Kompas，在官方正式汉化前本文件仅做学术探讨使用，不承担相关法律责任。
### 使用说明
有两种使用方式，适合不同需求：
#### 1.懒人包
将chinese.rpa文件放置在游戏/game目录下，最终游戏目录结构如下：
```
游戏根目录/
├── game/
│  ├── chinese.rpa
```
#### 2.可以手动调整文本
将解压缩后将tl文件夹放置在游戏/game目录下，其他rpy文件直接放置在游戏/game目录下，最终游戏目录结构如下：
```
游戏根目录/
├── game/
│  ├── tl/
│     ├── chinese/
│        ├── ...
├── set_default_language_at_startup.rpy
├── hook_add_change_language_entrance.rpy
```
