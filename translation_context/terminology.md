# 术语与称谓规范

更新时间：2026-08-04

## 角色姓名（强制）

- 不建立中文音译姓名表。英文姓名、姓氏、全名和作为人物专名使用的昵称按原文原样保留。
- `babyface`、`dollface`、`champ` 这类本身带有明确语义、用于称呼对方的描述性亲昵称呼，不视为人物专名；应结合人物关系建立稳定中文，不能因形式像昵称就机械保留英文。
- 已确认必须恢复的形式：`Anon`（剧情对话、叙述和姓名字段不得写“匿名/你”）、`Tony`（不得写“托尼”）、`Tammy`（不得写“塔米”）、`Kevin`（不得写“凯文”）、`Judith`（不得写“朱迪丝/朱迪思”）。
- **UI 玩家占位例外**：手机任务提示等界面文本若把字面 `Anon` 当作玩家占位，并因此绕过玩家自定义姓名，可按界面视角译为“你”；该例外不得扩展到剧情对话、叙述或普通姓名。
- 原文使用变量时保留变量，例如 `[saga.cast.debbie]`、`[saga.cast.jenny]`。不得把字面姓名改成变量，也不得把变量改成字面姓名。
- 身份称谓可翻译，姓名部分不变：`Bissette老师`、`Johnson太太`、`Bridget教练`、`Smith校长`、`Harris医生`。

## 重复术语复查机制

- 同一英文名词、组合词、称呼或固定表达在短距离内出现 2 次及以上时，先视为潜在专名、人物口癖或专属称呼，必须执行全仓复查。
- 人工记录见 `recurring_terms.md`，机器可读规则见 `recurring_terms.json`；使用 `tools/audit_recurring_terms.py` 查询全仓对应和检查本批一致性。
- 确认稳定译法后才写入本术语表。未通读的跨文件命中只加入复查队列，不进行无上下文批量替换。

## 当前已确认地点与活动

| 英文 | 统一中文 | 说明 |
|---|---|---|
| Summerville | 夏日镇 | 当前项目既有译法；后续逐文件复核一致性 |
| Summerville College | 夏日学院 | 当前项目既有译法；学校语境统一使用 |
| Tony’s Pizza / Tony's Pizza | Tony披萨店 | Tony 保持英文，不得写“托尼披萨店” |
| Sorority Ball | 姐妹会舞会 | 序章目标文本采用此译法 |

## 系统与界面文本

| 英文 | 统一中文 |
|---|---|
| save | 存档 |
| load | 读档 |
| settings | 设置 |
| inventory | 物品栏 |
| satchel icon | 背包图标 |
| quest | 任务 |
| morning | 早晨（自然口语中可用“早上”） |
| afternoon | 下午 |
| evening | 傍晚 |
| night | 夜晚 |
| moderate affection points +[...] | 好感度中幅提升 +[...] |

## 关系与亲属称谓

- 英文原文使用 `Mom`、`Dad`、`Sis`、`Aunt` 等明确关系称谓时，可按角色口吻翻译。
- 英文原文使用姓名时，不得替换成关系称谓。
- 同一角色对另一角色的称呼变化必须有剧情依据，并记录在 `characters.md` 或对应剧情线档案中。

## 成人内容用词层级

- 原文委婉则保持委婉；原文明确则明确；原文粗俗则保留粗俗感。
- `fuck`、`cock`、`pussy`、`dick` 等不得脱离场景机械统一；需按愤怒、强调、调情、性行为、辱骂等功能选择中文。
- “操/肏/鸡巴/屄/骚货”等词没有自动禁用规则，但不得为了刺激擅自升级原文。女性角色明确要求与对方发生性行为，且中文使用“操某人／操屄”一类动作结构时，优先写作“肏”；感叹、惊讶、生气和辱骂中的“操”不变。双关语按语境可使用“干”。
- 呻吟和喘息需按惊讶、疼痛、快感、迟疑、愤怒等情绪区分，不让所有角色使用同一套拟声词。

