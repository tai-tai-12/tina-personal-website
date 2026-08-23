(() => {
  const root = document.documentElement;
  const saved = localStorage.getItem('tina-theme');
  if (saved) root.dataset.theme = saved;
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => btn.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next; localStorage.setItem('tina-theme', next);
  }));
  const menu = document.querySelector('[data-menu]');
  const toggle = document.querySelector('[data-menu-toggle]');
  if (menu && toggle) {
    toggle.addEventListener('click', () => { const open = menu.classList.toggle('open'); toggle.setAttribute('aria-expanded', String(open)); });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { menu.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); }));
  }
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(entries => entries.forEach(e => { if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target);} }), {threshold:.08}) : null;
  document.querySelectorAll('.reveal').forEach(el => io ? io.observe(el) : el.classList.add('visible'));
})();
