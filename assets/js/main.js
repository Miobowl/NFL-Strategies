/* ==========================================
   NFL Strategies - Main JavaScript
   橄榄球战术网站 - 主逻辑文件
   ========================================== */

// ========== Tactics Renderer Class ==========
class TacticsRenderer {
  constructor(containerSelector) {
    this.container = document.querySelector(containerSelector);
    this.currentTactics = [];
  }

  /**
   * Render tactic cards to the grid
   * @param {Array} tactics - Array of tactic objects to render
   */
  renderCards(tactics) {
    this.currentTactics = tactics;

    if (!tactics || tactics.length === 0) {
      this.renderEmpty();
      return;
    }

    this.container.innerHTML = tactics.map(tactic => this.createCardHTML(tactic)).join('');
    this.attachCardListeners();
    this.updateResultsCount(tactics.length);
  }

  /**
   * Create HTML for a single tactic card
   * @param {Object} tactic - Tactic data object
   * @returns {string} HTML string
   */
  createCardHTML(tactic) {
    const categoryName = TacticsDataHelper.getCategoryName(tactic.category);
    const categoryIcon = TacticsDataHelper.getCategoryIcon(tactic.category);
    const descriptionPreview = this.truncateText(tactic.description, 120);

    return `
      <div class="tactic-card" data-id="${tactic.id}">
        <div class="card-image">
          <img src="${tactic.image}" alt="${tactic.nameEn}" loading="lazy" onerror="this.style.display='none'">
          <span class="category-badge">${categoryIcon} ${categoryName}</span>
        </div>
        <div class="card-content">
          <h3 class="tactic-name-en">${tactic.nameEn}</h3>
          ${tactic.nameCn ? `<p class="tactic-name-cn">${tactic.nameCn}</p>` : ''}
          <p class="tactic-description">${descriptionPreview}</p>
          <div class="card-tags">
            ${tactic.situations.slice(0, 3).map(situation =>
              `<span class="tag">${situation}</span>`
            ).join('')}
          </div>
        </div>
      </div>
    `;
  }

  /**
   * Attach click listeners to all cards
   */
  attachCardListeners() {
    const cards = this.container.querySelectorAll('.tactic-card');
    cards.forEach(card => {
      card.addEventListener('click', () => {
        const tacticId = card.dataset.id;
        if (window.modalManager) {
          window.modalManager.open(tacticId);
        }
      });
    });
  }

  /**
   * Render empty state when no tactics match
   */
  renderEmpty() {
    this.container.innerHTML = `
      <div class="empty-state" style="grid-column: 1 / -1;">
        <h3>未找到匹配的战术</h3>
        <p>请尝试调整筛选条件或搜索关键词</p>
      </div>
    `;
    this.updateResultsCount(0);
  }

  /**
   * Truncate text to specified length
   * @param {string} text - Text to truncate
   * @param {number} maxLength - Maximum length
   * @returns {string} Truncated text
   */
  truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength).trim() + '...';
  }

  /**
   * Update results count display
   * @param {number} count - Number of results
   */
  updateResultsCount(count) {
    const resultsCountElement = document.getElementById('results-count');
    if (resultsCountElement) {
      const totalCount = tacticsData.tactics.length;
      if (count === totalCount) {
        resultsCountElement.textContent = `显示全部 ${count} 个战术`;
      } else {
        resultsCountElement.textContent = `找到 ${count} 个战术（共 ${totalCount} 个）`;
      }
    }
  }
}

// ========== Category Filter Manager ==========
class CategoryFilterManager {
  constructor() {
    this.selectElement = document.getElementById('category-filter');
    this.init();
  }

  /**
   * Initialize category filter dropdown
   */
  init() {
    if (!this.selectElement) return;

    // Populate category options
    const optionsHTML = tacticsData.categories.map(category =>
      `<option value="${category.id}">${category.icon} ${category.name}</option>`
    ).join('');

    this.selectElement.innerHTML = `
      <option value="all">全部分类</option>
      ${optionsHTML}
    `;

    // Attach change listener
    this.selectElement.addEventListener('change', () => {
      if (window.filterManager) {
        window.filterManager.applyFilters();
      }
    });
  }

  /**
   * Get currently selected category
   * @returns {string} Category ID or 'all'
   */
  getSelectedCategory() {
    return this.selectElement ? this.selectElement.value : 'all';
  }

  /**
   * Reset to show all categories
   */
  reset() {
    if (this.selectElement) {
      this.selectElement.value = 'all';
    }
  }
}

// ========== Application Initialization ==========
class NFLStrategiesApp {
  constructor() {
    this.renderer = null;
    this.categoryFilter = null;
  }

  /**
   * Initialize the application
   */
  init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.setup());
    } else {
      this.setup();
    }
  }

  /**
   * Setup all components
   */
  setup() {
    // Initialize renderer
    this.renderer = new TacticsRenderer('#tactics-grid');
    window.renderer = this.renderer;

    // Initialize category filter
    this.categoryFilter = new CategoryFilterManager();
    window.categoryFilter = this.categoryFilter;

    // Initialize modal manager (from modal.js)
    if (typeof ModalManager !== 'undefined') {
      window.modalManager = new ModalManager();
    }

    // Initialize filter manager (from filter.js)
    if (typeof FilterManager !== 'undefined') {
      window.filterManager = new FilterManager(this.renderer);
    }

    // Initial render
    this.renderer.renderCards(tacticsData.tactics);

    console.log('✅ NFL Strategies App initialized successfully!');
    console.log(`📊 Loaded ${tacticsData.tactics.length} tactics across ${tacticsData.categories.length} categories`);
  }
}

// ========== Auto-Initialize ==========
const app = new NFLStrategiesApp();
app.init();