### 日常护理、私人物品与自慰表达

| 英文 | 统一中文 | 说明 |
|---|---|---|
| `lotion` | 润肤露 | 日常身体护理语境；具体产品为膏霜质地时可按产品名写“润肤霜” |
| `Brazilian Bum Bum Cream` | 巴西 Bum Bum 润肤霜 | 保留产品名中的 `Bum Bum`，不将其误当角色姓名或普通臀部描写 |
| `solid`（电影暧昧场景） | 挺得住 | 同时保留“能承受情色画面”和勃起坚挺的双关；后句可用“应付得来”解释表层含义 |
| `masturbation` / `masturbate` | 自慰 | 直接、中性地表达行为，不净化为“解决需求”等含糊说法 |
| `panties` / `underwear` | 内裤 | 按单复数和指代自然组织中文；`mom panties` 可译“妈妈穿的内裤”，不使用生硬的“妈妈内裤” |
| `ma’am`（Anon 对 Debbie） | 夫人 | 体现房东与房客之间带亲近感的礼貌；不得在“夫人”“女士”“长官”之间漂移 |
| `landlady`（色情片房东房客设定） | 房东太太 | `deb16.rpy` 色情片及其现实映照中的固定称呼；不同于 Anon 对 Debbie 的 `ma’am`“夫人” |
| `British Baking` | 英国烘焙节目 | 剧中电视节目；同一场景反复出现时保持一致，不擅自补成现实节目全名 |
| `banoffee pie` | 太妃香蕉派 | 香蕉、打发奶油、焦糖酱和饼干底组成的甜点 |
| `That's my good boy!`（后期成人语境） | 这才乖嘛！ | Debbie 的照顾者式亲昵称呼进入成人场景后的表达；不译成母子关系 |

## Debbie 线商场专名与调侃

| 英文 | 统一中文 | 说明 |
|---|---|---|
| Cupid | Cupid | 商场女装精品店名称，保持英文 |
| FunBiz Pizzeria Pub | FunBiz披萨酒吧 | Debbie 十六岁时第一份工作的地点；`FunBiz` 保持英文 |
| Billy-bear | Billy-bear | FunBiz 舞台吉祥物名称，保持英文拼写和连字符 |
| Rock-a-Billy Pants Explosion | Rock-a-Billy Pants Explosion | FunBiz 的拟人动物乐队名称，保持英文原名 |
| Casanova（Kassy 调侃 Anon） | 情圣 | 泛称式调侃，不使用中文音译“卡萨诺瓦” |

## Ren’Py 特殊内容

- `[变量]`、`{标签}`、`%(变量)s`、`%s`、`%d`、转义字符和文本标签必须与英文源字符串保持同一集合和拼写。
- `{dom=...}`、`{sub=...}` 是自定义显示标签：标签名 `dom`/`sub` 必须保留，等号后的内容会显示给玩家，必须汉化。当前统一写作 `{dom=强势}`、`{sub=顺从}`。
- 不得把内心独白的普通圆括号改成方括号；Ren’Py 会把 `[...]` 识别为插值表达式。
- 台词内引述优先使用中文弯引号 `“……”`，避免 `「……」`；不得把外层 Ren’Py 字符串的 ASCII 双引号误改进文本。

## 学校与开局主线术语

| 英文 | 统一中文 | 说明 |
|---|---|---|
| Athletics class | 体育课 | 不机械译作“田径课”；具体赛事另行区分 |
| locker combination | 储物柜密码 | `combination` 在该场景指密码组合 |
| master key | 万能钥匙 | 保留剧情中可打开校内门锁/储物柜的功能含义 |
| Student Union President | 学生会主席 | Annie 身份 |
| hallway monitor | 走廊风纪委员 | Annie 身份；不要译成成人社会职务 |
| cafeteria duty | 食堂帮工 | Kevin 受罚场景 |
| private / one-on-one tutoring | 一对一辅导 | Viv 课后辅导；按场景可写“单独辅导”但不要误成普通课程名称 |
| Muay Thai | 泰拳 | `kickboxing` 另译“踢拳” |
| GPA | GPA | 保留英文缩写 |
| Whorecraft | Whorecraft | 游戏内作品名，暂保留英文 |
| Consum-R | Consum-R | 商场店名，保留原拼写和连字符 |

