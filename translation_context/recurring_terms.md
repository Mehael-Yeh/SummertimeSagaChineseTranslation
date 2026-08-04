# 重复称呼、口癖与专名复查记录

更新时间：2026-08-04

## 触发规则

处理完整文件时，只要英文原文中的同一名词、组合词、称呼或固定表达在短距离内出现 **2 次及以上**，就先把它视为潜在的专名、人物口癖或关系称呼，不在当前几行内孤立定译。

必须依次执行：

1. 在当前完整文件中确认说话人、指代对象、关系阶段和重复方式。
2. 使用仓库级搜索或 `python -X utf8 tools/audit_recurring_terms.py --query "英文短语"` 查找跨文件出现位置。
3. 判断其属于人物姓名、描述性称呼、口癖、地点/物品/车辆专名，还是普通重复用词。
4. 确认稳定译法后，同时登记到 `terminology.md`、`recurring_terms.json` 和本文件；涉及人物时同步更新 `characters.md`。
5. 未通读的后续文件只登记为复查队列，不直接做无上下文的全局替换。
6. 后续每处理一个文件，运行 `python -X utf8 tools/audit_recurring_terms.py --changed --fail-on-mismatch`，确保已登记表达没有再次漂移。

> `recurring_terms.json` 是机器可读的审计规则；`tools/audit_recurring_terms.py` 只检查和报告，不自动改写译文。

## 已确认条目

| 条目 | 类型 | 固定处理 | 仓库出现范围 | 当前结论 |
|---|---|---|---|---|
| Tony 的 `champ` | 人物专属称呼 | 冠军 | 173 处 / 13 个文件 | `ano09.rpy` 的 9 处已统一；未处理文件仍有 16 处旧译待随剧情文件复核 |
| Tina 的 `babyface` | 人物专属称呼 | 小帅哥 | 42 处 / 10 个文件 | `ano09.rpy`、`ano11.rpy`、`ano13.rpy` 的称呼已统一；Tony 客观描述外貌的 `babyfaces` 仍译“娃娃脸” |
| Maria/Tony 的 `dollface` | 老派亲昵称呼 | 美人儿 | 3 处 / 3 个文件 | `ano09.rpy`、`ano11.rpy`、`ano13.rpy` 已全部统一 |
| `The Blue Falcon` | 车辆专名 | 蓝色猎鹰号 | 6 处 / 1 个文件 | `ano09.rpy` 全部一致 |
| `The Sapphire Stallion` | 车辆候选名 | 蓝宝石种马号 | 2 处 / 1 个文件 | `ano09.rpy` 全部一致 |
| `The Overcompensator` | 车辆专名/笑点 | 过度补偿者 | 4 处 / 2 个文件 | `ano09.rpy`、`jos_trade.rpy` 当前核心译名一致 |
| Tony 的 `capisce` | 人物口癖 | 懂了没？／明白吗？ | 25 处 / 10 个文件 | 允许按威胁、催促、确认语气微调，但必须保留 Tony 的固定语用功能 |
| Tony 对 Anon 的 `protégé` | 关系定位 | 徒弟 | 5 处 / 3 个文件 | `ano10.rpy`、`ano11.rpy` 已统一；只剩 `tin_vault.rpy` 待随完整场景复核 |
| `cannoli`（食品） | 食品术语 | 意式奶油甜馅卷 | 4 处食品用法 / 4 个文件 | `ano10.rpy` 已定译；`mar_baby.rpy`、`mar_cook.rpy`、`mar_dark.rpy` 旧译待复核；`Holy cannoli` 感叹语排除 |
| `mustache ride` | 成人双关 | 骑胡子 | 4 处 / 2 个文件 | `ano10.rpy`、`ano15.rpy` 已全部复核并统一，保留早期 Anon 不懂含义的笑点 |
| Tony 的 `The Plumber` | 人物旧绰号 | 保持 `The Plumber` | 1 处 / 1 个文件 | `ano11.rpy` 已确认是旧黑帮专名，不翻译、不音译 |
| `Eddie Four-Fingers` / `Four-Fingers` | 人物姓名/绰号 | 保持英文原形 | 3 处 / 2 个文件 | `ano11.rpy`、`ano13.rpy` 已统一，中文音译/混合写法已清除 |
| Dimitri 的 `little bunny` | 戏谑性固定称呼 | 小兔子 | 11 处 / 4 个文件 | `ano03.rpy`、`ano06.rpy`、`ano11.rpy` 已确认；`deb18.rpy` 3 处列入后续队列 |
| `borscht` | 俄式食品 | 罗宋汤 | 2 处 / 1 个文件 | `ano11.rpy` 两处已统一，并登记防止后续漂移 |
| `prosciutto` | 食品术语 | 意式风干火腿 | 4 处 / 1 个文件 | `ano13.rpy` 四处连续配料台词已统一 |
| `gorgonzola` | 食品术语 | 戈贡佐拉奶酪 | 4 处 / 1 个文件 | `ano13.rpy` 四处连续配料台词已统一 |
| `calzone` | 食品术语 | 意式烤饺 | 3 处 / 3 个文件 | `ano09.rpy`、`ano13.rpy`、`ano15.rpy` 已全部复核并统一 |
| `Beachside Apartments` | 地点专名 | 海滨公寓 | 3 处 / 3 个文件 | 资源表、`ano13.rpy`、`ano14.rpy` 当前核心译名一致 |
| `moderate affection points` | 系统提示 | 好感度中幅提升 | 2 处 / 2 个文件 | `ano12.rpy`、`ano14.rpy` 已统一，角色变量和随机数表达式保持原样 |
| `hydration is key` | 固定口号 | 补水最重要 | 2 处 / 2 个文件 | `ano13.rpy`、`ano15.rpy` 已统一 |
| `capicola` | 食品术语 | 卡皮科拉火腿 | `ano15.rpy` | Tony 的意大利式熟食比喻，已复核 |
| `Boy, boy, boy... very tall boy.` | 暗号/重复句 | 男孩，男孩，男孩……长得高高的男孩。 | `ano15.rpy` | 保留 Tony 的拙劣暗号和重复节奏 |
| `godfather` | 关系身份/黑帮笑点 | 教父 | 8 处 / 2 个文件 | `ano16.rpy` 2 处已复核；`mar_baby.rpy` 6 处待随完整剧情复核；不改成“干爹” |
| `workplace seminar` / `the seminar` | 连续笑点 | 职场性骚扰培训／培训 | 2 处 / 1 个文件 | `ano15.rpy` 已结合员工场景复核；不是 Tony/Maria 性行为暗语 |
| `Consum-R` | 商店专名 | 保持 `Consum-R` | 跨多个剧情与资源文件 | 电脑零件和购物任务统一保留英文原拼写、大小写及连字符 |

