// News Portal — Main JavaScript

document.addEventListener('DOMContentLoaded', function () {

    // Navbar scroll effect
    const navbar = document.getElementById('main-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // Smooth scroll to comments
    const hash = window.location.hash;
    if (hash === '#comments') {
        const el = document.getElementById('comments');
        if (el) {
            setTimeout(() => {
                el.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 300);
        }
    }

    // Animate cards on scroll (Intersection Observer)
    const cards = document.querySelectorAll('.news-card, .feature-card, .about-card, .form-card');
    if ('IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        cards.forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'all 0.5s ease';
            observer.observe(card);
        });
    }

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) bsAlert.close();
        }, 5000);
    });

});