## `ano01.rpy` 游戏双关

- `carrot hole` → “胡萝卜洞”。
- `bunny hole` → “兔子洞”。
- `bunny bum-bum` → “兔兔屁屁”。
- 以上是 Erik 所玩色情游戏里的幼稚双关，仅在该游戏语境保持一致，不作为全项目身体部位通用术语。

## `ano02.rpy` 调查与金融术语

| 英文 | 统一中文 | 说明 |
|---|---|---|
| Saga Financial Bank | 传说金融 | 沿用仓库既有机构名；对话中无需机械补“银行” |
| autopsy report | 尸检报告 | 警方调查语境 |
| asphyxiation | 窒息 | 保持死因信息，不弱化成“呼吸困难” |
| bank teller | 银行柜员 | Liu Wang 的职务 |
| offshore account | 境外账户 | 当前场景指电子转账的资金去向 |
| launder money | 洗钱 | 明确犯罪含义，不委婉化 |
| 10-62 | 10-62 | 警务代码保留原数字与连字符，不自行扩写含义 |
| Bedtime Bandit | “晚安大盗” | 本地窃贼的戏称；保留昵称式引号，后续出现时复核一致性 |
## `ano03.rpy` 威胁与警务术语

| 英文 | 统一中文 | 说明 |
|---|---|---|
| APB | 协查通报 | 警方向巡逻警员发布车辆/人员查找信息的语境 |
| get/take a statement | 做笔录 | 询问并记录证人陈述；不机械译作“拿声明” |
| criminal organization | 犯罪组织 | 保持组织犯罪含义 |
| squad car | 警车 | 日常剧情无需展开车型 |
| patrol / monitor the neighborhood | 巡逻 / 留意周边 | 按具体句式处理，不机械统一 |
| assertive route | 强势路线 / `{dom=强势}` | 界面标签值必须中文显示 |
| submissive route | 顺从路线 / `{sub=顺从}` | 界面标签值必须中文显示 |

## `ano04.rpy` 丧亲慰问与生活语境

| 英文 | 统一中文 | 说明 |
|---|---|---|
| give/offer condolences | 表示慰问 / 说声节哀 | 根据人物亲疏调整，不机械译作“给予哀悼” |
| sublet | 转租 | 当前场景指 Tammy 将自己的房子转租出去 |
| come out of one’s shell | 慢慢开朗起来 / 不再封闭自己 | 按角色口吻处理，避免直译“走出壳” |

## `ano05.rpy` 监视、家庭安全与语用

| 英文 | 当前处理 | 说明 |
|---|---|---|
| keep on driving | 没停车，直接开走 | 当前场景强调车辆未停下，不译成“一直开着车” |
| a lot of good that's doing us | 可真是帮了我们大忙 | 反讽警方迟迟没有进展，不能按正面陈述翻译 |
| bond / bonding | 增进感情 | Debbie 希望 Jenny 与 Anon 改善同住关系，不擅自写成恋爱或亲属关系 |
| labia | 阴唇 | Jenny 的露骨厌恶比喻；保持身体部位准确，不净化，也不额外升级 |
| That's my boy! | 这才对嘛！ | 鼓励性习语；本场不能译成“这才是我儿子” |
| a cute girl down the street | 街那头那个可爱的女孩 | `down the street` 表示附近方位，不译成随机的“街上女孩” |

## `ano06.rpy` 追债、黑帮与房贷术语

