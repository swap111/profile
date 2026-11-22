// SwapnaLoka — mobile menu, reveal-on-scroll, footer year
(function () {
  var toggle = document.querySelector('.nav__toggle');
  var menu = document.getElementById('menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { menu.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
    });
  }

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  if ('IntersectionObserver' in window) {
    var els = document.querySelectorAll('.section h2, .card, .focus__item, .book, .timeline li, .newsletter, .video');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { el.classList.add('reveal'); io.observe(el); });
    // safety net: never leave content hidden (print, crawlers, odd viewports)
    setTimeout(function () { els.forEach(function (el) { el.classList.add('in'); }); }, 2500);
  }
})();
