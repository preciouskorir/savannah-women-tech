/* ============================================
   SAVANNAH WOMEN TECH - Main JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

    // ========== NAVBAR SCROLL EFFECT ==========
    var navbar = document.getElementById('navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            navbar.classList.toggle('scrolled', window.scrollY > 20);
        });
    }

    // ========== MOBILE MENU ==========
    var hamburger = document.getElementById('hamburger');
    var navLinks = document.getElementById('navLinks');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', function() {
            navLinks.classList.toggle('open');
            var spans = hamburger.querySelectorAll('span');

            if (navLinks.classList.contains('open')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
                hamburger.setAttribute('aria-expanded', 'true');
            } else {
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
                hamburger.setAttribute('aria-expanded', 'false');
            }
        });

        // Close mobile menu when clicking a link
        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navLinks.classList.remove('open');
                var spans = hamburger.querySelectorAll('span');
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
                hamburger.setAttribute('aria-expanded', 'false');
            });
        });

        // Close mobile menu on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navLinks.classList.contains('open')) {
                navLinks.classList.remove('open');
                var spans = hamburger.querySelectorAll('span');
                spans[0].style.transform = '';
                spans[1].style.opacity = '';
                spans[2].style.transform = '';
                hamburger.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ========== FADE-IN ANIMATIONS ==========
    var fadeElements = document.querySelectorAll('.fade-in');

    if (fadeElements.length > 0) {
        var fadeObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    fadeObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -40px 0px'
        });

        fadeElements.forEach(function(el) {
            fadeObserver.observe(el);
        });
    }

    // ========== ANIMATED COUNTERS ==========
    function animateCounters() {
        var counters = document.querySelectorAll('.impact-number[data-target]');

        counters.forEach(function(counter) {
            var target = parseInt(counter.dataset.target);
            var duration = 2000;
            var start = performance.now();
            var label = counter.closest('.impact-item').querySelector('.impact-label');
            var isPercent = label && label.textContent.includes('%');

            function update(now) {
                var elapsed = now - start;
                var progress = Math.min(elapsed / duration, 1);
                // Ease out quart
                var eased = 1 - Math.pow(1 - progress, 4);
                var current = Math.round(eased * target);

                if (isPercent) {
                    counter.textContent = current + '%';
                } else if (target >= 1000) {
                    counter.textContent = current.toLocaleString() + '+';
                } else {
                    counter.textContent = current + '+';
                }

                if (progress < 1) {
                    requestAnimationFrame(update);
                }
            }

            requestAnimationFrame(update);
        });
    }

    // Trigger counters when impact section is visible
    var impactSection = document.querySelector('.impact');

    if (impactSection) {
        var counterObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    animateCounters();
                    counterObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });

        counterObserver.observe(impactSection);
    }

    // ========== SMOOTH SCROLL FOR ANCHOR LINKS ==========
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;

            var targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

});