| 英文 | 当前处理 | 说明 |
|---|---|---|
| Tony's Pizza / Tony’s Pizza | Tony披萨店 | Tony 为英文姓名，不写作“托尼披萨店” |
| little bunny | 小兔子 | Dimitri 对 Anon 的固定嘲弄；与 Frank 生前的求饶呼应 |
| break both hands | 两只手都打断 | 明确的暴力威胁，不弱化成笼统“教训” |
| hand sanitizer | 洗手液 | Igor 搜身误抓阴茎后的洁癖笑点，必须保留场景因果 |
| put the screws on | 施压／逼迫／把矛头转向 | 按主宾关系处理，不直译成“上螺丝” |
| take his medicine | 认罚／承受后果 | 指接受犯罪组织惩罚，不按字面译“吃药” |
| snuff out your entire family | 灭门／杀光全家 | Tony 对犯罪组织手段的警告，暴力强度不得弱化 |
| Russkies | 俄国佬 | Tony 的贬义粗俗说法；与普通 `Russians` 区分 |
| Russians | 俄国人 | 中性识别国籍，不机械套用“俄国佬” |
| Das vidania | 达斯维达尼亚 | Tony 故意装腔的俄语告别梗，保留异国语感和挑衅口吻 |
| loan | 贷款 | Debbie 为支付二十五万美元而借款 |
| collateral | 抵押物／拿房子作抵押 | `used the house as collateral` 译“拿房子作了抵押” |
| put up the house | 拿房子作抵押 | 与 `collateral` 统一，不误译成出售房屋 |


## `ano07.rpy` 披萨店雇佣与送餐术语

| 英文 | 当前处理 | 说明 |
|---|---|---|
| dine in | 堂食 | 与到店自取、外送并列的经营方式 |
| pick up / collection order | 到店自取／到店自取订单 | 指顾客自行到店领取，不译成“收款订单”或普通取货 |
| delivery boy | 送餐员／送餐小子 | Tony披萨店的披萨外送岗位；正式描述用“送餐员”，Tony／Maria 口语中可说“送餐小子” |
| trial run | 试送／试送一趟 | 指正式录用前的送餐测试，不译成泛化的“试运行” |
| perfect run | 完美完成的一趟送餐 | Tony 因全部订单正确送达而额外发放奖金 |
| kitchen | 后厨 | 披萨店工作区语境；家用烹饪场景仍可按语境译“厨房” |
| unmentionables | 贴身衣物 | Maria 指先前被 Anon 意外看到的私密衣物，保留尴尬但不擅自改成裸体 |
| brains of the operation | 全靠她拿主意 | 强调 Maria 是实际经营核心，不直译“行动的大脑” |
| heart and soul | 主心骨 | 与上一句连续，说明 Maria 对店铺不可或缺 |
| capisce? | 懂了没？ | Tony 的固定江湖化口头表达，保留压迫或催促感 |

## `ano09.rpy` 专属称呼、车辆与意大利裔口吻

