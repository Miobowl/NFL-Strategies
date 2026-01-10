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
