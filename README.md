# 🏈 NFL Strategies - 橄榄球战术学习网站

一个面向橄榄球入门者的交互式战术学习网站，通过图文结合的方式介绍NFL橄榄球中的主要战术。

## ✨ 功能特点

- 📚 **六大战术分类** - 进攻阵型、传球路线、传球概念、防守覆盖、防守阵型、跑球战术
- 🔍 **智能搜索** - 实时搜索战术名称和描述,快速找到你想要的内容
- 🎯 **多维度筛选** - 按分类、难度、场景筛选战术
- 📱 **响应式设计** - 完美支持桌面、平板、手机等各种设备
- 💡 **详细分析** - 每个战术包含介绍、优点、弱点、应对方法和适用场景
- 🎨 **现代界面** - 清爽的设计风格,流畅的交互体验
- 🇨🇳 **完整中文翻译** - 49个战术全部翻译成中文

## 🎯 目标受众

本网站专为**能看懂橄榄球比赛的刚入门的人**设计,帮助他们:
- 理解比赛中常见的战术和阵型
- 学习战术的优缺点和应对方法
- 提升观赛体验和战术理解能力

## 📖 内容来源

所有战术内容基于以下YouTube教学视频整理:

1. **进攻阵型** - [Every OFFENSIVE Formation Explained!](https://www.youtube.com/watch?v=sRaIlyv95hs)
2. **传球路线** - [Passing Routes Explained](https://www.youtube.com/watch?v=Ebn6c1jNZbo)
3. **防守覆盖** - [Defensive Coverage Explained](https://www.youtube.com/watch?v=ROliJ27Br9A)
4. **防守阵型** - [Defensive Formations](https://www.youtube.com/watch?v=Q6iuu58jLgU)
5. **跑球战术** - [Running Plays Breakdown](https://www.youtube.com/watch?v=Of_TwCsCETs)

## 🚀 快速开始

### 在线访问

网站已部署到 GitHub Pages,可以直接访问:
```
https://miobowl.github.io/NFL-Strategies/
```

### 本地运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/Miobowl/NFL-Strategies.git
   cd NFL-Strategies
   ```

2. **直接打开**

   由于是纯前端项目,可以直接在浏览器中打开 `index.html` 文件。

3. **使用本地服务器 (推荐)**

   为了避免跨域问题,建议使用本地HTTP服务器:

   **Python 3:**
   ```bash
   python -m http.server 8000
   ```

   **Node.js (http-server):**
   ```bash
   npx http-server -p 8000
   ```

   然后在浏览器访问: `http://localhost:8000`

## 📂 项目结构

```
NFL-Strategies/
├── index.html                 # 主页面
├── README.md                  # 项目说明
├── .gitignore                # Git忽略文件
├── assets/
│   ├── css/
│   │   ├── main.css          # 主样式(设计系统)
│   │   ├── cards.css         # 卡片样式
│   │   ├── modal.css         # 模态框样式
│   │   └── responsive.css    # 响应式样式
│   ├── js/
│   │   ├── data.js           # 战术数据
│   │   ├── main.js           # 主逻辑(卡片渲染)
│   │   ├── modal.js          # 模态框交互
│   │   └── filter.js         # 筛选和搜索
│   └── images/
│       ├── offense-formation/ # 进攻阵型SVG
│       ├── defense-formation/ # 防守阵型SVG
│       ├── defense-coverage/  # 防守覆盖SVG
│       ├── passing-routes/    # 传球路线SVG
│       ├── passing-concepts/  # 传球概念SVG
│       └── running-plays/     # 跑球战术SVG
```

## 🛠️ 技术栈

- **HTML5** - 语义化标记
- **CSS3** - 现代样式(Grid, Flexbox, CSS Variables)
- **JavaScript (ES6+)** - 原生JS,无框架依赖
- **GitHub Pages** - 免费静态网站托管

## 📄 许可证

本项目仅用于**教育目的**。所有战术内容和图片来源于YouTube教学视频,版权归原作者所有。

## 🙏 致谢

- 感谢YouTube上提供优质橄榄球教学内容的创作者
- 感谢NFL为我们带来精彩的比赛

---

**制作于 2026年** | 🏈 享受橄榄球的乐趣!
