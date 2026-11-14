(() => {
  const root = document.documentElement;
  if (!window.matchMedia || !window.matchMedia('(prefers-reduced-motion: reduce)').matches) root.classList.add('motion');
  try {
    const saved = localStorage.getItem('tina-theme');
    if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
  } catch (_) { /* Private browsing/storage restrictions must not block the UI. */ }

  const themeButtons = document.querySelectorAll('[data-theme-toggle]');
  themeButtons.forEach(btn => btn.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('tina-theme', next); } catch (_) {}
  }));

  const menu = document.querySelector('[data-menu]');
  const toggle = document.querySelector('[data-menu-toggle]');
  if (menu && toggle) {
    const close = () => { menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); };
    toggle.addEventListener('click', () => {
      const opened = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(opened));
    });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', close));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  // Enlarging authentic research figures does not alter or expose source data.
  const lightbox = document.getElementById('research-lightbox-v83');
  if (lightbox && typeof lightbox.showModal === 'function') {
    const zoomed = lightbox.querySelector('img');
    document.querySelectorAll('[data-lightbox]').forEach(link => link.addEventListener('click', event => {
      event.preventDefault();
      zoomed.src = link.href;
      lightbox.showModal();
    }));
    lightbox.querySelector('button').addEventListener('click', () => lightbox.close());
    lightbox.addEventListener('click', e => { if (e.target === lightbox) lightbox.close(); });
    lightbox.addEventListener('close', () => { zoomed.removeAttribute('src'); });
  }

  // V8.15 · FairPay product screenshots: accessible modal, Escape and backdrop close,
  // focus return, and direct-image fallback if <dialog> is unsupported.
  const fairpayLightbox = document.getElementById('fairpay-lightbox-v815');
  if (fairpayLightbox && typeof fairpayLightbox.showModal === 'function') {
    const img = fairpayLightbox.querySelector('img');
    const caption = fairpayLightbox.querySelector('.fairpay-lightbox-caption-v815');
    let lastTrigger = null;
    document.querySelectorAll('[data-fairpay-zoom]').forEach(link => {
      link.addEventListener('click', event => {
        event.preventDefault();
        lastTrigger = link;
        img.src = link.href;
        img.alt = link.querySelector('img')?.alt || '';
        caption.textContent = link.closest('figure')?.querySelector('figcaption')?.textContent?.trim() || '';
        fairpayLightbox.showModal();
      });
    });
    fairpayLightbox.querySelector('button').addEventListener('click', () => fairpayLightbox.close());
    fairpayLightbox.addEventListener('click', event => { if (event.target === fairpayLightbox) fairpayLightbox.close(); });
    fairpayLightbox.addEventListener('close', () => {
      img.removeAttribute('src');
      if (lastTrigger) lastTrigger.focus({ preventScroll: true });
    });
  }

  // Highlight current case-study section without introducing a fixed mobile overlay.
  const caseNav = document.querySelector('.case-margin-nav-v526 nav');
  if (caseNav) {
    const links = [...caseNav.querySelectorAll('a[href^="#"]')];
    const sections = links.map(a => document.getElementById(a.hash.substring(1)));
    const active = () => {
      let current = 0;
      for (let i = 0; i < sections.length; i++) {
        if (sections[i] && sections[i].getBoundingClientRect().top <= window.innerHeight * .34) current = i;
      }
      links.forEach((link, index) => {
        if (index === current) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    };
    let scheduled = false;
    const requestUpdate = () => {
      if (scheduled) return;
      scheduled = true;
      requestAnimationFrame(() => { scheduled = false; active(); });
    };
    active();
    window.addEventListener('scroll', requestUpdate, { passive: true });
    window.addEventListener('resize', requestUpdate, { passive: true });
  }

  const reveal = document.querySelectorAll('.reveal');
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    reveal.forEach(el => el.classList.add('visible'));
  } else if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {
      if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); }
    }), { threshold: 0.08 });
    reveal.forEach(el => observer.observe(el));
  } else { reveal.forEach(el => el.classList.add('visible')); }
})();
