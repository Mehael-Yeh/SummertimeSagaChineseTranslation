# 翻译精修进度

更新时间：2026-08-05

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
| `tl/chinese/src/plot/deb13.rpy` | Debbie线；汽车发动机损坏、Josie 保修/付款分支、Jiang 上门修车及车内关系推进 | Debbie、Anon、Josie、Jiang | 完成 | 通读 486 个对话块和 4 个选项；理顺车辆损坏、八千美元维修费、延长保修与自费分支，精修 Josie 的电话性暗示和 `bowl cut` 固定挖苦、Jiang 的修车/性双关，以及 Debbie 与 Anon 从责任感安慰推进到独处接吻、触碰勃起但仍拒绝进一步性接触的边界变化；统一中文省略号、双引号、内心括号和车辆术语 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb14.rpy` | Debbie线；再次偷拿内裤自慰、Debbie撞见、观看自慰、射精及浴室私下自慰 | Debbie、Anon、Mia（被提及） | 完成 | 通读 193 个对话块和 5 个选项；区分接受、退让及同龄女生建议分支，保留 Debbie 的真实吸引与照顾者边界、Anon 的欲望和越界责任；统一中文省略号、内心括号、菜单标点及 Anon 对 Debbie 的 `ma’am`“夫人”称呼 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb15.rpy` | Debbie线；浴室偷窥、擅自闯入与隐私边界重申 | Debbie、Anon、Jenny（被提及） | 完成 | 通读 40 个对话块和 2 个选项；理顺 Anon 将此前亲密许可误判为更广泛同意、闯入浴室后被 Debbie 制止及双方事后自责的逻辑；保留 Debbie 对 Anon 的吸引与明确隐私边界，统一中文省略号、内心括号和连续拆句 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb16.rpy` | Debbie线；Jenny遗留色情片、房东房客剧情映照、共同自慰与事后关系确认 | Debbie、Anon、Jenny、色情片角色 | 完成 | 通读 281 个翻译块；理顺 Anon 被色情片挑起欲望、Debbie 撞见后允许继续、双方互相观看自慰与描述幻想、Debbie 高潮、Anon 射精及事后罪恶感安抚；统一 `landlady`“房东太太”、中文省略号、内心括号和 Anon 对 Debbie 的 `ma’am`“夫人”，保留“只此一次”的真实边界 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb17.rpy` | Debbie线；共同自慰后的夜间反思、潜入卧室触摸 Anon 及主动停止越界 | Debbie、Anon | 完成 | 通读 66 个翻译块；理顺 Debbie 从罪恶感、自我否认转向偷看、隔着内裤触摸、直接抚弄阴茎及性交幻想，保留她以“帮忙”为借口的自我合理化和最终主动离开的真实边界；统一中文省略号、内心括号、成人动作强度及睡梦语气 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb18.rpy` | Debbie线；俄罗斯打手入侵、Anon保护 Debbie、浴室照顾与首次主动手淫 | Debbie、Anon、Jenny、Dimitri、Igor、Yumi、Harold、Raz（被提及） | 完成 | 通读 178 个翻译块；理顺打手入侵、Anon受伤、报警掩护、Debbie自责及以照顾和奖励为由主动手淫的关系推进；保留 Dimitri 的性威胁、Igor 的迟钝笑点、Debbie 照顾者式色情口吻及“只能到手淫”为止的新边界；统一中文省略号、内心括号和姓名变量 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb19.rpy` | Debbie线；失眠夜谈、丧亲孤独、主动同床与首次性交 | Debbie、Anon、Jenny（被提及）、Diane（被提及） | 完成 | 通读 304 个翻译块；理顺助眠药、亡夫留下的空床、Anon 不愿趁脆弱推进关系及 Debbie 主动邀请同床的情感基础；完整精修亲吻、身体爱抚、口交、摩擦、首次插入性交、互相表白、拔出/内射及多阶段停止分支，保留每个分支的真实同意边界和次日谨慎重复约定；统一中文省略号、内心括号、女性高潮表达及 `ma’am`“夫人” | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb20.rpy` | Debbie线；厨房偷听、向 Diane 复盘关系升级及道德顾虑疏导 | Debbie、Diane、Anon | 完成 | 通读 154 个翻译块；理顺从献殷勤、自慰被撞见、摆姿势帮助射精、共同洗澡到手淫的完整复盘；区分 Debbie 的羞耻、受用与年龄/照顾者负罪感，强化 Diane 开放直白的闺蜜调侃，并保留 Anon 偷听后选择给 Debbie 时间消化的边界 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb21.rpy` | Debbie线；Jenny母女冲突、陪看烘焙节目、沙发亲密升级及乳交被撞见 | Debbie、Anon、Jenny | 完成 | 通读 305 个翻译块；理顺 Debbie 因 Jenny 冷落而受伤、Anon 安慰和表白、舔舐与高潮后主动止步、继续依偎、乳交及 Jenny 撞见后的冲突；修复损坏文本、英文姓名音译、连续拆句和成人动作表达，并保持 Debbie 的照顾者语气、真实欲望与越界负罪感并存 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb22.rpy` | Debbie线；深夜进入Anon房间、欲望自辩、主动口交及梦魇分支 | Debbie、Anon、Diane（被提及）、Jenny（被提及）、Ursula（梦境） | 完成 | 通读 121 个对话块和 2 个菜单选项；理顺 Debbie 从房东/照顾者负罪感到接受自身欲望、主动触摸与口交、Anon 醒来后的惊慌逃离，以及追赶/回床分支和 Ursula 梦魇；统一内心括号、省略号、连续拆句与重复台词，并保留 Debbie 成熟照顾口吻和真实成人欲望 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb23.rpy` | Debbie线；深夜口交后的回避、渡鸦山私谈和解及Cupid泳衣试穿 | Debbie、Anon、Kassy | 完成 | 通读完整场景；理顺 Debbie 因趁 Anon 熟睡口交而自责回避、双方在渡鸦山区分熟睡时无法回应与醒来后的真实愿望、和解后再次主动口交，以及Cupid蓝色／紫色／白色泳衣试穿和试衣间“搭扣卡住了”的掩饰；保留 Debbie 的身体不自信、房东身份顾虑与真实欲望 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb24.rpy` | Debbie线；泳池裸泳、Diane推动Debbie正视欲望、浴袍搜索及拒绝同床 | Debbie、Diane、Anon、Jenny（浴室分支） | 完成 | 通读 342 个翻译块；修复 Anon 未来家庭归属的指代错译，理顺跨块连续句；精修手淫、口交、乳交、隔衣磨蹭、舔阴／舔肛及泳池挑逗；统一女性复数、中文括号、省略号和浴袍搜索分支口吻 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb25.rpy` | Debbie线；泳池挑逗后的欲望失控、夜间游荡、首次主动性交及次日退缩 | Debbie、Anon、Jenny（被提及）、Diane（被提及）、色情片角色 | 完成 | 通读 428 个翻译块；精修 Debbie 在家中转移注意力却不断联想到 Anon 的连续场景、主动口交与首次明确要求插入、性交和高潮、内射／拔出分支、事后爱意及次日因年龄差和房东责任退缩；修复眼镜蛇和 `gotten into` 双关、连续拆句、女性高潮、复述引号及成人表达强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
| `tl/chinese/src/plot/deb26.rpy` | Debbie线；Diane出谋划策、Cupid礼服、Ara Ara正式约会与关系公开 | Debbie、Anon、Diane、Jenny、Hana、Titomi | 完成 | 通读853个翻译块；理顺Diane劝Anon坚定沟通、送礼服、正式约会、未来承诺、女体盛与普通点餐分支、回家性交及次日公开亲密；统一`Charge`结账语义、`succulent`误读笑点、Diane的`stud`称呼、Anon对Debbie的`ma’am`“夫人”；保留Cupid、Ara Ara及英文姓名 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb27.rpy` | Debbie线；傍晚泳池调情、裸体跳水、被发现风险与泳池性交 | Debbie、Anon、Jenny（被提及）、邻居（被提及） | 完成 | 通读133个翻译块；精修泳池邀约、忍者神龟笑点、裸体跳水、性交、被邻居或Jenny发现的刺激、高潮失控及事后含糊告别；理顺三组连续拆句，统一`Cowabunga`复述、`sweetie`“亲爱的”、中文括号、省略号和双引号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过（327个文件） |
| `tl/chinese/src/plot/deb_baby.rpy` | Debbie生育支线；怀孕确认、Jenny知情、孕期日常、生产、医院恢复、母婴回家与产后照顾 | Debbie、Anon、Jenny、Diane、Micoe、新生儿 | 完成 | 通读758个翻译块及16个菜单项；精修怀孕阶段关系变化、Frank冷冻精子圆谎、单胎/双胎分支、父亲身份掩饰、医院和产后代词、房客身份错位笑点、托儿所及乳头刺激双关；清除“娃娃脸”等误译 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过（327个文件） |
| `tl/chinese/src/plot/deb_island.rpy` | Debbie支线；厨房中岛台调情、Jenny撞见风险、舔阴与台面性交、体外射精/内射分支 | Debbie、Anon、Jenny、Jane（被提及） | 完成 | 通读153个翻译块及2个菜单项；精修关系后期的主动调情、房东身份玩笑、舔阴和台面性交；理顺Jenny在家/外出、连续拆句、女性高潮及体外射精/内射差异；统一`landlady`“房东太太”、中文省略号和成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过（327个文件） |
| `tl/chinese/src/plot/deb_kitchen.rpy` | Debbie支线；早餐厨房调情、Jenny在旁/洗澡/不在分支、从背后性交及内射/体外射精 | Debbie、Anon、Jenny | 完成 | 通读205个翻译块及1个菜单项；精修“香肠肉饼”“拍松肉”“更能填饱我”等连续食物/性双关，理顺Jenny发现风险、女性高潮与潮喷、射精主语、腿软连续句、房东身份调情和事后清理；统一中文省略号、括号与成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过（327个文件） |
| `tl/chinese/src/plot/deb_laundry.rpy` | Debbie支线；洗衣房调情、洗衣量/射精量双关、烘干机乳交、骑乘性交及内射/体外射精 | Debbie、Anon、Jenny（被提及） | 完成 | 通读332个翻译块及2个菜单项；精修`load`与`spin cycle`双关、连续拆句、`boobs`/`breasts`/`tits`用词层级、房东身份调情、女性高潮与射精主语，并理顺事后家务及晚餐过渡 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过（327个文件） |
| `tl/chinese/src/plot/deb_lobby.rpy` | Debbie支线；客厅中的亲密互动、Jenny回家风险及成人关系推进 | Debbie、Anon、Jenny（被提及） | 完成 | 通读完整场景；精修房东太太身份调情、亲吻、性交及内射/体外射精分支；统一 `landlady`→“房东太太”、`sweetie`→“亲爱的”、中文省略号和成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_mall.rpy` | Debbie支线；商场购物、车内亲密互动与怀孕后日常 | Debbie、Anon、Jenny（被提及） | 完成 | 通读完整场景；精修购物闲聊、车内接吻、Raven Hill 骑乘与口交分支、一起高潮、体外/内射和怀孕后日常；统一 `sweetie`、中文省略号、弯引号、人物语气及成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_pants.rpy` | Debbie支线；Debbie发现Anon自慰、留下观看并主动调情，随后进入射精与事后清理分支 | Debbie、Anon | 完成 | 通读完整场景；精修偷窥/自慰发现、Debbie主动观看与鼓励、射精到身上、事后安抚及“憋得太久”的支线双关；统一`sweetie`“亲爱的”、中文省略号、喘息表达、英文姓名和成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_pool.rpy` | Debbie支线；泳池边泳装调情、户外性交及邻居撞见风险 | Debbie、Anon、Tammy、Erik、Harold、Helen（被提及） | 完成 | 通读完整场景；精修泳装赞美、泳池边主动调情、邻居与熟人可能撞见的紧张感、性交节奏及 Debbie 的高潮前连续拆句；统一 `sweetie`“亲爱的”、中文省略号、全角括号、英文姓名和成人动作强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_shower.rpy` | Debbie支线；浴室偷窥、淋浴性交、口交与边界重申 | Debbie、Anon、Jenny（被提及） | 完成 | 通读完整场景；精修浴室雾气、偷窥与关系阶段变化；理顺肛门相关双关、口交射精、互相清洗、抚摸/手淫和停止分支；统一 `ma’am`→“夫人”、`landlady`→“房东太太”、`my boy`→“我的好男孩”、中文省略号及女性高潮表达 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_sink.rpy` | Debbie支线；浴室洗澡/自慰、舔阴、洗手台性交与房东房客双关 | Debbie、Anon、Jenny（被提及） | 完成 | 通读完整场景；精修浴室调情、舔阴、女性高潮、洗手台性交、内射/暂缓分支及事后房东房客双关；统一 `ma’am`→“夫人”、`sweetie`→“亲爱的”、`landlady`→“房东太太”、中文省略号和成人表达强度 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_sleep.rpy` | Debbie支线；Debbie与Anon同床过夜、早晨亲吻及避开Jenny的离开互动 | Debbie、Anon、Jenny（被提及） | 完成 | 通读完整场景；精修同床邀约、拥抱安抚、早晨调情、`good boy`与`ma’am`称呼、避开Jenny的紧张感；修复中文省略号、变量与菜单选项表达 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_utility.rpy` | Debbie线；地下室/公用设施区域短交互；Anon与Debbie的日常碰面及暧昧关系延续 | Debbie、Anon | 完成 | 通读完整短场景；修复地下室方向、日常询问、突然撞见和安慰语气；统一 `sweetie`→“亲爱的”、中文省略号与自然口语，保留英文姓名、变量和 Ren’Py 结构 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA构建通过 |
| `tl/chinese/src/plot/deb_visit.rpy` | Debbie线；夜间唤醒、多轮性交、怀孕后性欲与拒绝继续分支 | Debbie、Anon | 完成 | 通读完整场景；理顺 Debbie 的羞愧、内疚、主动欲望和怀孕后激素影响；修复连续拆句、女性高潮表达、内射与拔出分支及 `sweetie`、`ma’am`、`landlady` 称谓；活动译文统一使用中文省略号和中文双引号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过 |
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
| `tl/chinese/src/plot/jen01.rpy` | Jenny线；浴室偷窥、被发现及前期敌对关系 | Jenny、Anon、Debbie（被提及） | 完成 | 通读完整场景并精修 31 个翻译块；将 `You! / Little! / PERVERT!!!` 作为被吹风机击打打断的连续辱骂处理，修复“娃娃脸”误译；保留偷窥事实、Jenny 的尖刻攻击性及 Anon 求情逻辑，统一中文省略号与标点 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过（327 个文件） |
| `tl/chinese/src/plot/jen02.rpy` | Jenny线；新衣争执、求职压力、搬家宣言及家庭责任对照 | Jenny、Debbie、Anon | 完成 | 通读完整场景并精修 58 个翻译块；恢复 `Consum-R` 英文专名，理顺 Jenny 的讽刺与负担感、Debbie 的经济压力和安抚、Anon 的挖苦与体谅；统一 `sweetie`“亲爱的”、`good boy`“好男孩”及连续拆句 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过（327 个文件） |
| `tl/chinese/src/plot/jen03.rpy` | Jenny线；早餐赌气、借款争执及赚钱计划铺垫 | Jenny、Debbie、Anon、Diane（被提及） | 完成 | 通读完整场景并精修 67 个翻译块；承接 `jen02.rpy` 的家庭争执，理顺 Jenny 拒绝早餐、借六十美元、含糊赚钱计划与学费压力；区分 Jenny 的讽刺、Anon 的反驳和 Debbie 的照顾者语气，统一 `sweetie`“亲爱的”、中文省略号及活动译文标点 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过（327 个文件） |
| `tl/chinese/src/plot/jen04.rpy` | Jenny线；夜间色情影片角色扮演、再次偷窥、吹风机反击与勒索 | Jenny、Anon、Debbie（被提及）、影片男声 | 完成 | 通读完整场景并精修 63 个翻译块；理顺 Anon 误以为 Jenny 带男人回家、发现她跟随影片进行角色扮演、暴露后再次挨打及按现金量分支交钱的因果；统一 Jenny 对 Anon 的 `perv/pervert` 为“变态”，将色情角色称谓 `Daddy` 译为“爸爸”并与真实亲属关系区分，保留成人内容强度及中文引号、省略号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过（327 个文件） |
| `tl/chinese/src/plot/jen05.rpy` | Jenny线；Sluttygram 赚钱计划、首次合作拍摄性感照片与关系短暂缓和 | Jenny、Anon | 完成 | 通读 129 个翻译块和 7 项拍照选项；理顺粉丝焦虑、社交媒体建议、拒绝回 Consum-R、逐步增加暴露程度及拍完立即赶人的关系变化；恢复 `Sluttygram`、`Consum-R` 英文专名，统一 `perv`“变态”、本场 `wimp`“窝囊废”、连续拆句、拍摄评价和中文省略号 | `validate_translations.py --changed`、`audit_recurring_terms.py --changed --fail-on-mismatch`、`git diff --check`、RPA 构建通过（327 个文件） |

