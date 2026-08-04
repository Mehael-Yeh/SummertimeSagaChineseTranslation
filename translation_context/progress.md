# 翻译精修进度

更新时间：2026-08-04

## 状态说明

- **完成**：已通读完整文件，完成英文对照、纯中文复读、原文复核及格式校验。
- **规则修复**：仅修复可高置信确认的姓名、标签或变量问题，尚未对完整剧情逐条精修。
- **待处理**：尚未完成完整场景级精修。

## 已完成文件

| 文件 | 剧情线/场景 | 主要角色 | 状态 | 主要修复 | 校验 |
|---|---|---|---|---|---|
| `tl/chinese/src/plot/mar01.rpy` | Maria线；Tony/Maria 生育后的披萨店成人场景与关系安抚 | Maria、Tony、Anon | 完成 | 通读完整场景并精修感谢、生育双关、顾客掩饰、性交与高潮、负罪感安抚；统一中文省略号、成人动作强度和 Maria 主动粗俗口吻；保留所有英文姓名与变量 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar02.rpy` | Maria线；Tony与Anon讨论 Maria 产后继续发生关系及再生育计划 | Tony、Anon、Maria（被提及） | 完成 | 通读完整场景并精修 Tony 的支持与施压、Anon 的犹豫和关系推进；统一 Tony 专属称呼 `champ` →“冠军”；保留性行为动作强度、粗俗语气和英文姓名 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_baby.rpy` | Maria线；怀孕确认、单胎/双胎生产、医院探访、产后恢复与返回披萨店 | Maria、Tony、Anon、新生儿 | 完成 | 通读单胎与双胎全部分支；精修怀孕生产、教父关系、产后关怀和成人双关；修复“听醒”“娃娃脸”等误译；统一 `champ`、`cannoli`、单复数代词及英文姓名 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_cook.rpy` | Maria线；Maria在厨房为Anon准备食物并推进亲密关系 | Maria、Anon | 完成 | 通读完整场景并精修 40 个翻译块；统一 cannoli 等意大利食物术语；修复厨房动作、暧昧双关、成人语气和 Maria 对 Anon 的称呼；保留英文姓名、变量与 Ren’Py 结构 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/maria.rpy` | Maria 线；公寓与披萨店的通用入口、出口、菜单及储藏室短互动 | Maria、Anon、Tony（被提及） | 完成 | 精修 58 个对话块和 4 个菜单文本；按关系阶段区分“小子”与“帅哥”，将后期 `lookin’ for trouble` 处理为性邀约式“找刺激”；修复菜单主题、工钱占位符外围中文及储藏室连续互动 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/maria_lounge.rpy` | Maria 线；公寓客厅夜间访问、无人应门及 Tony 休息日拦截 | Maria、Tony、Anon | 完成 | 精修 13 个翻译块；纠正整文件多处译文错位和截断，恢复夜间内心独白、敲门声、Maria 邀请进门、无人应门及让 Tony 休息的完整逻辑；按实际生效方式保留 TODO 块中的中文拦截文本 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_dark.rpy` | Maria线；夜间造人、内射/拔出分支、骑乘、“恶魔三人行”及双重插入 | Maria、Tony、Anon | 完成 | 通读 369 组英文—中文对应；精修 Tony 的造人指导和粗俗起哄、Maria 后期主动口吻、Anon 的迟疑与参与；统一 `champ`、`capisce/capiche`、`Devil's Threeway`、`The Kidney Shifter`、`cannoli` 及成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_couch.rpy` | Maria线；Tony熟睡、半醒或看球时，Maria与Anon在沙发上发生性行为，并以棒球双关贯穿多条场景 | Maria、Tony、Anon、Carmella | 完成 | 通读 640 个翻译块；精修射精、内射、上垒、满垒、界外球和“横着做披萨”等双关；统一 Tony 的 `champ`→“冠军”、The Falsettos→《假声》以及 Carmella 英文姓名；恢复露骨性行为和 Maria 主动语气，全文消除活动译文中的 ASCII 省略号和直角引号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_door.rpy` | Maria线；久未造访后的卧室性交、央求、拔出/内射与续战分支 | Maria、Anon、Tony（被提及） | 完成 | 精修后期关系中的主动邀约、央求与 Anon 掌控节奏；明确区分内射期待和拔出后的保密要求；统一连续拆句、女性高潮和动作义“肏” | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_kitchen.rpy` | Maria线；披萨店后厨的试探、速战速决与食物式成人双关 | Maria、Anon | 完成 | 精修 38 个翻译块；保留 Maria 经营者的警觉和后期直接欲望；统一 `au jus`→“肉汁”、`Yes, ma’am.`→“是，老板娘”及未完成连续句 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/mar_pantry.rpy` | Maria线；储藏室工作压力、性邀约、内射/拔出与事后交接 | Maria、Anon、Tony（被提及） | 完成 | 精修 90 个翻译块；恢复“休息”双关、再次怀孕诉求和拔出分支差异；统一女性高潮、`Cum in me`、`Gimme another baby` 及连续拆句 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb01.rpy` | Debbie线开端；陌生索款威胁、父亲债务疑云及 Diane 园艺工作分支 | Debbie、Anon、Diane（被提及） | 完成 | 通读 77 个翻译块；理顺电话冲突、Debbie 强装镇定、Anon 主动分担和菜园分支；统一 `sweetie`→“亲爱的”、中文省略号、内心独白括号与父亲称谓 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb02.rpy` | Debbie线早期；父亲遗留报纸、填字游戏双关、意外亲吻与 Anon 首次性反应 | Debbie、Anon | 完成 | 通读 71 个翻译块和 4 个选项；恢复 `Dick` 的英文填字与性双关，修复捡笔动作、碰头安慰、勃起反应及错位内心独白；统一 `sweetie`、省略号、中文括号与英文填字答案 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb03.rpy` | Debbie线早期；承担家务、修剪草坪、地下室毛巾事故与首次明确身体吸引 | Debbie、Anon、Jenny | 完成 | 通读 219 个翻译块和 3 个选项；修复父亲责任承接、`my boy` 误译、洗衣动作、裸体/勃起场景、Debbie 的掩饰、蜘蛛借口及三分支连续性；统一全角括号和中文省略号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb04.rpy` | Debbie线早期；浴室水管爆裂、家庭维修责任与 Jenny 湿衣试探 | Debbie、Jenny、Anon | 完成 | 通读 188 个翻译块并精修 154 处；理顺关总水阀、获取扳手、湿衣脱衣试探和四类维修见证分支；强化 Debbie 的经济压力与照顾者鼓励、Jenny 的尖刻挑衅及 Anon 承接父亲责任的成长 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb05.rpy` | Debbie线早期；家务分担、卧室送衣、腿部按摩与暧昧边界 | Debbie、Anon | 完成 | 通读完整场景并精修约 171 处；理顺家务承接、背痛与压力、乳液气味和私人物品分心、按摩中的身体吸引及 Debbie 及时叫停；统一 `sweetie`、中文省略号、全角括号，并保留早期关系阶段的含蓄强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb06.rpy` | Debbie线早期；按摩回忆、偷拿润肤露、使用内裤自慰被撞见及事后边界谈话 | Debbie、Anon | 完成 | 通读 126 个翻译块；理顺按摩记忆、气味诱发的性冲动、Debbie 撞见后的震惊与自我安慰，以及她理解自慰但明确禁止在卧室或使用内裤的边界；统一 `sweetie`、润肤露、自慰、内裤、中文省略号、中文双引号和全角括号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb07.rpy` | Debbie线早期暧昧推进；夜间共看爱情片、意外触碰勃起及双方首次持续性幻想 | Debbie、Anon | 完成 | 通读 141 个翻译块；理顺选片争论、电影情色转折、脚部误触、Debbie 对尺寸的震惊与幻想、Anon 的尴尬掩饰及温柔告别；以“挺得住”保留 `solid` 的承受/勃起双关，并回扣“巴西 Bum Bum”产品名 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb08.rpy` | Debbie线；商场同行、Cupid试衣、首次接吻与事后回避 | Debbie、Anon、Kassy、Jenny（被提及） | 完成 | 通读 375 个翻译块和 6 个选项；精修购物邀请、童年照片笑点、女装店调侃、更衣室拉链、电影回调、首次接吻及双方不同的事后心理；修复反译、连续拆句、拉链方向和关系阶段，统一省略号、中文双引号与内心括号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb09.rpy` | Debbie线；首次接吻后的性梦、Ursula乱入噩梦及关系认知变化 | Debbie、Anon、Ursula | 完成 | 通读 33 个翻译块；理顺 Debbie 安抚与性诱惑的连续拆句、Ursula 的学校羞耻威胁及 Anon 醒后的自我审视；修复称谓误译、机翻语序、ASCII 省略号和半角内心括号，保留梦境露骨强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb10.rpy` | Debbie线；Debbie自慰幻想、Anon与Jenny偷窥及Jenny借机要挟 | Debbie、Anon、Jenny | 完成 | 通读 88 个翻译块；精修门外误判、自慰幻想、Anon确认幻想对象、Jenny撞破偷窥及后续要挟；修复连续拆句、自慰俚语、女性高潮、双关笑话、中文引号、省略号和内心括号，区分幻想中的欲望与现实中的同意 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb11.rpy` | Debbie线；早餐性梦、小丑噩梦、梦遗惊醒及Jenny隔门挖苦 | Anon、Debbie、Jenny | 完成 | 通读 88 个翻译块；理顺Jenny炫耀新裙、Debbie桌下口交、人物变成小丑、阴茎变羊驼及咬伤惊醒的梦境递进；修复连续拆句、口交拟声、食物性双关、梦遗笑点、中文省略号和内心括号，保留梦境欲望与现实关系的区别 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb12.rpy` | Debbie线；借性焦虑请求指导、再次接吻、Jenny撞见及重新划定边界 | Debbie、Anon、Jenny | 完成 | 通读 128 个对话块和 3 个选项；理顺梦境话题转为性焦虑的试探、商场接吻回扣、“纯教学”自我辩护、大学接吻技巧、扁桃体炎掩饰及Jenny的尖刻揭穿；修复代词、连续拆句、中文省略号、双引号与内心括号，区分真实吸引、主动试探和现实边界 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/+prologue.rpy` | 序章；父亲葬礼、死亡疑点、债务与开学背景 | Anon、Debbie（叙述中） | 完成 | 重写机翻腔；理顺死亡调查、收留和债务背景；统一叙述语气 | `validate_translations.py --changed` 通过 |
| `tl/chinese/src/plot/+tutor.rpy` | 系统教程；HUD、地图、物品栏、手机、时间推进 | tutor、Anon（变量） | 完成 | 统一系统术语；修复 `extend` 连续拆句；改善教程说明的自然度 | `validate_translations.py --changed` 通过 |
| `tl/chinese/src/plot/ano01.rpy` | 主线；复学第一天及学校角色集中引入 | Anon、Jenny、Debbie、Erik、Tammy、Mia、Roxxy、Ursula、Kevin、Annie、Judith、Bridget、Rhonda、Viv、Eve | 完成 | 精修 609 个翻译块和 3 组菜单文本；修复答非所问、连续拆句、角色口吻、色情游戏双关、ASCII 省略号和菜单术语不一致 | `validate_translations.py --changed`、`git diff --check`、RPA 构建/校验通过 |
| `tl/chinese/src/plot/ano02.rpy` | 主线；警方通报父亲死亡调查、资金失踪与威胁电话 | Anon、Debbie、Harold、Yumi、Frank、Liu Wang | 完成 | 精修 121 个翻译块；修复调查逻辑、连续拆句、职业礼貌、代词指向、`overhear` 误译为“偷听”、金融术语及 `[saga.cast.liu] Wang` 姓名顺序 | `validate_translations.py --changed`、`git diff --check`、RPA 构建/校验通过 |
| `tl/chinese/src/plot/ano03.rpy` | 主线；家庭早餐、Dimitri 上门威胁、Yumi 做笔录与安全安排 | Anon、Debbie、Jenny、Dimitri、Yumi、Frank、Harold | 完成 | 通读 253 个翻译块并精修 189 个；修复苹果汁漏译、连续拆句、Dimitri 非母语威胁口吻、Yumi 警务称谓、APB/笔录术语及 Jenny 前期敌对语气 | `validate_translations.py --changed`、`git diff --check`、RPA 构建/校验通过 |
| `tl/chinese/src/plot/ano04.rpy` | 主线早期；Tammy 上门慰问、与 Debbie 谈离婚及照顾 Erik、鼓励 Debbie 与 Anon 沟通 | Tammy、Debbie、Anon、Erik（被提及） | 完成 | 通读 43 个翻译块并精修 39 个；修复丧亲慰问翻译腔、`friendly ear`/`come out of his shell` 直译、连续拆句、Tammy 母性化口吻及 Debbie 早期照顾者边界 | `validate_translations.py --changed`、`git diff --check`、RPA 构建/校验通过 |
| `tl/chinese/src/plot/ano05.rpy` | 主线；Dimitri 驾车监视、报警与警方留守、Anon 的家庭保护欲及开放探索引导 | Anon、Debbie、Jenny、Yumi、Dimitri（车内） | 完成 | 通读 115 个翻译块并精修 91 个；修复车辆动作误译、警方反讽、连续拆句、Jenny 露骨拒绝比喻、`That's my boy!` 关系误译及 ASCII 省略号 | `validate_translations.py --changed`、`git diff --check` 通过；RPA 已成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano06.rpy` | 主线；Dimitri 与 Igor 街头围堵、Tony 解围、Debbie 抵押房屋支付追债款 | Anon、Dimitri、Igor、Tony、Debbie、Jenny | 完成 | 通读 329 个翻译块并精修 231 处译文；修复块内错配、非母语威胁口吻、成人搜身笑话、Tony 粗俗保护者语气、二十五万美元贷款和房屋抵押逻辑 | `validate_translations.py --changed`、`git diff --check` 通过；RPA 已成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano07.rpy` | 主线；Tony披萨店送餐试送、正式入职及初见 Maria | Anon、Tony、Maria、Gino（被提及） | 完成 | 通读 249 个翻译块并精修 198 处译文；修复送货员短缺错译、自取订单和试送术语、分支衔接、Tony 江湖化雇主口吻、Maria 从警惕到工作指导的态度变化及粗俗比喻强度 | `validate_translations.py --changed`、`git diff --check`、结构映射专项检查通过；RPA 已成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano08.rpy` | 主线占位；Tony 关系线的元叙事自嘲 | Anon、Tony（被提及） | 完成 | 通读 4 个翻译块并精修 3 处译文；修复 `face time` 误译、元叙事逻辑、全角内心独白括号和纯省略号 | `validate_translations.py --changed`、`git diff --check`、结构映射专项检查通过；RPA 已成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano09.rpy` | Tony披萨店；Tina 初见、Luigi 遗属照顾承诺、送餐车辆购买/置换与命名 | Anon、Tony、Maria、Tina、Luigi（被提及） | 完成 | 通读并精修 385 个翻译块；统一 Tony/Maria 的意大利裔美国人口吻、雇佣称谓和车辆分支；固定 `champ`→“冠军”、`babyface`→“小帅哥”、`dollface`→“美人儿”及车辆专名；保留 Luigi 遗属承诺的真实关系 | `validate_translations.py --changed`、重复术语审计、`git diff --check`、结构/BOM/CRLF 专项检查通过；RPA 已成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano10.rpy` | Tony披萨店；披萨教学、cannoli 奖励误导、黑帮往事与不育诊断 | Anon、Tony、Maria、Luigi（被提及） | 完成 | 通读 324 个英文—中文映射并精修 248 余处；统一手抛饼底、深盘披萨、披萨石和意式奶油甜馅卷；修复 `mustache ride` 成人双关、`protégé` 关系定位、连续拆句、Tony/Luigi 兄弟关系、意大利黑手党身份及 Tony 不育比喻到直白说明的情绪递进 | `validate_translations.py --changed` 验证 18 个修改文件；10 组重复术语审计零不一致；`git diff --check` 通过；RPA 成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano11.rpy` | Tony披萨店；领养/精子捐赠争论、搬面粉、Dimitri/Igor 闯店及 Tony 调查 Raz | Anon、Tony、Maria、Tina、Dimitri、Igor、Eddie Four-Fingers（被提及） | 完成 | 通读 324 条对话映射和 2 条 strings，精修 259 条译文；修复生育状态误判、领养与捐精逻辑、俄式食品笑话、持枪冲突节奏、连续拆句及人物旧绰号；固定 `little bunny`、`The Plumber`、`Eddie Four-Fingers` | `validate_translations.py --changed`、重复术语审计、`git diff --check` 通过；BOM/LF/末尾换行保持 |
| `tl/chinese/src/plot/ano12.rpy` | Tony/Maria 关系线元叙事占位 | Anon、Tony、Maria（被提及） | 完成 | 通读 4 个对话块和 1 条 strings，精修 5 处；与 `ano08.rpy` 的平行元叙事统一，并将随机奖励显示统一为“好感度中幅提升” | `validate_translations.py --changed`、`git diff --check` 通过；BOM/CRLF/末尾换行保持 |
| `tl/chinese/src/plot/ano13.rpy` | Tony/Maria 领养面谈；特殊披萨送餐；Tina 成人关系推进；Becca 撞见；Eddie 调查与领养失败 | Anon、Tony、Maria、Tina、Becca、Missy、Eddie Four-Fingers（被提及） | 完成 | 通读约 540 个翻译块并精修 268 处；修复特殊披萨配料、海滨公寓、成人场景强度、母女冲突、连续拆句、Eddie 英文姓名、十年刑期与探监调查逻辑；固定“冠军/小帅哥/美人儿”；按审查意见补强“额外香肠”的阴茎双关、区分动作义“肏”与感叹义“操”，并改用中文弯引号 | `validate_translations.py --changed` 验证 21 个修改文件；18 组重复术语审计零不一致；`git diff --check` 通过；BOM/LF/末尾换行保持；RPA 成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano14.rpy` | Tony 探监离城；Maria 独守披萨店；第四面墙强制引导 | Anon、Tony、Maria | 完成 | 通读 79 个翻译块并精修 67 处；区分多日条件分支和送餐成败回应，统一 Tony/Maria 老派口吻，修复第三次强制引导的元叙事、海滨公寓302室、好感度提示及全部活动译文 ASCII 省略号 | `validate_translations.py --changed` 验证 22 个修改文件；19 组重复术语审计零不一致；`git diff --check` 通过；BOM/CRLF/末尾换行保持 |
| `tl/chinese/src/plot/ano15.rpy` | 俄国人走私窝点情报；自然受孕交易；Tony/Maria/Anon 成人关系分支 | Anon、Tony、Maria、Eddie Four-Fingers（被提及） | 完成 | 通读 754 个翻译块并精修 490 处；修复俄国人情报、自然受孕条件、Maria 婚姻忠诚冲突、成人关系阶段和食物/棒球/性行为双关；固定“冠军”“补水最重要”“卡皮科拉火腿”“锉刀”等术语，并恢复 `Obi-Wan` 英文专名 | `validate_translations.py --changed` 验证 23 个修改文件；22 组重复术语审计零不一致；`git diff --check` 通过；RPA 成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/ano16.rpy` | Maria 怀孕确认；邀请 Anon 当教父；俄国人地址与版本结尾占位 | Anon、Tony、Maria | 完成 | 通读 52 个翻译块并精修 41 处；修复 `I'm ya guy` 反译、`champ` 称呼漂移、教父/黑帮双关、Tony/Maria 家人式关系、版本更新元叙事及活动译文 ASCII 省略号 | `validate_translations.py --changed` 验证 24 个修改文件；23 组重复术语审计零不一致；`git diff --check` 通过；RPA 成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/anon_chair.rpy` | Anon 卧室；检查卡死的椅子脚轮 | Anon | 完成 | 通读 5 个翻译块并精修全部译文；理顺用力、发现脚轮卡死及“没锁就好办”的连续思路 | `validate_translations.py --changed`、`git diff --check`、BOM/CRLF/末尾换行保持检查通过 |
| `tl/chinese/src/plot/anon_pc.rpy` | Anon 卧室；电脑故障、零件线索、道具检查、修复与画质升级 | Anon、mono | 完成 | 通读 15 个翻译块并精修 14 处；保留空 `mono` 块、Consum-R 专名、成人用品语境和电脑修复/高分辨率/游戏 BUG 元叙事 | `validate_translations.py --changed`、25 组重复术语审计零不一致、RPA 构建/校验通过 |
| `tl/chinese/src/plot/anon_phone.rpy` | 手机 Wi-Fi 设置连续点击彩蛋 | Anon | 完成 | 通读 8 个翻译块并精修 6 处；将八条警告整理为“查看信号—制止点击—识破意图—解锁作弊菜单”的递进序列 | `validate_translations.py --changed`、`git diff --check`、RPA 构建/校验通过 |
| `tl/chinese/src/plot/apt_empty.rpy` | 公寓入口；深夜与未受邀访问拦截 | Anon | 完成 | 通读 4 个翻译块并精修 3 处；修复 ASCII 省略号和“不请自来”的翻译腔，保持尴尬递进 | 本批 10 个 Ren’Py 文件格式校验通过 |
| `tl/chinese/src/plot/bank_hall.rpy` | 银行后场员工区拦截 | Anon | 完成 | 通读并精修 2 个翻译块；将地点指代改为自然的“后面/员工区”，保留擅入后果 | 本批格式校验通过 |
| `tl/chinese/src/plot/bank_lobby.rpy` | 银行闭店、周末营业与禁止逗留提示 | Anon、more | 完成 | 通读 7 个翻译块并精修 5 处；降低 `Dang it` 过度粗俗译法，修复直角引号并理顺“办事后离开”的连续思路 | 本批格式校验通过 |
| `tl/chinese/src/plot/bank_vault.rpy` | 银行金库上锁提示 | Anon | 完成 | 通读并精修 2 个翻译块；保留先自嘲“明知故说”再确认上锁的笑点 | 本批格式校验通过 |
| `tl/chinese/src/plot/car_garage.rpy` | 车行维修区拦截 | Anon | 完成 | 通读并精修 2 个翻译块；修复“它们修车”的代词错误及 ASCII 省略号 | 本批格式校验通过 |
| `tl/chinese/src/plot/car_lounge.rpy` | 车行员工休息区拦截 | Anon | 完成 | 通读并精修 2 个翻译块；自然化 `employee only vibes`，原样保留 `{i}` 标签 | 本批格式校验通过 |
| `tl/chinese/src/plot/car_shop.rpy` | 车行闭店与即将闭店提示 | Anon | 完成 | 通读 3 个翻译块并精修全部译文；统一自然简短的闭店提示语气 | `git diff --check`、RPA 打包/校验 328 个文件通过 |
| `tl/chinese/src/plot/erik_bed.rpy` | Erik 卧室；检查床底并发现书 | Anon | 完成 | 通读并精修 2 个翻译块；将 `dust bunnies` 自然化为“灰尘团”，保持先检查再发现物品的连续节奏 | 本批 13 个 Ren’Py 文件格式校验通过 |
| `tl/chinese/src/plot/erik_drawer.rpy` | Erik 卧室；检查凌乱抽屉 | Anon | 完成 | 通读并精修 3 个翻译块；修正 `dresser` 的“梳妆台”误译，保留对污渍的惊讶和嫌弃但不补写来源 | 本批格式校验、`git diff --check` 通过 |
| `tl/chinese/src/plot/tech_gamepad.rpy` | Erik 卧室；旧游戏手柄与童年回忆 | Anon、Erik（变量） | 完成 | 通读并精修 2 个翻译块；修复缺失主语、ASCII 省略号和生硬回忆表述，保留两人如今已很少一起玩的惋惜 | RPA 成功打包并验证 328 个文件 |
| `tl/chinese/src/plot/debbie_attic.rpy` | Debbie 家阁楼；借凳子进入与旧物期待 | Anon、Debbie、Dad（叙述中） | 完成 | 通读 4 个翻译块并精修全部译文；自然化进入阁楼与寻找垫脚物的表达，保留明确亲属称谓“爸爸”，修复 ASCII 省略号 | 本批格式校验通过 |
| `tl/chinese/src/plot/debbie_bed1.rpy` | Debbie 卧室；进入限制、睡眠与潜入状态提示 | Anon、Debbie（变量） | 完成 | 通读 4 个翻译块并精修全部译文；简化重复主语，统一卧室隐私和保持安静的内心独白语气 | 本批格式校验通过 |
| `tl/chinese/src/plot/debbie_canvas.rpy` | Debbie 家旧画布；回忆其绘画爱好 | Anon、Debbie（变量） | 完成 | 通读并精修 1 个翻译块；将生硬的过去时表达改为自然回忆，确认 Debbie 以前很喜欢画农场动物 | 本批格式校验通过 |
| `tl/chinese/src/plot/debbie_drawer.rpy` | Debbie 卧室；抽屉与内裤抽屉隐私提示 | Anon、Debbie（变量） | 完成 | 通读 3 个翻译块并精修全部译文；明确 `panty drawer` 为“内裤抽屉”，保留对玩家/自己的共同警告与越界感，不额外扩写 | 本批格式校验通过 |
| `tl/chinese/src/plot/debbie_landing.rpy` | Debbie 家楼梯平台；浴室门缝偷看提示 | Anon | 完成 | 通读 4 个翻译块并精修 3 处；修复病句和 ASCII 省略号，理顺发现门缝、好奇与自我开脱的心理递进 | 本批格式校验通过 |
| `tl/chinese/src/plot/photo_debbie_diane.rpy` | Debbie/Diane 夏令营旧照片 | Anon、Debbie、Diane（变量） | 完成 | 通读并精修 2 个翻译块；修复女性复数代词误用，保留两人年轻时共同参加夏令营的时间与情绪信息 | 本批格式校验通过 |

## 已完成的规则修复（剧情未全面精修）

| 文件 | 修复内容 | 后续要求 |
|---|---|---|
| `tl/chinese/base_box/sets.rpy` | “托尼披萨店”恢复为 `Tony披萨店` | 后续结合资源调用统一地点名称 |
| `tl/chinese/renpybox_bytecode_strings.rpy` | 四处手机任务提示将字面 `Anon` 按玩家视角改为“你”；玩家可见标签统一为 `{dom=强势}`、`{sub=顺从}`；其他姓名/变量保持原状 | 后续完整复核资源字符串 |
| `tl/chinese/res/meta/prop.rpy` | “凯文”恢复为 `Kevin`；按界面文本使用中文双引号：“光膀子的壮汉！” | 后续完整复核资源字符串 |
| `tl/chinese/res/meta/step.rpy` | “朱迪丝”恢复为 `Judith` | 后续完整复核资源字符串 |
| `tl/chinese/src/game.rpy` | `anon`、`Anon` 保持英文原拼写和大小写 | 后续完整复核全局字符串 |
| `tl/chinese/src/plot/ano01.rpy` | 将 12 处英文纯省略号误写的 `??` 全部恢复为中文省略号 `……` | 已随完整文件精修复核 |
| `tl/chinese/src/plot/jos01.rpy` | 删除英文原文没有的 `[saga.cast.tony]` 插值，保留 `Tony披萨店` | 必须完整通读后才能标记完成 |

## 全仓校验待修复队列

运行 `python tools/validate_translations.py --no-compare` 后，当前报告 **26 个既有问题**。这些问题先登记，按完整场景阅读结果逐项修复；明显程序格式错误可作为独立安全批次处理，但不得据此将剧情文件标记为完成。

### 变量、标签或占位符不一致

- `tl/chinese/res/meta/cast.rpy:97`：`[saga.cast.frank]` 数量多 1。
- `tl/chinese/src/plot/ano13.rpy:2577`：译文新增 `[saga.cast.becca]`。
- `tl/chinese/src/plot/cedric.rpy:50,57,190`：`[saga.cast.anon]` 或 `[saga.cast.cedric]` 增删不一致。
- `tl/chinese/src/plot/deb26.rpy:4201`：译文新增 `[saga.cast.debbie]`。
- `tl/chinese/src/plot/deb26.rpy:5198`：`{nw=.3}` 被改成 `{nw=2}`。
- `tl/chinese/src/plot/jen11.rpy:104`：译文新增 `[saga.cast.jenny]`。
- `tl/chinese/src/plot/jen14.rpy:904`：译文新增斜体标签。
- `tl/chinese/src/plot/jen17.rpy:97,1428`：译文新增 `[saga.cast.erik]`。
- `tl/chinese/src/plot/maria.rpy:151`：译文新增 `[saga.cast.anon]`。
- `tl/chinese/src/plot/mel03.rpy:374,678,902`：`Eve`/`Melody` 变量增删不一致。
- `tl/chinese/src/plot/tin02.rpy:930`：漏掉 `[saga.cast.tina]`。
- `tl/chinese/src/plot/tin_dusk.rpy:943`：译文新增 `[saga.cast.becca]`。
- `tl/chinese/src/plot/tony.rpy:22`：漏掉 `[saga.cast.tony]`。

### 错误插值或空译文

- `tl/chinese/src/plot/jen15.rpy:295,301,307`：普通内心独白被写成 `['中文']`，会被 Ren’Py 当作插值。
- `tl/chinese/src/plot/mel02.rpy:1856,1863,1870`：普通文本被写成 `['中文']`，会被 Ren’Py 当作插值。
- `tl/chinese/src/plot/deb26.rpy:5488`：非空英文对应空译文。
- `tl/chinese/src/plot/jen17.rpy:319`：非空英文对应空译文。

## 上下文与术语更新

- 已建立 `characters.md`、`terminology.md`、`storylines.md`、`style_guide.md`、`file_inventory.md`、`recurring_terms.md` 和机器可读的 `recurring_terms.json`。
- 固定强制规则：角色姓名、昵称、姓氏和特殊拼写按英文原文保留，不建立中文音译姓名；手机任务提示中用作玩家占位的字面 `Anon` 可按 UI 视角译为“你”。
- 已确认 `{dom=...}`、`{sub=...}` 的标签名必须保留，等号后的玩家可见文字必须汉化，统一为“强势/顺从”。
- 已补充 Dimitri 的危险、戏谑、非母语化语气档案，以及 `ano03.rpy` 的威胁和警务上下文。
- 已补充 Tammy 在离婚后通过照顾 Erik 获得被需要感的背景，并确认 `ano04.rpy` 中 Debbie 与 Anon 仍处于早期家庭适应阶段。
- 已补充 `ano05.rpy` 的驾车监视、警方留守、Anon 保护欲和 Debbie 责任边界；固定 `That's my boy!` 在本场译为“这才对嘛”，不得误建母子关系。
- 已补充 Igor 与 Tony 的角色档案，以及 `ano06.rpy` 的街头围堵、工作邀请、二十五万美元贷款和房屋抵押危机；固定 `Russkies`／`Russians`、`collateral`、`take his medicine` 等语境处理。
- 已补充 Maria 的经营核心、强势务实和粗俗比喻档案，并补全 Tony 在 `ano07.rpy` 中作为照顾型雇主的语气；固定“到店自取订单”“试送”“后厨”“贴身衣物”等场景术语。
- 已记录 `ano08.rpy` 的第四面墙式元叙事占位；`face time` 按当面相处处理，不使用“刷存在感”等偏离原意的网络化表达。
- 已补充 `ano09.rpy` 的 Tina 初见、Luigi 遗属承诺、车辆购买/置换分支和 Tony/Maria 意大利裔美国人口吻；固定 `champ`／`babyface`／`dollface` 及三组车辆名称。
- 已补充 `ano10.rpy` 的披萨教学、cannoli 奖励误导、Tony/Luigi 黑帮兄弟关系和不育诊断；固定 `protégé`→“徒弟”、`cannoli`→“意式奶油甜馅卷”、`mustache ride`→“骑胡子”及披萨制作术语。
- 已补充 `ano11.rpy` 的领养/精子捐赠分歧、俄式食品笑话、持枪闯店与 Raz 调查承接；固定 `little bunny`→“小兔子”，并确认 `The Plumber`、`Eddie Four-Fingers`／`Four-Fingers` 保持英文。
- 已记录 `ano12.rpy` 与 `ano08.rpy` 平行的元叙事占位；`moderate affection points` 与 `ano14.rpy` 统一为“好感度中幅提升”。
- 已补充 `ano13.rpy` 的特殊披萨送餐、Tina 成人关系推进、Becca 母女冲突、Eddie 服刑与探监调查、领养失败及捐精方案承接；固定 `prosciutto`→“意式风干火腿”、`gorgonzola`→“戈贡佐拉奶酪”、`calzone`→“意式烤饺”、`Beachside Apartments`→“海滨公寓”。
- 已补充 `ano14.rpy` 的探监离城、多日店务条件分支和第三次强制引导元叙事；固定“海滨公寓302室”，并保持动作RPG、更新版本和玩家选择座驾等第四面墙笑点。
- 已补充 `ano15.rpy` 的俄国人走私窝点情报、自然受孕条件、Maria 的婚姻忠诚冲突及 Tony/Maria/Anon 成人关系分支；固定“补水最重要”“卡皮科拉火腿”“锉刀”“骑胡子”和“意式烤饺”。`ano16.rpy` 进一步确认 Maria 怀孕、Anon 的教父身份和三人家人关系，并保留版本结尾元叙事。
- 审查反馈复核：`ano14.rpy` 的内部引述改用弯引号“……”；已处理的修改文件同步清除活动译文中的 `「……」`。`ano15.rpy` 的 `workplace seminar` 结合员工/老板场景确定为“职场性骚扰培训”，不是 Tony/Maria 的性交暗语。
- 已建立“短距离重复 2 次即触发”的跨文件复查机制；当前登记 25 组称呼、口癖、关系身份、连续笑点、专名、食品术语、地点和成人双关，并记录未处理文件中的既有不一致队列。
- 已固定首批系统术语：存档、读档、设置、物品栏、任务、城镇地图、时间段。
- 地点暂定统一为“夏日镇”；`Tony's Pizza` 按语境使用“Tony披萨店”。
- 已补充 Anon 卧室设备交互：椅子脚轮检查、电脑零件/修复/画质升级及手机 Wi-Fi 连点彩蛋；固定 `Consum-R` 保持英文、`cheat menu`→“作弊菜单”、游戏故障 `bugs`→“BUG”，并把手机八条提示作为连续递进场景处理。
- 已补充公寓、银行与车行的地点进入限制：统一使用简短内心独白表达深夜/未受邀访问、员工区、营业时间、禁止逗留和闭店逻辑，并修复代词、ASCII 省略号及活动译文直角引号。
- 已补充 Erik 卧室物品检查：床底灰尘与书、凌乱抽屉及旧游戏手柄回忆；保持 Anon/Erik 童年好友语气，不擅自解释抽屉污渍来源。
- 已补充 Debbie 家中短交互：阁楼旧物、卧室进入限制、绘画爱好、内裤抽屉隐私、浴室门缝与 Debbie/Diane 夏令营旧照片；修复女性复数代词，并补建 Diane 的英文姓名档案。

