/* ==========================================
   NFL Strategies - Filter JavaScript
   橄榄球战术网站 - 筛选和搜索功能
   ========================================== */

// ========== Filter Manager Class ==========
class FilterManager {
  constructor(renderer) {
    this.renderer = renderer;
    this.activeTab = 'all';
    this.activeCategory = 'all';
    this.activeDifficulty = 'all';
    this.searchQuery = '';

    this.setupTabFilters();
    this.setupDifficultyFilters();
    this.setupSearchBox();
  }

  /**
   * Setup tab filter buttons
   */
  setupTabFilters() {
    const tabButtons = document.querySelectorAll('[data-tab]');

    tabButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all tab buttons
        tabButtons.forEach(btn => btn.classList.remove('active'));

        // Add active class to clicked button
        button.classList.add('active');

        // Update active tab
        this.activeTab = button.dataset.tab;

        // Apply filters
        this.applyFilters();
      });
    });
  }

  /**
   * Setup difficulty filter buttons
   */
  setupDifficultyFilters() {
    const difficultyButtons = document.querySelectorAll('[data-difficulty]');

    difficultyButtons.forEach(button => {
      button.addEventListener('click', () => {
        // Remove active class from all buttons
        difficultyButtons.forEach(btn => btn.classList.remove('active'));

        // Add active class to clicked button
        button.classList.add('active');

        // Update active difficulty
        this.activeDifficulty = button.dataset.difficulty;

        // Apply filters
        this.applyFilters();
      });
    });
  }

  /**
   * Setup search box with debounced input
   */
  setupSearchBox() {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');

    if (searchInput) {
      // Debounced search on input
      searchInput.addEventListener('input', this.debounce((e) => {
        this.searchQuery = e.target.value.trim();
        this.applyFilters();
      }, 300));

      // Search on Enter key
      searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
          this.searchQuery = e.target.value.trim();
          this.applyFilters();
        }
      });
    }

    if (searchBtn) {
      // Search on button click
      searchBtn.addEventListener('click', () => {
        if (searchInput) {
          this.searchQuery = searchInput.value.trim();
          this.applyFilters();
        }
      });
    }
  }

  /**
   * Apply all active filters and render results
   */
  applyFilters() {
    let filteredTactics = [...tacticsData.tactics];

    // Apply tab filter first
    if (this.activeTab !== 'all') {
      filteredTactics = this.filterByTab(filteredTactics, this.activeTab);
    }

    // Apply category filter
    if (window.categoryFilter) {
      this.activeCategory = window.categoryFilter.getSelectedCategory();
    }

    if (this.activeCategory !== 'all') {
      filteredTactics = filteredTactics.filter(tactic =>
        tactic.category === this.activeCategory
      );
    }

    // Apply difficulty filter
    if (this.activeDifficulty !== 'all') {
      filteredTactics = filteredTactics.filter(tactic =>
        tactic.difficulty === this.activeDifficulty
      );
    }

    // Apply search filter
    if (this.searchQuery && this.searchQuery.length > 0) {
      filteredTactics = this.searchTactics(filteredTactics, this.searchQuery);
    }

    // Render filtered results
    this.renderer.renderCards(filteredTactics);
  }

  /**
   * Filter tactics by tab
   * @param {Array} tactics - Tactics to filter
   * @param {string} tab - Tab identifier
   * @returns {Array} Filtered tactics
   */
  filterByTab(tactics, tab) {
    const tabCategoryMap = {
      'offense': ['offense-formation', 'passing-concepts', 'running-plays'],
      'defense': ['defense-coverage', 'defense-formation'],
      'routes': ['passing-routes']
    };

    if (tabCategoryMap[tab]) {
      return tactics.filter(tactic =>
        tabCategoryMap[tab].includes(tactic.category)
      );
    }

    return tactics;
  }

  /**
   * Search tactics by query
   * @param {Array} tactics - Tactics to search through
   * @param {string} query - Search query
   * @returns {Array} Filtered tactics
   */
  searchTactics(tactics, query) {
    const lowerQuery = query.toLowerCase();

    return tactics.filter(tactic => {
      // Search in English name
      const nameEnMatch = tactic.nameEn.toLowerCase().includes(lowerQuery);

      // Search in Chinese name
      const nameCnMatch = tactic.nameCn &&
                          tactic.nameCn.toLowerCase().includes(lowerQuery);

      // Search in description
      const descMatch = tactic.description.toLowerCase().includes(lowerQuery);

      // Search in situations
      const situationMatch = tactic.situations.some(situation =>
        situation.toLowerCase().includes(lowerQuery)
      );

      // Search in advantages
      const advantageMatch = tactic.advantages.some(advantage =>
        advantage.toLowerCase().includes(lowerQuery)
      );

      return nameEnMatch || nameCnMatch || descMatch || situationMatch || advantageMatch;
    });
  }

  /**
   * Reset all filters to default
   */
  resetFilters() {
    // Reset tab filter
    const tabButtons = document.querySelectorAll('[data-tab]');
    tabButtons.forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.tab === 'all') {
        btn.classList.add('active');
      }
    });
    this.activeTab = 'all';

    // Reset category filter
    if (window.categoryFilter) {
      window.categoryFilter.reset();
      this.activeCategory = 'all';
    }

    // Reset difficulty filter
    const difficultyButtons = document.querySelectorAll('[data-difficulty]');
    difficultyButtons.forEach(btn => {
      btn.classList.remove('active');
      if (btn.dataset.difficulty === 'all') {
        btn.classList.add('active');
      }
    });
    this.activeDifficulty = 'all';

    // Reset search
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
      searchInput.value = '';
    }
    this.searchQuery = '';

    // Apply (empty) filters to show all tactics
    this.applyFilters();
  }

  /**
   * Debounce function to limit API calls
   * @param {Function} func - Function to debounce
   * @param {number} delay - Delay in milliseconds
   * @returns {Function} Debounced function
   */
  debounce(func, delay) {
    let timeoutId;
    return function (...args) {
      clearTimeout(timeoutId);
      timeoutId = setTimeout(() => {
        func.apply(this, args);
      }, delay);
    };
  }

  /**
   * Get current filter state
   * @returns {Object} Current filter state
   */
  getFilterState() {
    return {
      category: this.activeCategory,
      difficulty: this.activeDifficulty,
      search: this.searchQuery
    };
  }

  /**
   * Set filter state programmatically
   * @param {Object} state - Filter state object
   */
  setFilterState(state) {
    if (state.category !== undefined) {
      this.activeCategory = state.category;
      if (window.categoryFilter && window.categoryFilter.selectElement) {
        window.categoryFilter.selectElement.value = state.category;
      }
    }

    if (state.difficulty !== undefined) {
      this.activeDifficulty = state.difficulty;
      const difficultyButtons = document.querySelectorAll('[data-difficulty]');
      difficultyButtons.forEach(btn => {
        btn.classList.toggle('active', btn.dataset.difficulty === state.difficulty);
      });
    }

    if (state.search !== undefined) {
      this.searchQuery = state.search;
      const searchInput = document.getElementById('search-input');
      if (searchInput) {
        searchInput.value = state.search;
      }
    }

    this.applyFilters();
  }
}

