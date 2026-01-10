// NFL Strategies - Tactics Data
// 橄榄球战术数据

const tacticsData = {
  // 战术分类
  categories: [
    { id: 'offense-formation', name: '进攻阵型', icon: '🏈' },
    { id: 'passing-routes', name: '传球路线', icon: '📍' },
    { id: 'passing-concepts', name: '传球概念', icon: '🎯' },
    { id: 'defense-coverage', name: '防守覆盖', icon: '🛡️' },
    { id: 'defense-formation', name: '防守阵型', icon: '⚔️' },
    { id: 'running-plays', name: '跑球战术', icon: '💨' }
  ],

  // 战术数据
  tactics: [
    // ========== 进攻阵型 (Offensive Formations) ==========
    {
      id: 'shotgun-formation',
      category: 'offense-formation',
      nameEn: 'Shotgun Formation',
      nameCn: '霰弹枪阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '0:45',
      description: '四分卫站在中锋后方约5码处直接接球的进攻阵型。这个阵型让四分卫有更多时间观察防守并做出决策，是现代NFL中最常见的传球阵型之一。',
      advantages: [
        '给四分卫更多时间读取防守',
        '便于快速传球和短传进攻',
        '适合传跑结合战术',
        '接球手有更多时间跑出路线'
      ],
      weaknesses: [
        '跑球威胁相对较小',
        '容易被防守识别为传球战术',
        '四分卫压力较大，需要快速决策',
        '中锋直接传球增加失误风险'
      ],
      counters: [
        '使用Blitz快速冲击四分卫',
        '采用Cover 2或Cover 3防守',
        '加强边路防守限制外接手',
        '使用假装冲击扰乱四分卫节奏'
      ],
      situations: ['长码数', '传球优势', '两分钟进攻', '得分区域'],
      difficulty: 'beginner',
      image: 'assets/images/offense/shotgun-formation.svg'
    },
    {
      id: 'i-formation',
      category: 'offense-formation',
      nameEn: 'I-Formation',
      nameCn: 'I阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '2:15',
      description: '全卫和跑卫在四分卫身后排成一条直线的经典阵型。这是NFL历史上最传统的跑球阵型之一，强调力量跑球和短码数进攻。',
      advantages: [
        '强大的跑球威胁',
        '全卫可以为跑卫开路',
        '适合短码数情况',
        '可以进行Power跑球战术'
      ],
      weaknesses: [
        '传球选择相对有限',
        '容易被防守识别意图',
        '需要强大的进攻线',
        '在长码数情况下效果不佳'
      ],
      counters: [
        '堆叠防守线对抗跑球',
        '使用8人防守盒子',
        '线卫快速填补空档',
        '预判跑球方向提前移动'
      ],
      situations: ['短码数', '跑球进攻', 'Goal Line', '建立跑球威胁'],
      difficulty: 'beginner',
      image: 'assets/images/offense/i-formation.svg'
    },
    {
      id: 'spread-offense',
      category: 'offense-formation',
      nameEn: 'Spread Offense',
      nameCn: '展开进攻阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '4:30',
      description: '将接球手分散到场地宽度,迫使防守展开的现代进攻阵型。通常使用3-5个接球手,创造一对一匹配和空间优势。',
      advantages: [
        '创造更多空间和一对一机会',
        '迫使防守展开,减少防守盒子人数',
        '利于快节奏进攻',
        '发挥速度型球员优势'
      ],
      weaknesses: [
        '对四分卫要求很高',
        '跑球保护相对较弱',
        '面对强力冲传压力大',
        '需要多个有威胁的接球手'
      ],
      counters: [
        '使用Nickel或Dime防守包',
        '区域防守覆盖多个接球点',
        '边缘冲传施加压力',
        '用快速后卫匹配接球手'
      ],
      situations: ['传球进攻', '追分情况', '利用空间', '对阵弱防守二线'],
      difficulty: 'intermediate',
      image: 'assets/images/offense/spread-offense.svg'
    },
    {
      id: 'singleback-formation',
      category: 'offense-formation',
      nameEn: 'Singleback Formation',
      nameCn: '单后卫阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '3:20',
      description: '只有一个跑卫在四分卫身后的平衡型阵型。这是NFL最常用的基础阵型之一,兼顾传球和跑球能力,给进攻组更多灵活性。',
      advantages: [
        '传跑平衡,不易被防守预判',
        '可以快速变换为多种子阵型',
        '给四分卫更多传球选择',
        '适应性强,适合多种战术'
      ],
      weaknesses: [
        '跑球威力不如双后卫阵型',
        '保护四分卫的人手相对较少',
        '面对强力冲传压力较大',
        '需要全能型跑卫'
      ],
      counters: [
        '使用Nickel防守包增加覆盖',
        '线卫灵活应对传跑',
        '观察跑卫位置预判战术',
        '混合使用冲传和覆盖'
      ],
      situations: ['标准下档', '中等码数', '保持平衡', '需要灵活性'],
      difficulty: 'beginner',
      image: 'assets/images/offense/singleback-formation.svg'
    },
    {
      id: 'pistol-formation',
      category: 'offense-formation',
      nameEn: 'Pistol Formation',
      nameCn: '手枪阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '5:45',
      description: '四分卫站在中锋后方约4码处,跑卫在QB正后方的混合阵型。结合了Under Center和Shotgun的优点,是现代NFL流行的创新阵型。',
      advantages: [
        '既能看清防守又能快速交球',
        '跑卫有向前冲刺的助跑空间',
        '适合Read Option战术',
        '欺骗性强,传跑难以预判'
      ],
      weaknesses: [
        '相对较新,部分球队不熟悉',
        '需要移动能力强的四分卫',
        '时机把握要求高',
        '在某些情况下不如传统阵型有效'
      ],
      counters: [
        '指定球员专门跟防QB',
        '快速识别Read Option关键',
        '保持防守纪律不被假动作欺骗',
        '边缘防守收紧'
      ],
      situations: ['Read Option', '短码数', '红区进攻', '移动型QB'],
      difficulty: 'intermediate',
      image: 'assets/images/offense/pistol-formation.svg'
    },
    {
      id: 'empty-backfield',
      category: 'offense-formation',
      nameEn: 'Empty Backfield',
      nameCn: '空后场阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '7:10',
      description: '后场没有跑卫,所有技术位置球员都在外接位置的极端传球阵型。这是明显的传球信号,但也带来极大的空间优势。',
      advantages: [
        '5个接球点同时出现',
        '防守盒子内人数最少',
        '强迫防守使用传球防守阵型',
        '创造大量一对一机会'
      ],
      weaknesses: [
        '完全放弃跑球威胁',
        '四分卫保护压力巨大',
        '易被Blitz攻击',
        '需要快速出球'
      ],
      counters: [
        '全力冲传攻击QB',
        '使用多人Blitz',
        '人盯人防守限制接球手',
        '给予持续压力'
      ],
      situations: ['长码数', '两分钟进攻', '必须传球', '追分情况'],
      difficulty: 'advanced',
      image: 'assets/images/offense/empty-backfield.svg'
    },
    {
      id: 'wildcat-formation',
      category: 'offense-formation',
      nameEn: 'Wildcat Formation',
      nameCn: '野猫阵型',
      videoSource: 'https://www.youtube.com/watch?v=sRaIlyv95hs',
      videoTimestamp: '8:50',
      description: '跑卫或接球手直接接中锋开球,四分卫不在场上或作为接球手的特殊阵型。这是一种欺骗性强的突然变化战术。',
      advantages: [
        '出其不意,打乱防守节奏',
        '增加跑球手的视野和选择',
        '可以执行Read Option',
        '场上多一个阻挡者或接球手'
      ],
      weaknesses: [
        '传球选择有限',
        '需要特殊球员',
        '使用过多会失去突然性',
        '容易被识破'
      ],
      counters: [
        '提前识别阵型调整防守',
        '假定是跑球加强前线',
        '保持防守纪律',
        '不被花哨战术迷惑'
      ],
      situations: ['短码数', '突然袭击', 'Goal Line', '改变节奏'],
      difficulty: 'intermediate',
      image: 'assets/images/offense/wildcat-formation.svg'
    },

    // ========== 传球路线 (Passing Routes) ==========
    {
      id: 'go-route',
      category: 'passing-routes',
      nameEn: 'Go Route (9 Route)',
      nameCn: '直线深传路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '1:20',
      description: '接球手直线向前冲刺的深传路线,也称为Fly Route或Streak。这是最简单但也最具威胁的路线之一,目标是超越防守获得深传接球。',
      advantages: [
        '威胁防守深度,拉开防守阵型',
        '利用接球手速度优势',
        '可以获得大码数推进',
        '路线简单易执行'
      ],
      weaknesses: [
        '需要四分卫有强传球臂力',
        '进攻线需要提供足够保护时间',
        '容易被防守深度覆盖',
        '完成率相对较低'
      ],
      counters: [
        '使用Cover 2或Cover 3防守深度',
        '安全卫提供顶部覆盖',
        '避免给予接球手内线位置',
        '冲传迫使四分卫提前出球'
      ],
      situations: ['长码数', '对阵慢速防守后卫', '拉开防守', '得分机会'],
      difficulty: 'beginner',
      image: 'assets/images/routes/go-route.svg'
    },
    {
      id: 'slant-route',
      category: 'passing-routes',
      nameEn: 'Slant Route',
      nameCn: '斜插路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '3:45',
      description: '接球手向前冲刺几步后以45度角斜向内切入中路的快速路线。这是对抗区域防守和人盯人防守的有效武器。',
      advantages: [
        '出球快速,减少四分卫压力',
        '利用中路空档',
        '接球后有跑动空间(YAC)',
        '对抗紧逼防守有效'
      ],
      weaknesses: [
        '容易被中路线卫击球',
        '需要精准时机',
        '可能被抄截',
        '在拥挤区域有受伤风险'
      ],
      counters: [
        '线卫保护中路区域',
        '角卫紧随并干扰路线',
        '安全卫提供中路支援',
        '预判路线准备击球'
      ],
      situations: ['短码数', '对抗Blitz', '快速进攻', '红区进攻'],
      difficulty: 'beginner',
      image: 'assets/images/routes/slant-route.svg'
    },
    {
      id: 'out-route',
      category: 'passing-routes',
      nameEn: 'Out Route (7 Route)',
      nameCn: '外切路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '5:20',
      description: '接球手向前跑10-15码后90度角急转向边线的路线。这是对抗区域防守的经典路线,常用于需要稳定推进码数的情况。',
      advantages: [
        '到达边线后可停表',
        '利用边线作为额外防守者',
        '适合精准传球',
        '接球后安全性高'
      ],
      weaknesses: [
        '转身时容易被角卫拦截',
        '需要QB精准传球',
        '容易被识破',
        '接球后难以获得额外码数'
      ],
      counters: [
        '角卫紧跟并卡位',
        '在转身点准备拦截',
        '边线卫预读路线',
        '用身体对抗干扰'
      ],
      situations: ['两分钟进攻', '需要停表', '边线进攻', '中等码数'],
      difficulty: 'beginner',
      image: 'assets/images/routes/out-route.svg'
    },
    {
      id: 'post-route',
      category: 'passing-routes',
      nameEn: 'Post Route (8 Route)',
      nameCn: '柱子路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '6:45',
      description: '接球手向前跑12-15码后向中路球门柱方向斜切的深传路线。这是攻击Cover 2防守安全卫之间空档的最佳路线。',
      advantages: [
        '攻击防守深度薄弱点',
        '大码数推进潜力',
        '对抗Cover 2极为有效',
        '接球后还有跑动空间'
      ],
      weaknesses: [
        '需要时间发展',
        '容易被Free Safety拦截',
        '对QB臂力要求高',
        '在拥挤中路风险较大'
      ],
      counters: [
        'Free Safety及时补位',
        '角卫深度覆盖跟随',
        '使用Cover 3或Cover 1',
        '提前识别路线组合'
      ],
      situations: ['对抗Cover 2', '长码数', '得分机会', '深度进攻'],
      difficulty: 'intermediate',
      image: 'assets/images/routes/post-route.svg'
    },
    {
      id: 'corner-route',
      category: 'passing-routes',
      nameEn: 'Corner Route (7/9 Route)',
      nameCn: '角落路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '8:10',
      description: '接球手先做直线深传假动作,然后突然45度角转向边线角落的路线。这是最难防守的路线之一,结合了速度和技巧。',
      advantages: [
        '利用角卫背对转身的瞬间',
        '攻击端区角落',
        '大码数或达阵机会',
        '假动作欺骗性强'
      ],
      weaknesses: [
        '时机把握极其重要',
        '需要接球手精准跑位',
        '容易被安全卫补防',
        '路线复杂容易出错'
      ],
      counters: [
        '角卫保持内线位置',
        '安全卫提供顶部帮助',
        '不被假动作欺骗',
        '使用Cover 2或Cover 4'
      ],
      situations: ['红区进攻', '端区角落', '对抗人盯人', '大码数需求'],
      difficulty: 'advanced',
      image: 'assets/images/routes/corner-route.svg'
    },
    {
      id: 'curl-route',
      category: 'passing-routes',
      nameEn: 'Curl Route (5 Route)',
      nameCn: '回钩路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '4:15',
      description: '接球手向前冲刺10-12码后转身面向四分卫的路线。这是对抗区域防守的稳定选择,提供安全的传球目标。',
      advantages: [
        '高完成率路线',
        '接球手面对QB易接球',
        '适合第三档转换',
        '对抗各种防守都有效'
      ],
      weaknesses: [
        '接球后面对防守',
        'YAC机会有限',
        '容易被线卫击球',
        '在拥挤区域接球困难'
      ],
      counters: [
        '线卫紧密覆盖该区域',
        '接球瞬间施加压力',
        '安全卫快速上前',
        '限制接球后推进'
      ],
      situations: ['第三档转换', '中等码数', '需要稳定推进', '对抗区域防守'],
      difficulty: 'beginner',
      image: 'assets/images/routes/curl-route.svg'
    },
    {
      id: 'drag-route',
      category: 'passing-routes',
      nameEn: 'Drag Route (Cross Route)',
      nameCn: '横拖路线',
      videoSource: 'https://www.youtube.com/watch?v=Ebn6c1jNZbo',
      videoTimestamp: '9:30',
      description: '接球手从一侧横向穿越球场到另一侧的浅层路线。常用于TE或Slot接球手,是对抗区域防守的有效武器。',
      advantages: [
        '横向移动创造空档',
        '接球后有跑动空间',
        '对抗区域防守有效',
        '可与其他路线配合'
      ],
      weaknesses: [
        '需要时间穿越球场',
        '容易被线卫击球',
        '在拥挤中路风险高',
        'QB需要耐心等待'
      ],
      counters: [
        '线卫横向追踪',
        '保持中路密集',
        '安全卫提供支援',
        '用身体对抗干扰'
      ],
      situations: ['对抗区域防守', '需要YAC', '配合其他路线', 'RPO战术'],
      difficulty: 'intermediate',
      image: 'assets/images/routes/drag-route.svg'
    },

    // ========== 防守覆盖 (Defensive Coverage) ==========
    {
      id: 'cover-2',
      category: 'defense-coverage',
      nameEn: 'Cover 2',
      nameCn: 'Cover 2防守',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '0:30',
      description: '两个安全卫各负责半边深度区域,角卫和线卫覆盖浅层区域的基础区域防守。是NFL中最常见的防守覆盖之一。',
      advantages: [
        '有效防守深传和边路进攻',
        '保护边线和深度',
        '便于支援跑球防守',
        '相对容易沟通和执行'
      ],
      weaknesses: [
        '中路短传区域容易被攻击',
        '对线卫覆盖能力要求高',
        '角卫和安全卫之间容易出现空档',
        '面对四接球手阵型压力大'
      ],
      counters: [
        '攻击中路15-20码区域',
        '使用Seam路线攻击安全卫交界',
        '短传后获得跑动码数(YAC)',
        '利用TE攻击线卫覆盖'
      ],
      situations: ['防守长传', '边线情况', '对抗强臂四分卫', '普通下档距离'],
      difficulty: 'beginner',
      image: 'assets/images/defense/cover-2.svg'
    },
    {
      id: 'cover-3',
      category: 'defense-coverage',
      nameEn: 'Cover 3',
      nameCn: 'Cover 3防守',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '2:15',
      description: '三个深度防守者各负责三分之一场地深度,四个球员覆盖浅层的区域防守。这是对抗跑球和短传的平衡型防守。',
      advantages: [
        '对抗跑球更有效',
        '保护深度三个区域',
        '角卫可支援跑球防守',
        '适合对抗平衡型进攻'
      ],
      weaknesses: [
        '边线深度容易被攻击',
        '中路10-15码区域薄弱',
        '对抗四接球手阵型困难',
        '需要角卫能力全面'
      ],
      counters: [
        '攻击边线深度角落',
        '使用4接球手拉开防守',
        '短传后获取YAC',
        '利用TE攻击中路'
      ],
      situations: ['对抗跑球进攻', '标准防守', '防守平衡', '第一第二档'],
      difficulty: 'beginner',
      image: 'assets/images/defense/cover-3.svg'
    },
    {
      id: 'cover-1',
      category: 'defense-coverage',
      nameEn: 'Cover 1 (Man Free)',
      nameCn: 'Cover 1人盯人',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '4:30',
      description: '一个Free Safety提供深度保护,其他防守后卫人盯人的防守方案。这是最激进的覆盖方式,常配合Blitz使用。',
      advantages: [
        '可以派更多人冲传',
        '人盯人限制接球手',
        '防守意图明确',
        '对抗精英接球手有效'
      ],
      weaknesses: [
        '对防守后卫要求极高',
        '一旦被甩开后果严重',
        '容易被Pick战术攻击',
        '深度只有一人保护'
      ],
      counters: [
        '利用Pick/Rub路线',
        '攻击弱侧角卫',
        '使用速度快的接球手',
        '快速出球避免冲传'
      ],
      situations: ['需要冲传', '第三档长码数', '对抗弱QB', '关键时刻'],
      difficulty: 'advanced',
      image: 'assets/images/defense/cover-1.svg'
    },
    {
      id: 'cover-0',
      category: 'defense-coverage',
      nameEn: 'Cover 0 (Zero Blitz)',
      nameCn: '全场人盯人',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '6:00',
      description: '没有深度帮助的全场人盯人防守,所有人不参与盯人的球员都参与冲传。这是最激进的防守方案,目标是在传球前擒杀四分卫。',
      advantages: [
        '最大化冲传压力',
        '打乱进攻节奏',
        '强迫QB仓促决策',
        '可能造成Sack或失误'
      ],
      weaknesses: [
        '没有深度保护',
        '一旦被甩开必定失分',
        '对位不佳会被虐',
        '风险极大'
      ],
      counters: [
        '快速短传Hot Route',
        '利用RB承接短传',
        'Screen战术',
        '保持冷静快速决策'
      ],
      situations: ['第三档长码数', '两分钟防守', '必须得手', '对抗弱O-Line'],
      difficulty: 'advanced',
      image: 'assets/images/defense/cover-0.svg'
    },
    {
      id: 'cover-4',
      category: 'defense-coverage',
      nameEn: 'Cover 4 (Quarters)',
      nameCn: 'Cover 4四分防守',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '7:45',
      description: '四个深度防守者各守四分之一场地的防守覆盖。两个角卫和两个安全卫共同保护深度,是防守深传的专门方案。',
      advantages: [
        '深度保护最严密',
        '防守深传效果最佳',
        '边线和中路都有覆盖',
        '适合对抗强臂QB'
      ],
      weaknesses: [
        '浅层防守人手不足',
        '中短传容易完成',
        'YAC机会多',
        '对抗跑球较弱'
      ],
      counters: [
        '使用短传控制节奏',
        '跑球进攻',
        '获取YAC积累码数',
        '耐心推进不冒险'
      ],
      situations: ['防守深传', 'Hail Mary', '长码数情况', '比赛末尾领先'],
      difficulty: 'intermediate',
      image: 'assets/images/defense/cover-4.svg'
    },
    {
      id: 'cover-6',
      category: 'defense-coverage',
      nameEn: 'Cover 6 (Quarter-Quarter-Half)',
      nameCn: 'Cover 6混合防守',
      videoSource: 'https://www.youtube.com/watch?v=ROliJ27Br9A',
      videoTimestamp: '9:10',
      description: '一侧使用Cover 4(两个四分之一),另一侧使用Cover 2(一个二分之一)的混合防守方案。针对进攻强弱侧的不对称防守。',
      advantages: [
        '针对性强',
        '保护重点接球手一侧',
        '灵活应对不对称阵型',
        '欺骗性好'
      ],
      weaknesses: [
        '复杂,需要良好沟通',
        '容易出现覆盖失误',
        '弱侧可能被攻击',
        '需要聪明的防守后卫'
      ],
      counters: [
        '识别防守调整进攻方向',
        '攻击弱侧',
        '利用阵型变化',
        '快速改变传球目标'
      ],
      situations: ['对抗精英接球手', '不对称阵型', '特殊情况', '混淆进攻'],
      difficulty: 'advanced',
      image: 'assets/images/defense/cover-6.svg'
    },

    // ========== 跑球战术 (Running Plays) ==========
    {
      id: 'inside-zone',
      category: 'running-plays',
      nameEn: 'Inside Zone',
      nameCn: '内侧区域跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '1:15',
      description: '进攻线横向移动并创造跑球通道的区域跑球战术。跑卫读取防守并选择最佳缝隙,是现代NFL的主流跑球战术。',
      advantages: [
        '灵活性高,跑卫可选择跑球路线',
        '不依赖单个阻挡员',
        '可以配合各种阵型',
        '有效对抗多种防守阵型'
      ],
      weaknesses: [
        '需要进攻线整体配合',
        '对跑卫视野要求高',
        '面对快速填补的防守效果有限',
        '需要时间发展跑球通道'
      ],
      counters: [
        '防守线快速穿透',
        '线卫迅速填补空档',
        '使用Slant技术破坏阻挡',
        '预判跑球方向提前移位'
      ],
      situations: ['建立跑球进攻', '中等码数', '控制比赛节奏', '消耗时间'],
      difficulty: 'intermediate',
      image: 'assets/images/running/inside-zone.svg'
    },
    {
      id: 'outside-zone',
      category: 'running-plays',
      nameEn: 'Outside Zone (Stretch)',
      nameCn: '外侧区域跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '3:30',
      description: '进攻线横向移动向外拉伸防守,跑卫寻找外侧跑球通道的区域跑球战术。目标是到达防守外侧利用速度优势。',
      advantages: [
        '拉伸防守横向覆盖',
        '利用速度型跑卫优势',
        '创造边线突破机会',
        '如防守追得太快可内切'
      ],
      weaknesses: [
        '容易被边缘防守限制',
        '需要进攻线机动性',
        '在边线易被逼出界',
        '对跑卫速度要求高'
      ],
      counters: [
        '边缘防守设置牢固',
        '外侧线卫快速追击',
        '不过度追击保持内线',
        '用速度与跑卫竞争'
      ],
      situations: ['利用速度优势', '拉开防守', '对抗慢速防守', '需要大码数'],
      difficulty: 'intermediate',
      image: 'assets/images/running/outside-zone.svg'
    },
    {
      id: 'power-run',
      category: 'running-plays',
      nameEn: 'Power Run (Gap Scheme)',
      nameCn: '强力跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '5:15',
      description: '进攻线使用Gap阻挡方案,全卫或H-Back拉动lead block为跑卫开路的力量型跑球战术。这是短码数情况的经典选择。',
      advantages: [
        '强大的力量冲击',
        '短码数极为有效',
        '有额外lead blocker',
        '明确的跑球缝隙'
      ],
      weaknesses: [
        '缺乏欺骗性',
        '速度较慢',
        '需要优秀的O-Line',
        '防守易识别'
      ],
      counters: [
        '堆叠防守线',
        '填补预定缝隙',
        '使用力量对抗力量',
        '线卫快速反应'
      ],
      situations: ['短码数', 'Goal Line', '第四档冲锋', '建立跑球威胁'],
      difficulty: 'beginner',
      image: 'assets/images/running/power-run.svg'
    },
    {
      id: 'counter-run',
      category: 'running-plays',
      nameEn: 'Counter Run',
      nameCn: '反向跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '6:45',
      description: '通过假动作和拉动阻挡,让跑卫反向跑向防守追击相反方向的欺骗性跑球战术。对抗过度追击的防守非常有效。',
      advantages: [
        '欺骗性极强',
        '利用防守过度追击',
        '拉动阻挡创造优势',
        '大码数潜力'
      ],
      weaknesses: [
        '需要时间发展',
        '阻挡配合要求高',
        '一旦失败损失码数大',
        '对抗纪律性强的防守效果有限'
      ],
      counters: [
        '保持防守纪律',
        '不过度追击',
        '识别拉动阻挡',
        '后侧防守保持警惕'
      ],
      situations: ['对抗快速防守', '需要大码数', '打乱防守节奏', '第二层进攻'],
      difficulty: 'advanced',
      image: 'assets/images/running/counter-run.svg'
    },
    {
      id: 'draw-play',
      category: 'running-plays',
      nameEn: 'Draw Play',
      nameCn: 'Draw跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '8:00',
      description: '假装传球保护让防守冲传深入,然后突然交球给跑卫的延迟跑球战术。这是对抗激进冲传的有效武器。',
      advantages: [
        '对抗激进冲传',
        '欺骗性强',
        '让冲传者失位',
        '常能获得大码数'
      ],
      weaknesses: [
        '时机把握困难',
        '如被识破损失大',
        '需要O-Line演技',
        '在长码数情况风险高'
      ],
      counters: [
        '识别进攻线的"放人"',
        '线卫保持警惕',
        '不盲目深入冲传',
        '保持跑球防守纪律'
      ],
      situations: ['对抗Blitz', '长码数', '防守过度冲传', '改变节奏'],
      difficulty: 'intermediate',
      image: 'assets/images/running/draw-play.svg'
    },
    {
      id: 'toss-sweep',
      category: 'running-plays',
      nameEn: 'Toss Sweep (Pitch)',
      nameCn: '外抛扫荡跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '9:20',
      description: 'QB向侧面抛球给跑卫,跑卫接球后向外侧扫荡的快速跑球战术。利用速度和外侧空间获取码数。',
      advantages: [
        '快速到达外侧',
        '利用速度优势',
        '多个lead blockers',
        '大码数突破可能性'
      ],
      weaknesses: [
        '易失误(抛球)',
        '容易损失码数',
        '需要优秀外侧阻挡',
        '对抗快速防守效果有限'
      ],
      counters: [
        '外侧防守快速封堵',
        '迫使跑卫向内',
        '不被外侧拉动牵制',
        '用速度竞争'
      ],
      situations: ['利用速度', '攻击防守弱侧', '需要改变跑球点', '对抗慢速防守'],
      difficulty: 'intermediate',
      image: 'assets/images/running/toss-sweep.svg'
    },
    // ========== 以下为CSV新增战术 (需添加中文翻译) ==========

    // ========== 新增进攻阵型 (Additional Offensive Formations) ==========
  {
    id: 't-formation',
    category: 'offense-formation',
    nameEn: 'T Formation',
    nameCn: 'T字阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '四分卫在中锋正后方,三个跑卫在QB身后排成T字形的经典阵型。这是NFL早期最具革命性的阵型之一,让四分卫有多个交球选择。',
    advantages: ['QB有4个即时选择(交球、侧抛、自己持球)', '将决策权集中在一个球员手中', '多样化的跑球选择', '欺骗性强'],
    weaknesses: ['在现代标准下过于古老和可预测', '接球手选择有限', '传球威胁较小', '容易被现代防守识破'],
    counters: ['堆叠防守线对抗跑球', '预判四分卫交球目标', '限制外围空间', '使用快速线卫填补'],
    situations: ['历史参考', '短码数', '建立跑球进攻', '多样化跑球战术'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/t-formation.svg'
  },
  {
    id: 'single-back-ace',
    category: 'offense-formation',
    nameEn: 'Single Back (Ace)',
    nameCn: '单后卫ACE阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '一个跑卫在QB后方5码处,通常配有一个槽位接球手的平衡型阵型。这是现代NFL最常用的基础阵型之一,完美融合传跑威胁。',
    advantages: ['传跑完美平衡', '槽位接球手对线卫形成错位优势', '适应性强', '现代NFL最常见阵型'],
    weaknesses: ['如果额外接球手出场,传球保护人手较少', '防守盒子相对较轻', '需要全能型跑卫', '槽位接球手受伤影响较大'],
    counters: ['Nickel防守包应对', '线卫紧盯槽位接球手', '混合防守应对传跑', '观察跑卫位置预判'],
    situations: ['标准下档', '任何码数情况', '现代进攻基础', '传跑平衡'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/single-back-ace.svg'
  },
  {
    id: 'pro-set',
    category: 'offense-formation',
    nameEn: 'Pro Set',
    nameCn: '职业套装阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '两个跑卫并排站在四分卫身后的经典阵型。这是NFL历史上的标志性阵型,以其极强的欺骗性和多样化的跑球选择而闻名。',
    advantages: ['极强的欺骗性', '任一跑卫都可以冲球、扫荡或接球', '双跑卫威胁', '多种战术变化'],
    weaknesses: ['对抗现代6-7个防守后卫阵型效果不佳', '通常只有2个接球手', '传球选择有限', '在长码数情况下劣势明显'],
    counters: ['使用Nickel或Dime防守包', '增加防守后卫覆盖', '不被跑球假动作欺骗', '强化传球防守'],
    situations: ['短码数', '近距离进攻', '建立跑球威胁', '历史战术参考'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/pro-set.svg'
  },
  {
    id: 'shotgun',
    category: 'offense-formation',
    nameEn: 'Shotgun',
    nameCn: '霰弹枪阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '四分卫站在中锋后方5-7码处直接接球的现代进攻阵型。QB一开始就处于传球姿势,有更好的视野和更多时间做决策。现代某些球队使用率超过80%。',
    advantages: ['QB一开始就在传球位置', '更好的场地视野', '更多时间传球', '便于快速传球进攻'],
    weaknesses: ['历史上跑球较困难', '跑卫起始位置太靠后难以建立冲势', '中锋直接传球增加失误风险', '跑球威胁相对较小'],
    counters: ['使用Blitz快速冲击四分卫', '采用Cover 2或Cover 3防守', '加强边路防守', '预判为传球战术'],
    situations: ['传球优势', '长码数', '两分钟进攻', '现代快节奏进攻'],
    difficulty: 'beginner',
    image: 'assets/images/offense-formation/shotgun.svg'
  },
  {
    id: 'pistol',
    category: 'offense-formation',
    nameEn: 'Pistol',
    nameCn: '手枪阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '四分卫在中锋后方3-4码,跑卫直接在QB正后方的混合阵型。结合了霰弹枪阵型的视野优势和I阵型的下坡式跑球威力,特别适合Zone Read战术。',
    advantages: ['结合霰弹枪视野和I阵型跑球优势', '更适合Zone Read战术', '跑卫有向前冲刺空间', '传跑欺骗性强'],
    weaknesses: ['需要移动能力强的四分卫才能发挥最大效果', '对QB要求较高', '部分传统球队不熟悉', '执行难度相对较高'],
    counters: ['指定球员专门跟防QB', '识别Zone Read关键', '保持防守纪律', '边缘防守收紧'],
    situations: ['Zone Read战术', '移动型QB', '短码数', '红区进攻'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/pistol.svg'
  },
  {
    id: 'spread',
    category: 'offense-formation',
    nameEn: 'Spread',
    nameCn: '展开阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '4个外接手加1个跑卫的极端传球阵型。强迫防守覆盖整个场地宽度,为跑球创造轻防守盒子,也为传球创造大量空间和错位机会。',
    advantages: ['强迫防守覆盖整个场地宽度', '为跑球创造轻防守盒子', '多个传球目标', '创造一对一机会'],
    weaknesses: ['没有紧端锋帮助阻挡,传球保护较弱', '面对强力冲传压力大', '需要4个有威胁的接球手', '跑球保护相对薄弱'],
    counters: ['使用Nickel或Dime防守包', '边缘冲传施加压力', '区域防守覆盖', '快速冲传攻击QB'],
    situations: ['第三档长码数', 'NFL长码数情况', '传球进攻', '追分情况'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/spread.svg'
  },
  {
    id: 'wildcat',
    category: 'offense-formation',
    nameEn: 'Wildcat',
    nameCn: '野猫阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '中锋直接开球给跑卫,没有四分卫参与的特殊阵型。消除中间环节,让一个跑卫获得10个阻挡者的支持,2008年迈阿密海豚队让这个阵型重新流行。',
    advantages: ['消除四分卫中间环节', '10个阻挡者支持1个跑卫', '出其不意打乱防守', '额外阻挡优势'],
    weaknesses: ['可预测性强', '大多数跑卫传球不准确', '防守会堆叠盒子', '传球威胁有限'],
    counters: ['堆叠防守盒子', '假定是跑球加强前线', '不被花哨战术迷惑', '保持防守纪律'],
    situations: ['短码数', '突然袭击', '改变节奏', 'Goal Line'],
    difficulty: 'advanced',
    image: 'assets/images/offense-formation/wildcat.svg'
  },
  {
    id: 'jumbo-goal-line',
    category: 'offense-formation',
    nameEn: 'Jumbo (Goal Line)',
    nameCn: '重型球门线阵型',
    videoSource: 'https://www.youtube.com/watch?v=source3',
    videoTimestamp: '0:00',
    description: '最重的进攻阵型,使用3个紧端锋、2个跑卫、0个外接手,甚至包括进攻线锋充当紧端锋。纯粹的蛮力阵型,用于极短距离推进。',
    advantages: ['纯粹的蛮力冲击', '在线上人数优势压制防守', '短距离推进极为有效', '最大化阻挡力量'],
    weaknesses: ['几乎没有传球威胁', '防守可以投入10人在盒子里', '完全可预测', '被识破后难以得手'],
    counters: ['投入10人防守盒子', '全力堆叠防守线', '对抗力量用力量', '预判跑球方向'],
    situations: ['需要1码推进', 'Goal Line', '第四档短距离', '极短码数'],
    difficulty: 'intermediate',
    image: 'assets/images/offense-formation/jumbo-goal-line.svg'
  },
    // ========== 新增防守阵型 (Additional Defensive Formations) ==========
  {
    id: '6-2-formation',
    category: 'defense-formation',
    nameEn: '6-2 Formation',
    nameCn: '6-2防守阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '6个防守线锋、2个线卫、3个防守后卫的极端防跑阵型。堵住每一个跑球缝隙(A、B、C缝),是最强的防跑阵型,但传球防守很弱。',
    advantages: ['极端的防跑能力', '堵住所有跑球缝隙(A、B、C缝)', '线上人数优势', '短距离防守极强'],
    weaknesses: ['传球覆盖噩梦', '3个后卫对抗4-5个接球手', '角卫被孤立在岛上', '容易被传球攻击'],
    counters: ['使用传球进攻', '4-5个接球手阵型', '快速短传', '攻击孤立的角卫'],
    situations: ['Goal Line防守', '第三/四档1码', '极短距离防守', '必须防跑'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/6-2-formation.svg'
  },
  {
    id: '5-3-formation',
    category: 'defense-formation',
    nameEn: '5-3 Formation',
    nameCn: '5-3防守阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '5个防守线锋、3个线卫、3个防守后卫的平衡阵型。提供坚实的防跑能力,同时比6-2有稍好的传球覆盖,中路线卫可以覆盖紧端锋。',
    advantages: ['坚实的防跑能力', '比6-2有更好的传球覆盖', '中路线卫可以覆盖紧端锋', '多功能防守'],
    weaknesses: ['如果进攻有4-5个接球手会形成错位', '线卫被迫覆盖快速接球手', '传球防守仍然薄弱', '容易被展开阵型攻击'],
    counters: ['使用4-5个接球手', '展开进攻', '快速传球', '利用速度优势'],
    situations: ['Goal Line防守包', '短码数防守', '偏重防跑', '平衡防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/5-3-formation.svg'
  },
  {
    id: '5-2-eagle',
    category: 'defense-formation',
    nameEn: '5-2 Eagle',
    nameCn: '5-2老鹰阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '5个防守线锋、2个线卫、4个防守后卫的经典防守阵型。由1950年代费城老鹰队推广,在预期跑球的同时提供比5-3更好的传球覆盖。',
    advantages: ['比5-3有更好的传球覆盖', '仍然预期跑球进攻', '4个防守后卫提供覆盖', '历史经典阵型'],
    weaknesses: ['防守线锋专注防跑而非冲传', 'QB有更多时间传球', '冲传压力不足', '线卫覆盖压力大'],
    counters: ['利用QB更多时间', '深传进攻', '保护好四分卫', '耐心发展传球路线'],
    situations: ['预期跑球但需要传球覆盖', '平衡防守', '历史战术参考', '标准下档'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/5-2-eagle.svg'
  },
  {
    id: '4-4-formation',
    category: 'defense-formation',
    nameEn: '4-4 Formation',
    nameCn: '4-4防守阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '4个防守线锋、4个线卫、3个防守后卫的8人前线阵型。有效阻止扫荡跑球和移动型四分卫,对抗RPO战术效果显著,控制每一个缝隙。',
    advantages: ['阻止扫荡跑球和移动型QB', '对抗RPO有效', '控制每一个缝隙', '8人前线强大'],
    weaknesses: ['只有3个后卫覆盖4-5个接球手', '传球覆盖薄弱', '容易被展开阵型攻击', '深度保护不足'],
    counters: ['展开阵型4-5个接球手', '快速传球进攻', '攻击深度', '利用场地宽度'],
    situations: ['对抗移动型QB', '防守RPO战术', '对抗跑球进攻', '短码数防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/4-4-formation.svg'
  },
  {
    id: '3-4-formation',
    category: 'defense-formation',
    nameEn: '3-4 Formation',
    nameCn: '3-4防守阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '3个防守线锋、4个线卫的灵活防守阵型,鼻锋(Nose Tackle)占据中锋。线卫可以冲传或后撤覆盖,提供多样化角度,是心理战的利器。',
    advantages: ['心理战优势', '线卫可以冲传或后撤', '多样化的冲传角度', '战术欺骗性强'],
    weaknesses: ['需要统治级鼻锋和全能型线卫', '对球员要求极高', '需要特殊球员配置', '执行难度大'],
    counters: ['识别线卫意图', '快速出球', '攻击线卫覆盖弱点', '利用跑球测试'],
    situations: ['多样化防守', '混淆进攻', '需要灵活性', '标准防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/3-4-formation.svg'
  },
  {
    id: '4-3-formation',
    category: 'defense-formation',
    nameEn: '4-3 Formation',
    nameCn: '4-3防守阵型',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '4个防守线锋、3个线卫、4个防守后卫的基础防守阵型。4个线锋提供持续的冲传压力,是传跑平衡的经典防守配置。',
    advantages: ['4个线锋提供持续冲传压力', '传跑平衡防守', '基础防守配置', '执行相对简单'],
    weaknesses: ['对抗11人员配置(3外接手)较弱', '线卫必须覆盖槽位接球手', '面对展开阵型压力大', '槽位覆盖是弱点'],
    counters: ['使用11人员配置', '3外接手阵型', '攻击线卫覆盖', '槽位接球手制造错位'],
    situations: ['基础防守', '标准下档', '传跑平衡', '通用防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/4-3-formation.svg'
  },
  {
    id: '46-bear',
    category: 'defense-formation',
    nameEn: '46 Bear',
    nameCn: '46熊式防守',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '5个防守线锋、3个线卫、1个安全卫、2个角卫的激进防守阵型。3个线锋压制中锋和护锋,8人拥挤在线上,立即从中路施压。由1985年芝加哥熊队发扬光大。',
    advantages: ['立即从中路施压', '8人拥挤在线上', '阻止缓慢发展的战术', '极强的前线压力'],
    weaknesses: ['容易被现代快速传球攻击(泡泡屏传)', '只有3个深度防守者', '深度覆盖薄弱', '快速传球是克星'],
    counters: ['快速传球和泡泡屏传', '展开阵型', '攻击深度', '利用边线空间'],
    situations: ['激进防守', '破坏进攻节奏', '短码数防守', '历史经典战术'],
    difficulty: 'advanced',
    image: 'assets/images/defense-formation/46-bear.svg'
  },
  {
    id: 'nickel-formation',
    category: 'defense-formation',
    nameEn: 'Nickel Formation',
    nameCn: '镍币防守(5后卫)',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '4个防守线锋、2个线卫、5个防守后卫的现代基础防守阵型。专门覆盖槽位接球手,更好匹配11人员配置。在65%的NFL战术中被使用。',
    advantages: ['专门覆盖槽位接球手', '更好匹配11人员配置', '现代NFL最常用防守', '传球覆盖强'],
    weaknesses: ['前线较轻', '跑卫更容易突破到二线', '镍币角卫体型较小擒抱能力弱', '防跑能力下降'],
    counters: ['加强跑球进攻', '攻击较轻的前线', '利用跑卫力量优势', '目标是镍币角卫'],
    situations: ['65%的NFL战术', '标准防守', '对抗3外接手', '现代基础防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/nickel-formation.svg'
  },
  {
    id: 'dime-formation',
    category: 'defense-formation',
    nameEn: 'Dime Formation',
    nameCn: '一角硬币防守(6后卫)',
    videoSource: 'https://www.youtube.com/watch?v=source2',
    videoTimestamp: '0:00',
    description: '4个防守线锋、1个线卫、6个防守后卫的极端传球防守阵型。通常使用2个额外安全卫,提供终极传球保护,覆盖每一个接球手。',
    advantages: ['终极传球保护', '覆盖每一个接球手', '第三档长码数/两分钟进攻安全', '深度覆盖最强'],
    weaknesses: ['由于线附近防守者较少,防跑能力很弱', '容易被跑球攻击', '前线压力小', '跑球防守噩梦'],
    counters: ['跑球进攻', '利用前线薄弱', '短传后跑动', '控制节奏'],
    situations: ['第三档长码数', '两分钟进攻防守', '季后赛传球局面', '必须防传球'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-formation/dime-formation.svg'
  },
    // ========== 新增防守覆盖 (Additional Coverage) ==========
{
    id: 'cover-zero',
    category: 'defense-coverage',
    nameEn: 'Cover Zero',
    nameCn: 'Cover 0全场人盯人',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '没有深度安全卫,每个防守球员要么人盯人覆盖要么冲击四分卫的最激进防守方案。目标是在传球前擒杀QB或强迫其仓促决策。',
    advantages: ['对QB造成毁灭性压力', '强迫瞬间决策', '关键第三档长码数极佳', '可能造成Sack或失误'],
    weaknesses: ['没有深度帮助', '一次漏人就是达阵', '容易被快速斜插/淡出路线攻击', '风险极大'],
    counters: ['快速短传Hot Route', '斜插和淡出路线', '保持冷静快速出球', 'Screen战术'],
    situations: ['关键第三档长码数', '必须得手', '赌博式防守', '对抗弱QB'],
    difficulty: 'advanced',
    image: 'assets/images/defense-coverage/cover-zero.svg'
  },
  {
    id: 'cover-one',
    category: 'defense-coverage',
    nameEn: 'Cover One',
    nameCn: 'Cover 1人盯人',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '一个安全卫巡逻深度中路,其他所有防守球员紧密人盯人覆盖的防守方案。关闭快速短传,让传球窗口极小。',
    advantages: ['关闭快速短传', '紧密覆盖让传球窗口极小', '限制接球手自由', '适合精英角卫'],
    weaknesses: ['只有一个安全卫防止达阵', '快速接球手形成错位', '一旦被甩开后果严重', '对角卫要求极高'],
    counters: ['利用速度优势制造错位', '攻击弱侧角卫', '快速接球手对慢速线卫', 'Pick路线'],
    situations: ['第二和第三档', '精英角卫阵容', '人盯人优势', '标准防守'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/cover-one.svg'
  },
  {
    id: 'cover-one-robber',
    category: 'defense-coverage',
    nameEn: 'Cover One Robber',
    nameCn: 'Cover 1抢断式',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '类似Cover 1,但一个安全卫或线卫潜伏在离锋线5-10码处伺机抢断中路路线的变体防守方案。',
    advantages: ['诱使QB传斜插和横穿路线从而轻松抄截', '中路区域有埋伏者', '适合对抗快传进攻', '制造失误机会'],
    weaknesses: ['深度防守球员更少', '长传在覆盖身后有更多空间', '依赖抢断者判断', '深度支援减弱'],
    counters: ['避开中路区域', '攻击边路深传', '识别潜伏球员', '利用深度覆盖漏洞'],
    situations: ['对抗第二档短码数快传进攻', '有精英抢断型安全卫', '预判对手传中路', '制造失误'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/cover-one-robber.svg'
  },
  {
    id: 'cover-two-zone',
    category: 'defense-coverage',
    nameEn: 'Cover Two Zone',
    nameCn: 'Cover 2区域防守',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '两个安全卫分守深度区域(15码深),五个防守球员防守浅层区域的经典区域防守方案。',
    advantages: ['群防短传', '安全卫防止深度边线传球', '弯曲但不破裂防守理念', '适合对抗传球进攻'],
    weaknesses: ['深度中路(接缝区)易受攻击', '对抗跑动防守较弱', '中路区域有漏洞', '依赖快速协防'],
    counters: ['攻击深度中路接缝', '近端锋中路垂直路线', '跑动进攻', '利用中路漏洞'],
    situations: ['第二档或传球为主的进攻', 'Peyton Manning时代小马队标志防守', '预期传球', '标准防守'],
    difficulty: 'beginner',
    image: 'assets/images/defense-coverage/cover-two-zone.svg'
  },
  {
    id: 'cover-two-man',
    category: 'defense-coverage',
    nameEn: 'Cover Two Man',
    nameCn: 'Cover 2人盯人',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '两个安全卫防守深度区域,其他所有防守球员进行紧密人盯人覆盖的混合防守方案。',
    advantages: ['结合紧密人盯人覆盖和深度安全卫支援', '接球手难以摆脱', '传球窗口狭小', '深度有保险'],
    weaknesses: ['灵活接球手仍可突破人盯人', '易受中路/接缝路线攻击', '对抗跑动QB脆弱', '对角卫要求高'],
    counters: ['利用速度优势甩开防守', '攻击中路接缝区', '跑动QB拉开空间', 'Pick路线'],
    situations: ['第三档极可能传球时', '海盗队(Jamal Dean)常用', '预期传球', '需要深度保护'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/cover-two-man.svg'
  },
  {
    id: 'cover-two-buzz',
    category: 'defense-coverage',
    nameEn: 'Cover Two Buzz',
    nameCn: 'Cover 2冲锋式',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '开球前展示Cover 3阵型,开球后安全卫冲向平层区,角卫后撤深度区,反转职责的伪装防守方案。',
    advantages: ['有效防守快速掩护传球', '欺骗性强', '诱捕读取开球前阵型的QB', '制造意外'],
    weaknesses: ['要求防守球员开球后快速调整', '若QB确认覆盖方式可被利用', '依赖执行', '协调要求高'],
    counters: ['开球后读取防守', '攻击调整中的漏洞', '识别伪装', '快速传球'],
    situations: ['公羊队对抗依赖外围进攻的球队', '对抗快速掩护传球', '伪装战术', '制造混乱'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/cover-two-buzz.svg'
  },
  {
    id: 'tampa-2',
    category: 'defense-coverage',
    nameEn: 'Tampa 2',
    nameCn: 'Tampa 2防守',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: 'Cover 2的变体,中路线卫后撤深度覆盖中路接缝区的经典Tampa防守方案。',
    advantages: ['封闭标准Cover 2的深度中路漏洞', '阻止近端锋攻击接缝区', '弥补中路弱点', '2002海盗队标志'],
    weaknesses: ['易受快速浅层传球攻击', '线卫撤离区域跑动脆弱', '中路线卫压力大', '需要精英线卫'],
    counters: ['快速短传攻击线卫撤离区', '跑动进攻', '利用线卫缺席', '两侧边路进攻'],
    situations: ['对抗精英近端锋如酋长队Kelce', '2002海盗队(Derek Brooks)经典', '防守近端锋', '封闭中路'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/tampa-2.svg'
  },
  {
    id: 'cover-three',
    category: 'defense-coverage',
    nameEn: 'Cover Three',
    nameCn: 'Cover 3防守',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '三个防守球员(1个安全卫,2个角卫)各自防守深度三分之一区域,四个浅层区域防守的平衡防守方案。',
    advantages: ['难以越顶长传', '保持防守球员靠近锋线阻止跑动', '平衡防守', '灵活应对'],
    weaknesses: ['中距离中路区域脆弱', '平层区易受攻击(Sky覆盖)', '边路浅层有漏洞', '依赖区域协防'],
    counters: ['攻击中距离中路', '平层路线', '角卫和安全卫之间区域', '浅层边路'],
    situations: ['早期档位', '海鹰队(Devon Witherspoon)常用', '平衡防守跑传', '标准防守'],
    difficulty: 'beginner',
    image: 'assets/images/defense-coverage/cover-three.svg'
  },
  {
    id: 'cover-three-cloud',
    category: 'defense-coverage',
    nameEn: 'Cover Three Cloud',
    nameCn: 'Cover 3云式',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '一侧角卫保持浅层(平层/干扰),安全卫轮转覆盖该侧深度三分之一区的Cover 3变体防守方案。',
    advantages: ['破坏一侧传球时机', '边路跑动支援更好', '对抗大型接球手有效', '增强边路防守'],
    weaknesses: ['安全卫轮转慢则危险', '易受槽位球员深度Post/直线路线攻击', '依赖轮转', '协调要求高'],
    counters: ['趁安全卫轮转前传球', '槽位球员深度路线', '攻击轮转漏洞', '快速传球'],
    situations: ['对抗大型接球手如猛虎队', '老鹰队(Darius Slay)常用', '增强边路', '对抗体型优势'],
    difficulty: 'beginner',
    image: 'assets/images/defense-coverage/cover-three-cloud.svg'
  },
  {
    id: 'cover-three-buzz',
    category: 'defense-coverage',
    nameEn: 'Cover Three Buzz',
    nameCn: 'Cover 3冲锋式',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '开球前展示两个高位安全卫(Cover 2阵型),开球后一个安全卫冲向浅层区域的伪装防守方案。',
    advantages: ['伪装性强', '诱捕准备应对Cover 2的进攻', '制造紧密的浅层传球窗口', '出其不意'],
    weaknesses: ['安全卫就位前有短暂攻击窗口', '易受假传真跑战术攻击', '依赖快速执行', '读取后易破'],
    counters: ['在安全卫就位前快速传球', '假传真跑战术', '识别伪装', '攻击深度区域'],
    situations: ['早期档位对抗Cover 2破解战术', '钢人队(Minkah Fitzpatrick)常用', '伪装意图', '制造混乱'],
    difficulty: 'beginner',
    image: 'assets/images/defense-coverage/cover-three-buzz.svg'
  },
  {
    id: 'cover-four-quarters',
    category: 'defense-coverage',
    nameEn: 'Cover Four (Quarters)',
    nameCn: 'Cover 4四分防守',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '四个防守后卫各自覆盖深度四分之一区域,三个浅层防守球员的极端保守防守方案。',
    advantages: ['几乎不可能完成深传', '消除大码数长传', '防止达阵长传', '保守防守'],
    weaknesses: ['浅层传球和跑动有大量空间', '放弃短码数', '消耗时间不利', '被短传消磨'],
    counters: ['耐心短传推进', '跑动进攻', '利用浅层空间', '控制时钟'],
    situations: ['比赛末期/长码数情况', '49人队对抗Aaron Rodgers等长传QB', '防止达阵长传', '保护领先'],
    difficulty: 'intermediate',
    image: 'assets/images/defense-coverage/cover-four-quarters.svg'
  },
  {
    id: 'cover-six',
    category: 'defense-coverage',
    nameEn: 'Cover Six',
    nameCn: 'Cover 6混合防守',
    videoSource: 'https://www.youtube.com/watch?v=source1',
    videoTimestamp: '0:00',
    description: '组合覆盖防守:一侧使用Cover 2,另一侧使用Cover 4的非对称混合防守方案。',
    advantages: ['通过展示不同阵型混淆QB', '处理不平衡阵型有效', '灵活应对', '难以读取'],
    weaknesses: ['复杂度高', '容易沟通失误', '需要高度协调', '执行要求高'],
    counters: ['识别覆盖方式差异', '攻击薄弱一侧', '利用沟通失误', '快速读取'],
    situations: ['传球为主的进攻', '爱国者队对抗Josh Allen', '复杂进攻阵型', '混淆对手'],
    difficulty: 'advanced',
    image: 'assets/images/defense-coverage/cover-six.svg'
  },
    // ========== 新增传球路线 (Additional Passing Routes) ==========
  {
    id: 'flat-route',
    category: 'passing-routes',
    nameEn: 'Flat Route',
    nameCn: '平层路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手沿着开球线平行移动,向边线方向推进1-3码,通常由跑卫执行的短距离路线。',
    advantages: ["四分卫压力下的安全出球选择", "利用Cover 3防守中空旷的平层区域"],
    weaknesses: ["容易被云型防守或线附近的线卫覆盖"],
    counters: ["四分卫的安全出球选择", "作为Flood概念战术的组成部分"],
    situations: ["四分卫被施压需要快速出球", "作为Flood概念战术的一部分"],
    difficulty: 'beginner',
    image: 'assets/images/passing-routes/flat-route.svg'
  },
  {
    id: 'comeback-route',
    category: 'passing-routes',
    nameEn: 'Comeback Route',
    nameCn: '回马枪路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手先垂直向前推进18-20码,然后急停并以45度角折返向边线方向。',
    advantages: ["利用角卫担心深传而后撤的防守心理", "一旦启动防守很难恢复"],
    weaknesses: ["需要出色的脚步技术和四分卫精准的时机把握", "出球时机晚容易被抄截"],
    counters: ["配合深度外角路线以孤立角卫", "适合对阵尊重深传的防守"],
    situations: ["与深度外角路线配合使用", "中长距离进攻", "对阵后撤防守"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-routes/comeback-route.svg'
  },
  {
    id: 'hitch-route',
    category: 'passing-routes',
    nameEn: 'Hitch Route',
    nameCn: '急停路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手垂直向前推进5-7码后180度转身面向四分卫接球。',
    advantages: ["快速进攻战术", "有效对抗远离防守(防守者站在7码以外)"],
    weaknesses: ["容易被贴身防守或模式匹配防守破解"],
    counters: ["利用防守者的缓冲距离", "快速出球战术"],
    situations: ["快速进攻", "利用防守者的缓冲空间", "短码数转换"],
    difficulty: 'beginner',
    image: 'assets/images/passing-routes/hitch-route.svg'
  },
  {
    id: 'dig-route',
    category: 'passing-routes',
    nameEn: 'Dig Route',
    nameCn: '挖掘路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手向前推进12-18码后以90度角横向切入场地中央区域。',
    advantages: ["在中场中间区域具有爆发性进攻潜力", "能找到线卫和安全卫之间的空档"],
    weaknesses: ["游走型安全卫常会跳起抄截这种路线"],
    counters: ["配合深度柱式路线或浅层横拖路线使用", "攻击中间区域防守漏洞"],
    situations: ["与深度柱式路线/浅层横拖路线配合", "中距离进攻", "对阵区域防守"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-routes/dig-route.svg'
  },
  {
    id: 'wheel-route',
    category: 'passing-routes',
    nameEn: 'Wheel Route',
    nameCn: '轮式路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手先跑平层路线,然后突然转向垂直沿边线向前冲刺。',
    advantages: ["利用线卫被横向移动吸引的防守弱点", "延迟的垂直威胁攻击"],
    weaknesses: ["需要时间发展完成", "依赖防守者对平层路线的反应"],
    counters: ["适合跑卫/槽位接球手执行(如Christian McCaffrey)", "欺骗性路线组合"],
    situations: ["由跑卫或槽位接球手执行", "对阵积极防守平层的线卫", "中长距离进攻"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-routes/wheel-route.svg'
  },
  {
    id: 'seam-route',
    category: 'passing-routes',
    nameEn: 'Seam Route',
    nameCn: '接缝路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手沿着两名防守者区域责任的边缘接缝处跑动。',
    advantages: ["造成防守犹豫和不确定性", "能找到Cover 3防守的甜蜜点"],
    weaknesses: ["安全卫可以下沉覆盖接缝区域", "容易被提前移位的角卫拦截"],
    counters: ["攻击Cover 3防守深区之间的中间区域", "利用区域防守缝隙"],
    situations: ["对阵Cover 3区域防守", "中距离进攻", "利用防守区域间隙"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-routes/seam-route.svg'
  },
  {
    id: 'option-route',
    category: 'passing-routes',
    nameEn: 'Option Route',
    nameCn: '选择路线',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手根据防守阵型选择折返方向(内切、外切或原地等待)。',
    advantages: ["给予接球手最大自由度", "根据开球后防守弱点灵活调整"],
    weaknesses: ["需要四分卫和接球手完美默契配合", "判断错误容易导致抄截"],
    counters: ["需要经验丰富的四分卫/外接手组合", "灵活应对各种防守"],
    situations: ["经验丰富的四分卫/外接手组合", "对阵复杂防守阵型", "需要灵活调整的情况"],
    difficulty: 'advanced',
    image: 'assets/images/passing-routes/option-route.svg'
  },
  {
    id: 'stop-and-go',
    category: 'passing-routes',
    nameEn: 'Stop and Go',
    nameCn: '急停再启动',
    videoSource: 'https://www.youtube.com/watch?v=source5',
    videoTimestamp: '0:00',
    description: '接球手先假装做急停或内切路线,然后突然加速垂直向前冲刺。',
    advantages: ["击败急于抄截的防守球员", "终极欺骗性二次假动作"],
    weaknesses: ["需要时间让假动作更逼真", "接球手必须有爆发力深传"],
    counters: ["对抗激进的防守球员", "二次假动作路线"],
    situations: ["对阵激进防守球员", "使用二次假动作", "长距离进攻机会"],
    difficulty: 'advanced',
    image: 'assets/images/passing-routes/stop-and-go.svg'
  },
    // ========== 传球概念 (Passing Concepts) ==========
  {
    id: 'mesh-concept',
    category: 'passing-concepts',
    nameEn: 'Mesh Concept',
    nameCn: '网格概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '两名接球手在中场交叉跑动的浅层交叉路线组合战术(在网格点交汇)。',
    advantages: ["对抗人盯人防守极为有效", "自然形成掩护挡拆", "容易传向平层接球点"],
    weaknesses: ["容易被区域下沉防守或人盯人换防技术破解"],
    counters: ["第3档中短码数情况", "酋长队(Travis Kelce)的招牌战术"],
    situations: ["第3档中短码数情况", "酋长队(Travis Kelce)的招牌战术"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/mesh-concept.svg'
  },
  {
    id: 'levels-concept',
    category: 'passing-concepts',
    nameEn: 'Levels Concept',
    nameCn: '层次概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '三名接球手在同侧以不同深度(短、中、深)布阵跑位的分层战术。',
    advantages: ["精准剖析区域防守(Cover 2/3)", "为四分卫创造清晰的高到低阅读选项"],
    weaknesses: ["容易被模式匹配防守或云层防守化解"],
    counters: ["Kyle Shanahan进攻体系的标志", "最大化接球后推进码数"],
    situations: ["Kyle Shanahan进攻体系的标志", "最大化接球后推进码数"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/levels-concept.svg'
  },
  {
    id: 'flood-concept',
    category: 'passing-concepts',
    nameEn: 'Flood Concept',
    nameCn: '洪水概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '三条不同深度的路线集中在同侧(角落路线、外切路线、平层路线)形成洪水般的进攻。',
    advantages: ["用3名接球手对抗2名区域防守球员,对Cover 3/4形成压力"],
    weaknesses: ["对抗Cover 2防守时较弱(安全卫覆盖角落路线)", "容易受到反侧冲传压力"],
    counters: ["公羊队(McVey)招牌战术", "常与外侧区域跑球/假跑传球配合使用"],
    situations: ["公羊队(McVey)招牌战术", "常与外侧区域跑球/假跑传球配合使用"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/flood-concept.svg'
  },
  {
    id: 'smash-concept',
    category: 'passing-concepts',
    nameEn: 'Smash Concept',
    nameCn: '粉碎概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '短距离横停/回切路线搭配深层角落路线的高低组合战术。',
    advantages: ["直接攻击Cover 2防守中角卫与安全卫之间的空隙"],
    weaknesses: ["容易被Tampa 2防守(线卫协防)或伪装防守化解"],
    counters: ["包装工队(Aaron Rodgers)经典战术"],
    situations: ["包装工队(Aaron Rodgers)经典战术"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/smash-concept.svg'
  },
  {
    id: 'y-cross',
    category: 'passing-concepts',
    nameEn: 'Y-Cross',
    nameCn: 'Y字交叉',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '近端锋/槽接手跑深层交叉路线(15-18码),配合垂直清空路线的组合战术。',
    advantages: ["利用区域防守中场空隙", "结合假跑传球可创造爆发性大码数推进"],
    weaknesses: ["受深层安全卫协防或游弋防守球员限制"],
    counters: ["酋长队(Travis Kelce)的拿手好戏"],
    situations: ["酋长队(Travis Kelce)的拿手好戏"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/y-cross.svg'
  },
  {
    id: 'four-verticals',
    category: 'passing-concepts',
    nameEn: 'Four Verticals',
    nameCn: '四垂直路线',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '四名接球手全部跑深层垂直路线的纵深拉伸战术。',
    advantages: ["垂直拉伸防守阵型", "惩罚单高位安全卫防守", "具有大码数推进潜力"],
    weaknesses: ["容易被四分卫防守或快速冲传化解"],
    counters: ["比尔队(Josh Allen强大臂力)的威力展示"],
    situations: ["比尔队(Josh Allen强大臂力)的威力展示"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/four-verticals.svg'
  },
  {
    id: 'stick-concept',
    category: 'passing-concepts',
    nameEn: 'Stick Concept',
    nameCn: '棍棒概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '三角阅读战术:外侧垂直路线、槽位棍棒路线、跑卫平层路线。',
    advantages: ["快速传球战术", "对抗闪电突袭的即时选项", "红区内阅读简单"],
    weaknesses: ["容易被紧逼人盯人或云层区域防守打乱"],
    counters: ["圣徒队(Drew Brees)的经典战术"],
    situations: ["圣徒队(Drew Brees)的经典战术"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/stick-concept.svg'
  },
  {
    id: 'drive-concept',
    category: 'passing-concepts',
    nameEn: 'Drive Concept',
    nameCn: '驱动概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '深层横挖路线叠加浅层交叉路线,配合反侧柱形路线的多层次战术。',
    advantages: ["找到区域防守的空隙", "对抗人盯人形成自然掩护", "适合长码数推进"],
    weaknesses: ["容易被紧密底层区域防守或盯梢防守球员破解"],
    counters: ["猛虎队(Joe Burrow)的进攻利器"],
    situations: ["猛虎队(Joe Burrow)的进攻利器"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/drive-concept.svg'
  },
  {
    id: 'dagger-concept',
    category: 'passing-concepts',
    nameEn: 'Dagger Concept',
    nameCn: '匕首概念',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '内侧接球手垂直清空,外侧接球手跑深层横挖路线的配合战术。',
    advantages: ["垂直路线拉开安全卫,为横挖路线打开中场中层空间"],
    weaknesses: ["容易被Tampa 2或安全卫游弋抢断技术化解"],
    counters: ["牛仔队(CeeDee Lamb)的得分利器"],
    situations: ["牛仔队(CeeDee Lamb)的得分利器"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/dagger-concept.svg'
  },
  {
    id: 'slant-flat',
    category: 'passing-concepts',
    nameEn: 'Slant Flat',
    nameCn: '斜插平层组合',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '外侧接球手跑斜插路线,内侧接球手/跑卫释放到平层区域的配合战术。',
    advantages: ["迫使平层防守球员面临两难选择", "击败人盯人防守位置"],
    weaknesses: ["容易被紧逼人盯人时机把握或陷阱防守破解"],
    counters: ["海豚队(Mike McDaniel)为Tyreek Hill量身打造"],
    situations: ["海豚队(Mike McDaniel)为Tyreek Hill量身打造"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/slant-flat.svg'
  },
  {
    id: 'double-china',
    category: 'passing-concepts',
    nameEn: 'Double China',
    nameCn: '双中路切入',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '两名外侧接球手跑5码内切路线,内侧接球手跑角落路线的红区战术。',
    advantages: ["红区进攻完美战术", "给防守球员制造由内到外的冲突选择"],
    weaknesses: ["容易被平脚Cover 2或游弋线卫防守破解"],
    counters: ["酋长队/爱国者队红区主打战术"],
    situations: ["酋长队/爱国者队红区主打战术"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/double-china.svg'
  },
  {
    id: 'shallow-cross',
    category: 'passing-concepts',
    nameEn: 'Shallow Cross',
    nameCn: '浅层交叉',
    videoSource: 'https://www.youtube.com/watch?v=source4',
    videoTimestamp: '0:00',
    description: '一名接球手在3-5码横向拖曳,其他接球手跑垂直/清空路线的配合战术。',
    advantages: ["容易完成传接", "接球后推进潜力大", "简化四分卫阅读"],
    weaknesses: ["容易被区域下沉防守堵塞交叉通道"],
    counters: ["红雀队(空袭进攻风格)的标志"],
    situations: ["红雀队(空袭进攻风格)的标志"],
    difficulty: 'intermediate',
    image: 'assets/images/passing-concepts/shallow-cross.svg'
  },

  
    {
      id: 'trap-play',
      category: 'running-plays',
      nameEn: 'Trap Play',
      nameCn: '陷阱跑球',
      videoSource: 'https://www.youtube.com/watch?v=Of_TwCsCETs',
      videoTimestamp: '10:45',
      description: '故意让防守线球员穿透,然后用拉动Guard从侧面阻挡他的欺骗性跑球战术。陷阱就是让防守球员以为得手了。',
      advantages: [
        '对抗激进防守',
        '欺骗性强',
        '创造清晰通道',
        '利用防守冲击力'
      ],
      weaknesses: [
        '时机要求极高',
        '需要精确执行',
        '一旦失败很难看',
        '对抗纪律性防守效果有限'
      ],
      counters: [
        '识别进攻线的"放人"',
        '保持防守纪律',
        '不盲目深入',
        '填补其他缝隙'
      ],
      situations: ['对抗激进DT', '短码数', '改变节奏', '欺骗防守'],
      difficulty: 'advanced',
      image: 'assets/images/running/trap-play.svg'
    }
  ]
};

// 辅助函数
const TacticsDataHelper = {
  // 根据ID获取战术
  getTacticById: function(id) {
    return tacticsData.tactics.find(t => t.id === id);
  },

  // 根据分类获取战术
  getTacticsByCategory: function(categoryId) {
    if (categoryId === 'all') {
      return tacticsData.tactics;
    }
    return tacticsData.tactics.filter(t => t.category === categoryId);
  },

  // 根据难度获取战术
  getTacticsByDifficulty: function(difficulty) {
    if (difficulty === 'all') {
      return tacticsData.tactics;
    }
    return tacticsData.tactics.filter(t => t.difficulty === difficulty);
  },

  // 获取分类名称
  getCategoryName: function(categoryId) {
    const category = tacticsData.categories.find(c => c.id === categoryId);
    return category ? category.name : '';
  },

  // 获取分类图标
  getCategoryIcon: function(categoryId) {
    const category = tacticsData.categories.find(c => c.id === categoryId);
    return category ? category.icon : '';
  },

  // 搜索战术
  searchTactics: function(query) {
    if (!query || query.trim() === '') {
      return tacticsData.tactics;
    }

    const lowerQuery = query.toLowerCase().trim();
    return tacticsData.tactics.filter(tactic => {
      const nameEnMatch = tactic.nameEn.toLowerCase().includes(lowerQuery);
      const nameCnMatch = tactic.nameCn && tactic.nameCn.toLowerCase().includes(lowerQuery);
      const descMatch = tactic.description.toLowerCase().includes(lowerQuery);

      return nameEnMatch || nameCnMatch || descMatch;
    });
  }
};