| 英文 | 当前处理 | 说明 |
|---|---|---|
| champ | 冠军 | Tony 对 Anon 的固定专属称呼；仅在英文明确使用 `champ` 时采用，不替代普通 `kid`／`kiddo` |
| babyface | 小帅哥 | Tina 对 Anon 的固定专属称呼；非称呼用法不得机械译成“娃娃脸”，应按语境处理为“长着娃娃脸的年轻人”等自然表达 |
| dollface | 美人儿 | Maria／Tony 使用的老派亲昵称呼；不是人物专名，不保留英文 |
| kid / kiddo | 小子／好小子 | 按责备、鼓励或熟稔语气选择，不与 `champ` 混用 |
| Yes, sir! | 遵命，老板！ | Anon 对 Tony 的玩笑式或恭敬回应；当前是雇佣关系，不机械译“先生” |
| Yes, ma’am. | 是，老板娘。 | Anon 对 Maria 的恭敬回应；结合披萨店经营关系处理 |
| scooter | 踏板车 | 与自行车、汽车分支区分 |
| car dealership / dealership | 车行 | 购买、置换车辆的场所 |
| trade-in | 旧车折价／旧车抵价 | 根据句式写“旧车抵了不少钱”“给旧车估了个好价”等 |
| calzone | 意式烤饺 | Maria 后厨制作的食物，不音译成人物名 |
| The Overcompensator | 过度补偿者 | 豪华车的夸张车型名，保留炫耀和补偿心理的笑点 |
| The Blue Falcon | 蓝色猎鹰号 | Tony 为车辆提出的夸张名字 |
| The Sapphire Stallion | 蓝宝石种马号 | 与“蓝色猎鹰号”并列的夸张车辆名 |
| Holy Mary, Mother, and Joseph! | 圣母玛利亚和圣约瑟在上！ | Maria 的天主教文化感叹，保留宗教色彩，不缩成泛化的“天哪” |
| forghedaboudit | 甭提了／别放在心上 | Tony 的意大利裔纽约式口头表达，按语用自然汉化，不保留英文拼写 |

- Tony、Maria 的意大利裔美国人口吻通过短句、老派口头语、夸张和宗教文化痕迹体现；不得硬套中国地方方言，也不得写成现代网络梗。
- Tony 帮助 Tina 源于与 Luigi 的兄弟情和遗属照顾承诺；相关调侃不得误译成明确婚外情。

## `ano10.rpy` 披萨制作、双关与生育诊断

| 英文 | 当前处理 | 说明 |
|---|---|---|
| hand-tossed dough | 手抛饼底 | 披萨制作术语，不译成泛化的“手工面团” |
| toppings | 配料／铺配料 | 按名词或动作自然处理 |
| deep-dish pizza | 深盘披萨 | Maria 明确鄙视的披萨类型 |
| pizza stone | 披萨石 | `double pizza stone setup` 译“上下两块披萨石” |
| pie / pizza pie | 披萨 | 披萨店语境，不直译“馅饼” |
| cannoli / cannolis | 意式奶油甜馅卷 | 食品名称统一；`Holy cannoli` 是感叹语，须另按语用翻译 |
| protégé | 徒弟 | Tony 对 Anon 的培养定位，跨 `ano10.rpy`、`ano11.rpy`、`tin_vault.rpy` 保持一致 |
| mustache ride | 骑胡子 | 成人双关；保留 Anon 不懂含义的喜剧节奏，不提前解释成口交 |
| my boys can’t swim | 我的小蝌蚪游不动了 | Tony 对不育诊断的委婉比喻 |
| my batter’s expired | 我的面糊过期了 | 与披萨店身份相符的生育比喻 |
| my milk’s turned sour | 我的牛奶馊了 | 与上一句连续递进，不擅自改成医学说明 |
| my gun’s shooting blanks | 我的枪打的是空包弹 | 生育能力比喻；随后才直白说明精液没有精子 |

- `ano10.rpy` 中 Maria 的“奖励”先以意式奶油甜馅卷制造误导，但 `mar_cook.rpy` 的成功分支后续明确描写了 Maria 借“奶油馅点心”双关为 Anon 口交。前段保留食物误导，后段不得净化或跳过明确的性行为。
- Tony 与 Luigi 是胜似亲兄弟的黑帮旧友；`more than friends` 不得译出恋爱关系。

## `ano11.rpy` 生育选择、俄式食品与黑帮专名

