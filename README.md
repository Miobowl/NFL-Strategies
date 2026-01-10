# 🏈 NFL Strategies - 橄榄球战术学习网站

一个面向橄榄球入门者的交互式战术学习网站，通过图文结合的方式介绍NFL橄榄球中的主要战术。

## ✨ 功能特点

- 📚 **六大战术分类** - 进攻阵型、传球路线、传球跑动路线、防守覆盖、防守阵型、跑球战术
- 🔍 **智能搜索** - 实时搜索战术名称和描述,快速找到你想要的内容
- 🎯 **多维度筛选** - 按分类、难度、场景筛选战术
- 📱 **响应式设计** - 完美支持桌面、平板、手机等各种设备
- 💡 **详细分析** - 每个战术包含介绍、优点、弱点、应对方法和适用场景
- 🎨 **现代界面** - 清爽的设计风格,流畅的交互体验

## 🎯 目标受众

本网站专为**能看懂橄榄球比赛的刚入门的人**设计,帮助他们:
- 理解比赛中常见的战术和阵型
- 学习战术的优缺点和应对方法
- 提升观赛体验和战术理解能力

## 📖 内容来源

所有战术内容基于以下YouTube教学视频整理:

1. **进攻阵型** - [Every OFFENSIVE Formation Explained!](https://www.youtube.com/watch?v=sRaIlyv95hs)
2. **传球路线** - [Passing Routes Explained](https://www.youtube.com/watch?v=Ebn6c1jNZbo)
3. **传球跑动路线** - [RPO Concepts](https://www.youtube.com/watch?v=2exkTbFboDw)
4. **防守覆盖** - [Defensive Coverage Explained](https://www.youtube.com/watch?v=ROliJ27Br9A)
5. **防守阵型** - [Defensive Formations](https://www.youtube.com/watch?v=Q6iuu58jLgU)
6. **跑球战术** - [Running Plays Breakdown](https://www.youtube.com/watch?v=Of_TwCsCETs)

## 🚀 快速开始

### 在线访问

网站已部署到 GitHub Pages,可以直接访问:
```
https://yourusername.github.io/NFL-Strategies/
```

### 本地运行

1. **克隆仓库**
   ```bash
   git clone https://github.com/yourusername/NFL-Strategies.git
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

   **Python 2:**
   ```bash
   python -m SimpleHTTPServer 8000
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
│       ├── offense/          # 进攻相关截图
│       ├── defense/          # 防守相关截图
│       ├── routes/           # 路线相关截图
│       └── running/          # 跑球相关截图
```

## 🛠️ 技术栈

- **HTML5** - 语义化标记
- **CSS3** - 现代样式(Grid, Flexbox, CSS Variables)
- **JavaScript (ES6+)** - 原生JS,无框架依赖
- **GitHub Pages** - 免费静态网站托管

## 📝 添加新战术

要添加新的战术数据,请编辑 `assets/js/data.js` 文件:

```javascript
{
  id: 'unique-id',                    // 唯一标识符
  category: 'offense-formation',      // 所属分类
  nameEn: 'Play Action Pass',         // 英文名称
  nameCn: '假跑真传',                  // 中文名称
  videoSource: 'https://youtube.com/...', // 视频URL
  videoTimestamp: '3:45',             // 时间戳
  description: '详细描述...',         // 战术描述
  advantages: ['优点1', '优点2'],     // 优点列表
  weaknesses: ['弱点1', '弱点2'],     // 弱点列表
  counters: ['应对1', '应对2'],       // 应对方法
  situations: ['短码数', '红区'],     // 适用场景
  difficulty: 'beginner',             // 难度等级
  image: 'assets/images/...'          // 图片路径
}
```

## 📸 添加图片

1. 从YouTube视频中截取关键画面 (Windows: Win + Shift + S)
2. 使用 [TinyPNG](https://tinypng.com/) 或 [Squoosh](https://squoosh.app/) 压缩图片
3. 保存到对应分类文件夹 (`assets/images/offense/` 等)
4. 文件命名规范: `category-tactic-name.jpg`
5. 建议尺寸: 1280x720 或 1920x1080
6. 建议大小: < 150KB

## 🌐 部署到 GitHub Pages

1. **创建GitHub仓库**

   在GitHub上创建一个新仓库 (例如: `NFL-Strategies`)

2. **推送代码**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: NFL Strategies website"
   git branch -M main
   git remote add origin https://github.com/yourusername/NFL-Strategies.git
   git push -u origin main
   ```

3. **启用GitHub Pages**

   - 进入仓库的 Settings → Pages
   - Source 选择 `main` 分支 → `/ (root)` 目录
   - 点击 Save
   - 等待 2-3 分钟,访问 `https://yourusername.github.io/NFL-Strategies/`

## 🎨 自定义主题

可以通过修改 `assets/css/main.css` 中的 CSS 变量来自定义主题颜色:

```css
:root {
  --primary-color: #1a472a;      /* 主色调 */
  --secondary-color: #d50a0a;    /* 次要色 */
  --bg-color: #f5f7f9;           /* 背景色 */
  --text-primary: #2c3e50;       /* 主文本色 */
  /* ... 更多变量 */
}
```

## 📱 浏览器支持

- Chrome / Edge (最新版本)
- Firefox (最新版本)
- Safari 12+
- 移动端浏览器 (iOS Safari, Chrome Mobile)

## 🤝 贡献指南

欢迎提交问题和拉取请求来改进这个项目!

1. Fork 这个仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

## 📄 许可证

本项目仅用于**教育目的**。所有战术内容和图片来源于YouTube教学视频,版权归原作者所有。

## 🙏 致谢

- 感谢YouTube上提供优质橄榄球教学内容的创作者
- 感谢NFL为我们带来精彩的比赛

## 📧 联系方式

如有问题或建议,请通过以下方式联系:

- 提交 [GitHub Issue](https://github.com/yourusername/NFL-Strategies/issues)
- 邮箱: your.email@example.com

---

**制作于 2026年** | 🏈 享受橄榄球的乐趣!