## 测试与校验状态

- `python -m py_compile tools/validate_translations.py tools/audit_recurring_terms.py`：通过。
- `python -X utf8 tools/validate_translations.py --changed`：本批通过，验证 1 个修改过的 Ren’Py 翻译文件；变量、标签、占位符、代码结构和活动译文标点均无异常。
- `python -X utf8 tools/audit_recurring_terms.py --changed --fail-on-mismatch`：本批涉及的已登记重复称呼、口癖、关系身份、连续笑点、专名和术语全部通过，零不一致。
- `python tools/validate_translations.py --no-compare`：报告 26 个仓库既有问题，已登记于上方队列。
- GitHub Actions 使用 Ren’Py 8.5.3 编译并运行 `tools/build_rpa.py`。
- 本机 PATH 中未发现 Ren’Py SDK；Ren’Py compile/lint 尚未运行。
- `python -X utf8 tools/build_rpa.py`：成功打包并校验 328 个文件（`dist/chinese.rpa`，42,285,105 字节；构建产物由 `.gitignore` 忽略）。

## 下一步

1. Maria 线现有 11 个文件及 Debbie 线 `deb01.rpy` 至 `deb12.rpy` 已完成；下一批继续完整通读并精修 `deb13.rpy`。
2. 进入后续文件前先查阅 `recurring_terms.md`；遇到重复表达立即做全仓查询并登记，不再只在当前场景内定译。
3. 每批继续完成三轮校对、逐文件格式检查、重复术语审计和 RPA 构建校验。
4. 在进入对应剧情文件时，按完整场景处理全仓校验队列中的 26 个既有格式问题。
