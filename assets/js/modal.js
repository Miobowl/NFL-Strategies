/* ==========================================
   NFL Strategies - Modal JavaScript
   橄榄球战术网站 - 模态框交互
   ========================================== */

// ========== Modal Manager Class ==========
class ModalManager {
  constructor() {
    this.modal = document.getElementById('tactic-modal');
    this.closeBtn = document.getElementById('modal-close');
    this.overlay = this.modal ? this.modal.querySelector('.modal-overlay') : null;
    this.currentTacticId = null;

    this.setupEventListeners();
  }

  /**
   * Open modal with tactic details
   * @param {string} tacticId - ID of the tactic to display
   */
  open(tacticId) {
    const tactic = TacticsDataHelper.getTacticById(tacticId);

    if (!tactic) {
      console.error(`Tactic with ID "${tacticId}" not found`);
      return;
    }

    this.currentTacticId = tacticId;
    this.populateModal(tactic);
    this.show();
  }

  /**
   * Close the modal
   */
  close() {
    this.hide();
    this.currentTacticId = null;
  }

  /**
   * Show the modal
   */
  show() {
    if (this.modal) {
      this.modal.classList.add('active');
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
    }
  }

  /**
   * Hide the modal
   */
  hide() {
    if (this.modal) {
      this.modal.classList.remove('active');
      document.body.style.overflow = ''; // Restore scrolling
    }
  }

  /**
   * Populate modal with tactic data
   * @param {Object} tactic - Tactic data object
   */
  populateModal(tactic) {
    const categoryName = TacticsDataHelper.getCategoryName(tactic.category);
    const categoryIcon = TacticsDataHelper.getCategoryIcon(tactic.category);

    // Category badge
    const categoryBadge = document.getElementById('modal-category-badge');
    if (categoryBadge) {
      categoryBadge.textContent = `${categoryIcon} ${categoryName}`;
    }

    // Titles
    const titleEn = document.getElementById('modal-title-en');
    if (titleEn) {
      titleEn.textContent = tactic.nameEn;
    }

    const titleCn = document.getElementById('modal-title-cn');
    if (titleCn) {
      titleCn.textContent = tactic.nameCn || '';
      titleCn.style.display = tactic.nameCn ? 'block' : 'none';
    }

    // Image
    const image = document.getElementById('modal-image');
    if (image) {
      image.src = tactic.image;
      image.alt = tactic.nameEn;
    }

    // Description
    const description = document.getElementById('modal-description');
    if (description) {
      description.textContent = tactic.description;
    }

    // Advantages
    this.populateList('modal-advantages', tactic.advantages);

    // Weaknesses
    this.populateList('modal-weaknesses', tactic.weaknesses);

    // Counters
    this.populateList('modal-counters', tactic.counters);

    // Situations
    this.populateSituations('modal-situations', tactic.situations);

    // Video link
    const videoLink = document.getElementById('modal-video-link');
    if (videoLink && tactic.videoSource) {
      let linkText = '查看视频来源 📺';
      if (tactic.videoTimestamp) {
        linkText += ` (${tactic.videoTimestamp})`;
      }
      videoLink.textContent = linkText;
      videoLink.href = tactic.videoSource;
    }
  }

  /**
   * Populate a list element with items
   * @param {string} elementId - ID of the list element
   * @param {Array} items - Array of list items
   */
  populateList(elementId, items) {
    const listElement = document.getElementById(elementId);
    if (!listElement) return;

    if (!items || items.length === 0) {
      listElement.innerHTML = '<li>暂无数据</li>';
      return;
    }

    listElement.innerHTML = items.map(item =>
      `<li>${this.escapeHtml(item)}</li>`
    ).join('');
  }

  /**
   * Populate situations tags
   * @param {string} elementId - ID of the container element
   * @param {Array} situations - Array of situation strings
   */
  populateSituations(elementId, situations) {
    const container = document.getElementById(elementId);
    if (!container) return;

    if (!situations || situations.length === 0) {
      container.innerHTML = '';
      return;
    }

    container.innerHTML = situations.map(situation =>
      `<span class="situation-tag">${this.escapeHtml(situation)}</span>`
    ).join('');
  }

  /**
   * Setup event listeners for modal controls
   */
  setupEventListeners() {
    // Close button
    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => this.close());
    }

    // Click overlay to close
    if (this.overlay) {
      this.overlay.addEventListener('click', () => this.close());
    }

    // ESC key to close
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.modal && this.modal.classList.contains('active')) {
        this.close();
      }
    });

    // Prevent modal content click from closing modal
    if (this.modal) {
      const modalContent = this.modal.querySelector('.modal-content');
      if (modalContent) {
        modalContent.addEventListener('click', (e) => {
          e.stopPropagation();
        });
      }
    }
  }

  /**
   * Escape HTML to prevent XSS
   * @param {string} text - Text to escape
   * @returns {string} Escaped text
   */
  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Navigate to next tactic (optional feature)
   */
  nextTactic() {
    if (!this.currentTacticId) return;

    const currentIndex = tacticsData.tactics.findIndex(t => t.id === this.currentTacticId);
    if (currentIndex === -1) return;

    const nextIndex = (currentIndex + 1) % tacticsData.tactics.length;
    const nextTactic = tacticsData.tactics[nextIndex];

    this.open(nextTactic.id);
  }

  /**
   * Navigate to previous tactic (optional feature)
   */
  prevTactic() {
    if (!this.currentTacticId) return;

    const currentIndex = tacticsData.tactics.findIndex(t => t.id === this.currentTacticId);
    if (currentIndex === -1) return;

    const prevIndex = (currentIndex - 1 + tacticsData.tactics.length) % tacticsData.tactics.length;
    const prevTactic = tacticsData.tactics[prevIndex];

    this.open(prevTactic.id);
  }
}