## 当前跨文件复查队列

- `champ`：`ano15.rpy`、`ano16.rpy` 已统一；`mar02.rpy`、`mar_baby.rpy`、`mar_dark.rpy`、`pizza_boxes.rpy`、`ton_baby.rpy` 仍待随完整剧情复核。
- `babyface`：已处理的 `ano09.rpy`、`ano11.rpy`、`ano13.rpy` 统一为“小帅哥”；其余 Tina 剧情文件中的“娃娃脸/小可爱/小宝贝”待逐文件复核。
- `protégé`：`ano11.rpy` 已统一为“徒弟”；`tin_vault.rpy` 仍有 1 处旧译待复核。
- `cannoli`：`mar_baby.rpy`、`mar_cook.rpy`、`mar_dark.rpy` 的食品名称旧译不一致；`Holy cannoli` 属感叹语，不机械替换。
- `little bunny`：`deb18.rpy` 3 处待在完整剧情中复核，核心译法保持“小兔子”。
- `godfather`：`ano16.rpy` 2 处已统一为“教父”；`mar_baby.rpy` 6 处待随完整剧情复核，并保留与 Tony 黑帮背景相关的《教父》笑点。
- 上述条目只登记，不在未通读完整文件前批量替换；进入对应文件时结合关系阶段完成统一。

## 审计命令

```powershell
# 检查全部已登记条目，只显示不一致项
python -X utf8 tools/audit_recurring_terms.py

# 查看某个条目的全部英文—中文对应
python -X utf8 tools/audit_recurring_terms.py --term vehicle_blue_falcon --show-all

# 临时搜索刚发现的重复短语
python -X utf8 tools/audit_recurring_terms.py --query "Blue Falcon"

# 每批必须运行：只检查本批修改过的 Ren'Py 文件，并在不一致时返回失败
python -X utf8 tools/audit_recurring_terms.py --changed --fail-on-mismatch
```