| 英文 | 当前处理 | 说明 |
|---|---|---|
| adoption | 领养 | Tina 提出的家庭选择；不得误写成收养宠物或临时照顾 |
| sperm donor | 精子捐献者 | 区分匿名捐献者与夫妻认识、信任的捐献人 |
| swimmers | 小蝌蚪 | Tony 对精子的委婉说法，并承接池塘/游泳双关 |
| pregnancy stuff | 生孩子的事／备孕和生育难题 | Maria 尚未怀孕；不得误译成已经发生的孕期事项 |
| pelmeni | 俄式饺子 | Igor 提议的俄式食物 |
| borscht | 罗宋汤 | Igor 反复惦记的食物；跨文件保持一致 |
| pirozhki | 俄式馅饼 | 结合场景作可理解的食品译名，不音译 |
| little bunny | 小兔子 | Dimitri 对 Anon 的戏谑性固定称呼 |
| The Plumber | `The Plumber` | Tony 的旧黑帮绰号，属于人物专名，保持英文原状 |
| Eddie Four-Fingers / Four-Fingers | `Eddie Four-Fingers`／`Four-Fingers` | 旧黑帮关系的姓名/绰号，保持英文拼写与原文形式 |
| pair of ducks | 一对二 | 骰子/牌桌式比喻，指 Maria 一人对付两名闯入者 |
| has balls | 有种 | 本义为有胆量；Igor 随后按“蛋蛋”误解，必须保留双层笑点 |
| Get. / The fuck. / Out of my shop! | 给。／老娘。／滚出我的店！ | 保持三条 Ren’Py 台词，中文连读为“给老娘滚出我的店！” |

## `ano13.rpy` 特殊披萨、地点与调查术语

| 英文 | 当前处理 | 说明 |
|---|---|---|
| pear | 梨 | 特殊披萨配料；与后两项构成连续列举 |
| prosciutto | 意式风干火腿 | 不泛化为普通“火腿”，跨文件保持食品术语 |
| gorgonzola | 戈贡佐拉奶酪 | 蓝纹奶酪品种；不使用不稳定音译 |
| pear-prosciutto-gorgonzola pizza | 梨、意式风干火腿和戈贡佐拉奶酪披萨 | 三项配料多次重复，顺序和核心译名保持一致 |
| Beachside Apartments | 海滨公寓 | 地点专名；保留房号变量或数字 |
| calzone | 意式烤饺 | 与 `ano09.rpy` 一致；藏锉刀的越狱笑话仍保留核心食品译名 |
| serving a ten stretch upstate | 在州北部监狱服十年刑 | 黑帮口语；同时保留地点方向、监禁和刑期信息 |
| dirty Russkies | 俄国杂种 | Tony 的粗俗敌对称呼；按原文保留攻击性，不推广成中性族群称谓 |
| extra sausage on the side | 另外还加一根“香肠”吗？ | Tina 借披萨配料影射 Anon 的阴茎；用弯引号点明双关，同时保留 Anon 一时没听懂的笑点 |

- `Eddie Four-Fingers` 在本文件恢复为英文原名；不得写作“Eddie·四指”等混合形式。
- `babyface`、`dollface`、`champ` 继续分别固定为“小帅哥”“美人儿”“冠军”。
- 动态日期 `[saga.time.dow + when]`、`[saga.time.dow + when + 3]` 必须原样保留，只调整外围中文语序。
## `ano15.rpy` 自然受孕、走私情报与 Tony 双关

| 英文 | 当前处理 | 说明 |
|---|---|---|
| hydration is key | 补水最重要 | Tony 反复叮嘱的运动补水口号；`ano13.rpy` 和 `ano15.rpy` 统一 |
| capicola | 卡皮科拉火腿 | 意大利式熟食；保留 Tony 的食物比喻 |
| file（越狱工具） | 锉刀 | 藏在意式烤饺里的金属工具，不译成“文件” |
| mustache ride | 骑胡子 | 已在 `ano10.rpy` 和 `ano15.rpy` 复核；保留成人双关及 Anon 早期没听懂的笑点 |
| calzone | 意式烤饺 | `ano09.rpy`、`ano13.rpy`、`ano15.rpy` 统一核心译名 |
| Boy, boy, boy... very tall boy. | 男孩，男孩，男孩……长得高高的男孩。 | Tony 给 Maria 的尴尬暗号；保留重复节奏和拙劣掩饰感 |
| workplace seminar | 职场性骚扰培训 | Maria 针对 Tony 向员工说露骨话的惩罚式威胁；Tony 害怕的是再次参加强制培训，不是与 Maria 发生性行为 |
## `ano16.rpy` 家庭身份与黑帮式元叙事