## 已完成的规则修复（剧情未全面精修）

| 文件 | 修复内容 | 后续要求 |
|---|---|---|
| `tl/chinese/base_box/sets.rpy` | “托尼披萨店”恢复为 `Tony披萨店` | 后续结合资源调用统一地点名称 |
| `tl/chinese/renpybox_bytecode_strings.rpy` | 四处手机任务提示将字面 `Anon` 按玩家视角改为“你”；玩家可见标签统一为 `{dom=强势}`、`{sub=顺从}`；恢复 `Sluttygram` 英文专名，并补译 Debbie 的洗衣篮手机留言；其他姓名/变量保持原状 | 后续完整复核资源字符串 |
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
- `python -X utf8 tools/validate_translations.py --changed`：本批通过，验证 6 个修改过的 Ren’Py 翻译文件；变量、标签、占位符、代码结构和活动译文标点均无异常。
- `python -X utf8 tools/audit_recurring_terms.py --changed --fail-on-mismatch`：本批涉及的已登记重复称呼、口癖、关系身份、连续笑点、专名和术语全部通过，零不一致。
- `python tools/validate_translations.py --no-compare`：报告 26 个仓库既有问题，已登记于上方队列。
- GitHub Actions 使用 Ren’Py 8.5.3 编译并运行 `tools/build_rpa.py`。
- 本机 PATH 中未发现 Ren’Py SDK；Ren’Py compile/lint 尚未运行。
- `python -X utf8 tools/build_rpa.py`：成功打包并校验 327 个文件（`dist/chinese.rpa`，42,313,279 字节；构建产物由 `.gitignore` 忽略）。

## 下一步

1. Maria 线现有 11 个文件、Debbie 主线及已登记支线已完成；Jenny 主线 `jen01.rpy` 至 `jen05.rpy` 已完成，下一批按数字顺序继续完整通读并精修 `jen06.rpy`。
2. 进入后续文件前先查阅 `recurring_terms.md`；遇到重复表达立即做全仓查询并登记，不再只在当前场景内定译。
3. 每批继续完成三轮校对、逐文件格式检查、重复术语审计和 RPA 构建校验。
4. 在进入对应剧情文件时，按完整场景处理全仓校验队列中的 26 个既有格式问题。
