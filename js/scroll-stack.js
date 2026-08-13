/**
 * Scroll Stack Effect — EX Devedor
 * Cada seção age como um card que fica "grudado" no topo enquanto
 * a próxima sobe por cima, criando o efeito de pilha/deslize.
 *
 * Para browsers modernos (Chrome 115+, Edge 115+, Safari 26+):
 *   a animação é feita inteiramente via CSS scroll-driven animations.
 *
 * Para Firefox e outros sem suporte:
 *   usa requestAnimationFrame + scroll listener como fallback.
 */
(function () {
  'use strict';

  const STACK_SELECTOR = '.stack-section';
  const SCALE_MIN      = 0.92;   // escala mínima quando coberta
  const RADIUS_MAX     = 20;     // border-radius máximo (px)
  const BRIGHTNESS_MIN = 0.82;   // filtro de brilho mínimo

  function initScrollStack() {
    const sections = Array.from(document.querySelectorAll(STACK_SELECTOR));
    if (!sections.length) return;

    // Atribui z-index crescente: seções posteriores ficam por cima das anteriores
    sections.forEach((el, i) => {
      el.style.zIndex = i + 1;
    });

    // Verifica suporte nativo a scroll-driven animations
    const supportsNative =
      CSS.supports('animation-timeline: scroll()') &&
      CSS.supports('animation-range: entry');

    if (supportsNative) {
      // O CSS já cuida de tudo — nada a fazer aqui
      return;
    }

    // ── Fallback JS para Firefox ──────────────────────────────────────────
    // Percorre todas as seções; para cada uma que está "saindo" pelo topo
    // (já foi scrollada para além do ponto sticky), aplica scale + radius + brightness.

    let ticking = false;

    function updateSections() {
      sections.forEach((section, i) => {
        // Só anima seções que não são hero e não são a última
        if (section.classList.contains('stack-hero') || i === sections.length - 1) {
          return;
        }

        const rect = section.getBoundingClientRect();
        // "top" do sticky é sempre 0 (seção colada no topo da viewport)
        // Quando rect.top fica negativa, a seção começou a sair pelo topo
        const outDistance = Math.max(0, -rect.top);
        // Normaliza: completa em 40% da altura da seção
        const ratio = Math.min(outDistance / (section.offsetHeight * 0.4), 1);

        if (ratio === 0) {
          // Seção completamente visível — reseta
          section.style.transform   = '';
          section.style.borderRadius = '';
          section.style.filter       = '';
        } else {
          const scale      = 1 - ratio * (1 - SCALE_MIN);
          const radius     = ratio * RADIUS_MAX;
          const brightness = 1 - ratio * (1 - BRIGHTNESS_MIN);

          section.style.transform      = `scale(${scale.toFixed(4)})`;
          section.style.transformOrigin = 'top center';
          section.style.borderRadius    = `0 0 ${radius.toFixed(1)}px ${radius.toFixed(1)}px`;
          section.style.filter          = `brightness(${brightness.toFixed(3)})`;
        }
      });

      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        requestAnimationFrame(updateSections);
        ticking = true;
      }
    }, { passive: true });

    // Executa uma vez para o estado inicial
    updateSections();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initScrollStack);
  } else {
    initScrollStack();
  }
})();