| 英文 | 当前处理 | 说明 |
|---|---|---|
| godfather | 教父 | 指 Anon 担任 Tony 与 Maria 孩子的教父；同时承接 Tony 的黑帮背景和下一句《教父》式玩笑，不改成“干爹” |
| an offer you can't refuse | 一个你没法拒绝的提议 | 保留《教父》式固定笑点；按 Tony 口吻自然表达，不直译成僵硬公文语 |
| Not this update! | 这次更新不给！ | 第四面墙式版本结尾；必须保留“更新”的元叙事含义 |


## 卧室设备与系统交互

| 英文 | 当前处理 | 说明 |
|---|---|---|
| Consum-R | Consum-R | 商场店名，保持英文原拼写和连字符；电脑零件线索与其他购物任务统一 |
| PC | 电脑 | 普通叙述和内心独白使用自然中文，不保留界面外的英文缩写 |
| higher resolution graphics | 更高分辨率的画面 | 电脑修复后的画质升级元叙事，不译成生硬的“图形” |
| bugs（游戏故障） | BUG | 仅用于游戏程序故障语境，与昆虫含义区分 |
| cheat menu | 作弊菜单 | 手机 Wi-Fi 连续点击彩蛋；保留玩家主动寻找并最终解锁的第四面墙逻辑 |


## Maria 线固定双关、专名与成人表达

| 英文表达 | 统一处理 | 说明 |
|---|---|---|
| `champ` | 冠军 | Tony 对 Anon 的专属称呼 |
| `The Falsettos` | 《假声》 | 电视节目标题 |
| `horizontal pizzica` | “横着做披萨” | 保留性双关 |
| `primed pussy` | 水润润、正等着开干的骚屄 | 保留 Tony 的露骨起哄 |
| `tap that` | 好好肏她一顿 | 明确性行为动作 |
| `work that big cock` | 好好使唤那根大鸡巴 | Tony 的粗俗起哄 |
| `lampredotto` | 灯笼牛肚 | 意大利食物比喻 |
| `Devil's Threeway` | 恶魔三人行 | Tony 为三人性交提出的夸张招式名 |
| `The Kidney Shifter` | 移肾术 | Tony 为性交动作提出的夸张招式名 |
| `batter` | 面糊 | 造人语境下指精液，延续披萨店食物双关 |
| `little guys` | 小家伙们 | 指精子，保持 Tony 半玩笑式造人说法 |
| `cannoli` | 意式奶油甜馅卷 | 食品核心译名不变；成人双关中仍保持同一意象 |
| `au jus` | 肉汁 | Maria 在披萨店后厨使用的食物式性比喻 |
| `Yes, ma’am.` | 是，老板娘。 | Anon 的服从式回应，同时对应 Maria 的经营者身份 |
| `break` | 休息／歇会儿 | 先指工作间歇，随后成为性交邀请和事后回味的连续双关 |
| `Gimme another baby` | 再让我怀一个 | Maria 明确要求再次受孕，不直译成生硬的“再给我一个宝宝” |
| `lookin’ for trouble` | 来找刺激／找刺激 | 后期性邀约式双关，不按普通“找麻烦”处理 |
| `Wages.` | 工钱 | 披萨外送欠付报酬的菜单主题；金额变量原样保留 |
| `Baby.`（菜单主题） | 宝宝 | 指谈论宝宝，不是亲昵称呼“宝贝” |
| `kid` / `handsome` | 小子／帅哥 | 标记 Maria 与 Anon 从长辈式审视到亲密暧昧的关系变化 |
