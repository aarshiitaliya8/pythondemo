document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // 1. Mobile Navbar Toggle
    // ----------------------------------------------------
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
            const icon = navToggle.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.replace('fa-bars', 'fa-xmark');
            } else {
                icon.classList.replace('fa-xmark', 'fa-bars');
            }
        });
    }

    // ----------------------------------------------------
    // 2. Light / Dark Theme Toggle
    // ----------------------------------------------------
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Load saved preference
    const savedTheme = localStorage.getItem('theme') || 'dark';
    if (savedTheme === 'light') {
        body.classList.remove('dark-theme');
        body.classList.add('light-theme');
    } else {
        body.classList.remove('light-theme');
        body.classList.add('dark-theme');
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            if (body.classList.contains('dark-theme')) {
                body.classList.replace('dark-theme', 'light-theme');
                localStorage.setItem('theme', 'light');
            } else {
                body.classList.replace('light-theme', 'dark-theme');
                localStorage.setItem('theme', 'dark');
            }
        });
    }

    // ----------------------------------------------------
    // 3. Client-Side Projects Categorization Filter
    // ----------------------------------------------------
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    if (filterButtons.length > 0 && projectCards.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active button classes
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                // Filter cards based on data-category
                projectCards.forEach(card => {
                    const cardCategory = card.getAttribute('data-category');
                    if (filterValue === 'all' || cardCategory === filterValue) {
                        card.style.display = 'block';
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.transition = 'opacity 0.3s ease';
                            card.style.opacity = '1';
                        }, 50);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // ----------------------------------------------------
    // 4. Contact Form Submission Success Mock Handler
    // ----------------------------------------------------
    const contactForm = document.getElementById('contact-form');
    const formSuccess = document.getElementById('form-success');
    const btnResetForm = document.getElementById('btn-reset-form');

    if (contactForm && formSuccess) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault(); // Stop standard reload
            
            // Capture data for confirmation
            const nameInput = document.getElementById('name').value;
            console.log(`Sending message from ${nameInput}...`);

            // Hide the active input form and display success alert
            contactForm.classList.add('hidden');
            formSuccess.classList.remove('hidden');
        });
    }

    if (btnResetForm && contactForm && formSuccess) {
        btnResetForm.addEventListener('click', () => {
            // Reset input values and toggle display status back
            contactForm.reset();
            formSuccess.classList.add('hidden');
            contactForm.classList.remove('hidden');
        });
    }

    // ----------------------------------------------------
    // 5. Scroll Effect for Navbar Elevation
    // ----------------------------------------------------
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.15)';
            navbar.style.padding = '12px 0';
        } else {
            navbar.style.boxShadow = 'none';
            navbar.style.padding = '16px 0';
        }
    });
});