// ========== Advanced Filter Features ==========

/**
 * Filter tactics by multiple situations (AND logic)
 * @param {Array} tactics - Tactics to filter
 * @param {Array} situations - Required situations
 * @returns {Array} Filtered tactics
 */
function filterBySituations(tactics, situations) {
  if (!situations || situations.length === 0) {
    return tactics;
  }

  return tactics.filter(tactic => {
    return situations.every(situation =>
      tactic.situations.includes(situation)
    );
  });
}

/**
 * Get tactics by video source
 * @param {string} videoUrl - YouTube video URL
 * @returns {Array} Tactics from this video
 */
function getTacticsByVideo(videoUrl) {
  return tacticsData.tactics.filter(tactic =>
    tactic.videoSource === videoUrl
  );
}

/**
 * Get unique situations across all tactics
 * @returns {Array} Array of unique situation strings
 */
function getAllSituations() {
  const situations = new Set();
  tacticsData.tactics.forEach(tactic => {
    tactic.situations.forEach(situation => situations.add(situation));
  });
  return Array.from(situations).sort();
}

/**
 * Get tactics count by category
 * @returns {Object} Category ID to count mapping
 */
function getTacticsCountByCategory() {
  const counts = {};
  tacticsData.categories.forEach(category => {
    counts[category.id] = tacticsData.tactics.filter(t =>
      t.category === category.id
    ).length;
  });
  return counts;
}

/**
 * Get tactics count by difficulty
 * @returns {Object} Difficulty level to count mapping
 */
function getTacticsCountByDifficulty() {
  const counts = {
    beginner: 0,
    intermediate: 0,
    advanced: 0
  };

  tacticsData.tactics.forEach(tactic => {
    if (counts[tactic.difficulty] !== undefined) {
      counts[tactic.difficulty]++;
    }
  });

  return counts;
}
