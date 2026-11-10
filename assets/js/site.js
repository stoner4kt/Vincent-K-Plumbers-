(function () {
  'use strict';

  /* ---------------------------------------------------------------- year */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ------------------------------------------------------- mobile menu */
  var menuBtn = document.getElementById('mobile-menu-btn');
  var mobileMenu = document.getElementById('mobile-menu');
  var iconOpen = document.getElementById('menu-icon-open');
  var iconClose = document.getElementById('menu-icon-close');

  function closeMenu() {
    if (!mobileMenu) return;
    mobileMenu.classList.add('hidden');
    if (iconOpen) iconOpen.classList.remove('hidden');
    if (iconClose) iconClose.classList.add('hidden');
    if (menuBtn) menuBtn.setAttribute('aria-expanded', 'false');
  }

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', function () {
      var isHidden = mobileMenu.classList.contains('hidden');
      mobileMenu.classList.toggle('hidden', !isHidden);
      if (iconOpen) iconOpen.classList.toggle('hidden', isHidden);
      if (iconClose) iconClose.classList.toggle('hidden', !isHidden);
      menuBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });
  }

  /* ------------------------------------------------- desktop dropdown */
  var dropParents = document.querySelectorAll('.nav-dropdown-parent');
  dropParents.forEach(function (parent) {
    var trigger = parent.querySelector('[data-dropdown-trigger]');
    var panel = parent.querySelector('.nav-dropdown');
    if (!trigger || !panel) return;

    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      var open = panel.classList.toggle('open');
      trigger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    parent.addEventListener('mouseleave', function () {
      panel.classList.remove('open');
      trigger.setAttribute('aria-expanded', 'false');
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        panel.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      }
    });
  });

  /* -------------------------------------------------- service filters */
  var filterBtns = document.querySelectorAll('.filter-btn');
  var filterCards = document.querySelectorAll('[data-category]');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var filter = btn.getAttribute('data-filter');
      filterBtns.forEach(function (b) {
        b.classList.remove('active', 'bg-slate-900', 'text-white');
        b.classList.add('bg-white', 'border', 'border-slate-200', 'text-slate-700');
      });
      btn.classList.add('active', 'bg-slate-900', 'text-white');
      btn.classList.remove('bg-white', 'border', 'border-slate-200', 'text-slate-700');

      filterCards.forEach(function (card) {
        var match = filter === 'all' || card.getAttribute('data-category') === filter;
        card.classList.toggle('hidden', !match);
        if (match) card.classList.add('visible');
      });
    });
  });

  /* ------------------------------------------------------ FAQ accordion */
  var faqBtns = document.querySelectorAll('.faq-btn');
  faqBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var panel = btn.nextElementSibling;
      var arrow = btn.querySelector('svg');
      var isOpen = !panel.classList.contains('hidden');

      document.querySelectorAll('.faq-panel').forEach(function (p) { p.classList.add('hidden'); });
      document.querySelectorAll('.faq-btn').forEach(function (b) {
        b.setAttribute('aria-expanded', 'false');
        var s = b.querySelector('svg');
        if (s) s.classList.remove('rotate-180');
      });

      if (!isOpen) {
        panel.classList.remove('hidden');
        btn.setAttribute('aria-expanded', 'true');
        if (arrow) arrow.classList.add('rotate-180');
      }
    });
  });

  /* ------------------------------------------------------- Netlify quote form */
  var leadForm = document.getElementById('lead-form');
  if (leadForm) {
    leadForm.addEventListener('submit', async function (e) {
      e.preventDefault();
      var feedback = document.getElementById('form-feedback');
      var submitButton = leadForm.querySelector('button[type="submit"]');
      var name = document.getElementById('customer-name').value.trim();
      var phone = document.getElementById('customer-phone').value.trim();
      var area = document.getElementById('customer-area').value.trim();
      var service = document.getElementById('service-select').value;

      if (!name || !phone || !area) {
        feedback.textContent = 'Please fill in your name, phone number and suburb so we can quote you fast.';
        feedback.className = 'text-xs font-semibold rounded-lg p-3 bg-red-50 text-red-700 border border-red-200 block';
        return;
      }

      if (typeof trackConversion === 'function') {
        trackConversion('generate_lead', { service_selected: service, suburb: area });
      }

      if (submitButton) {
        submitButton.disabled = true;
        submitButton.setAttribute('aria-busy', 'true');
        submitButton.classList.add('opacity-60', 'cursor-wait');
      }
      feedback.textContent = 'Sending your quote request...';
      feedback.className = 'text-xs font-semibold rounded-lg p-3 bg-sky-50 text-sky-800 border border-sky-200 block';

      try {
        var formData = new FormData(leadForm);
        var body = new URLSearchParams();
        formData.forEach(function (value, key) { body.append(key, value); });

        var response = await fetch('/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: body.toString()
        });
        if (!response.ok) throw new Error('Netlify form submission failed');

        feedback.textContent = 'Thank you, ' + name + '! Your quote request has been sent. Vincent K Plumbers will contact you shortly. You can also call 068 134 3276.';
        feedback.className = 'text-xs font-semibold rounded-lg p-3 bg-emerald-50 text-emerald-800 border border-emerald-200 block';
        leadForm.reset();
      } catch (error) {
        feedback.textContent = 'We could not send your request right now. Please call or WhatsApp 068 134 3276.';
        feedback.className = 'text-xs font-semibold rounded-lg p-3 bg-red-50 text-red-700 border border-red-200 block';
      } finally {
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.removeAttribute('aria-busy');
          submitButton.classList.remove('opacity-60', 'cursor-wait');
        }
      }
    });
  }

  /* ---------------------------------------------------- scroll reveal */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* --------------------------------------------------------- lightbox */
  var lightbox = document.getElementById('lightbox');
  if (lightbox) {
    var lbImg = lightbox.querySelector('[data-lightbox-img]');
    var lbCaption = lightbox.querySelector('[data-lightbox-caption]');
    var lastFocus = null;

    function openLightbox(figure) {
      var img = figure.querySelector('img');
      if (!img) return;
      lastFocus = document.activeElement;
      lbImg.src = img.getAttribute('data-full') || img.currentSrc || img.src;
      lbImg.alt = img.alt || '';
      lbCaption.textContent = img.getAttribute('data-caption') || img.alt || '';
      lightbox.classList.add('open');
      document.body.classList.add('lightbox-open');
      lightbox.querySelector('[data-lightbox-close]').focus();
    }

    function closeLightbox() {
      lightbox.classList.remove('open');
      document.body.classList.remove('lightbox-open');
      lbImg.removeAttribute('src');
      if (lastFocus) lastFocus.focus();
    }

    document.querySelectorAll('.gallery-item').forEach(function (figure) {
      figure.setAttribute('tabindex', '0');
      figure.setAttribute('role', 'button');
      figure.addEventListener('click', function () { openLightbox(figure); });
      figure.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openLightbox(figure);
        }
      });
    });

    lightbox.addEventListener('click', function (e) {
      if (e.target === lightbox || e.target.hasAttribute('data-lightbox-close')) closeLightbox();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && lightbox.classList.contains('open')) closeLightbox();
    });
  }

  /* ------------------------------------------- testimonial / step state */
  document.querySelectorAll('[data-select-service]').forEach(function (el) {
    el.addEventListener('click', function () {
      var value = el.getAttribute('data-select-service');
      var select = document.getElementById('service-select');
      if (select) {
        for (var i = 0; i < select.options.length; i++) {
          if (select.options[i].value === value) { select.selectedIndex = i; break; }
        }
      }
    });
  });
})();

/* Pre-select a service in the quote card and scroll it into view. */
function selectServiceForQuote(serviceName) {
  var select = document.getElementById('service-select');
  if (select) {
    for (var i = 0; i < select.options.length; i++) {
      if (select.options[i].value === serviceName) {
        select.selectedIndex = i;
        break;
      }
    }
  }
  var card = document.getElementById('quote-form');
  if (card) {
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    window.setTimeout(function () {
      var nameInput = document.getElementById('customer-name');
      if (nameInput) nameInput.focus({ preventScroll: true });
    }, 500);
  }
  if (typeof trackConversion === 'function') {
    trackConversion('service_quote_click', { service_name: serviceName });
  }
}
