document.addEventListener('DOMContentLoaded', () => {
    
    // --- MOBILE MENU TOGGLE ---
                spans[2].style.transform = 'rotate(-45deg) translate(6px, -6px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }

    // --- HEADER SCROLL TRANSITION (transparent → solid) ---
    const header = document.getElementById('main-header');
    const heroSection = document.getElementById('hero-section');

    if (header && heroSection) {
        const heroHeight = heroSection.offsetHeight || window.innerHeight;

        const handleScroll = () => {
            const scrollY = window.scrollY;

            if (scrollY > heroHeight * 0.6) {
                // Past 60% of the hero: go solid
                header.classList.remove('header--transparent');
                header.classList.add('scrolled');
            } else {
                // Still inside hero: stay transparent
                header.classList.remove('scrolled');
                header.classList.add('header--transparent');
            }
        };

        // Initial check on load
        handleScroll();
        window.addEventListener('scroll', handleScroll, { passive: true });
    }



    // --- DEBT SIMULATOR LOGIC ---
    const debtAmountSlider = document.getElementById('debt-amount-slider');
    const debtDelaySlider = document.getElementById('debt-delay-slider');
    const monthlyPaySlider = document.getElementById('monthly-pay-slider');
    
    // Labels
    const debtAmountLabel = document.getElementById('debt-amount-label');
    const debtDelayLabel = document.getElementById('debt-delay-label');
    const monthlyPayLabel = document.getElementById('monthly-pay-label');
    
    // Outputs
    const discountBadge = document.getElementById('discount-badge');
    const resultPayValue = document.getElementById('result-pay-value');
    const originalVsDeal = document.getElementById('original-vs-deal');
    const resultMonthsNeeded = document.getElementById('result-months-needed');
    const resultScoreProject = document.getElementById('result-score-project');
    
    // Helper to format currency
    const formatBRL = (value) => {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL',
            maximumFractionDigits: 0
        }).format(value);
    };

    const updateSimulation = () => {
        if (!debtAmountSlider || !debtDelaySlider || !monthlyPaySlider) return;
        
        const originalVal = parseFloat(debtAmountSlider.value);
        const delayMonths = parseInt(debtDelaySlider.value);
        const monthlyPay = parseFloat(monthlyPaySlider.value);
        
        // Update labels
        debtAmountLabel.textContent = formatBRL(originalVal);
        
        let delayText = '';
        if (delayMonths < 12) {
            delayText = `${delayMonths} ${delayMonths === 1 ? 'mês' : 'meses'}`;
        } else {
            const years = Math.floor(delayMonths / 12);
            const remainingMonths = delayMonths % 12;
            if (remainingMonths === 0) {
                delayText = `${years} ${years === 1 ? 'ano' : 'anos'}`;
            } else {
                delayText = `${years} ${years === 1 ? 'ano' : 'anos'} e ${remainingMonths} ${remainingMonths === 1 ? 'mês' : 'meses'}`;
            }
        }
        debtDelayLabel.textContent = delayText;
        monthlyPayLabel.textContent = `${formatBRL(monthlyPay)}/mês`;
        
        // Discount calculation based on debt age
        let discountPercent = 0.15; // default 15%
        if (delayMonths > 3 && delayMonths <= 6) {
            discountPercent = 0.35; // 35%
        } else if (delayMonths > 6 && delayMonths <= 12) {
            discountPercent = 0.55; // 55%
        } else if (delayMonths > 12 && delayMonths <= 24) {
            discountPercent = 0.75; // 75%
        } else if (delayMonths > 24) {
            discountPercent = 0.88; // 88%
        }
        
        const discountAmount = originalVal * discountPercent;
        const projectedPay = originalVal - discountAmount;
        const totalSaved = discountAmount;
        
        // Months needed to save up for the settlement
        const monthsNeeded = Math.ceil(projectedPay / monthlyPay);
        
        // Score improvement forecast
        let scoreText = 'Aumento Moderado';
        let scoreColor = 'var(--text-primary)';
        
        if (originalVal > 25000 && delayMonths > 18) {
            scoreText = 'Aumento Muito Alto (+280)';
            scoreColor = 'var(--accent-orange)';
        } else if (originalVal > 8000) {
            scoreText = 'Aumento Alto (+180)';
            scoreColor = 'var(--accent-orange)';
        } else {
            scoreText = 'Aumento Médio (+110)';
            scoreColor = 'var(--brand-navy)';
        }
        
        // Render values to UI
        if (discountBadge) {
            discountBadge.textContent = `${Math.round(discountPercent * 100)}% OFF`;
        }
        if (resultPayValue) {
            resultPayValue.textContent = formatBRL(projectedPay);
        }
        if (originalVsDeal) {
            originalVsDeal.textContent = `Você economiza ${formatBRL(totalSaved)}`;
        }
        if (resultMonthsNeeded) {
            resultMonthsNeeded.textContent = `${monthsNeeded} ${monthsNeeded === 1 ? 'mês' : 'meses'}`;
        }
        if (resultScoreProject) {
            resultScoreProject.textContent = scoreText;
            resultScoreProject.style.color = scoreColor;
        }
    };
    
    // Add event listeners for sliders
    if (debtAmountSlider) debtAmountSlider.addEventListener('input', updateSimulation);
    if (debtDelaySlider) debtDelaySlider.addEventListener('input', updateSimulation);
    if (monthlyPaySlider) monthlyPaySlider.addEventListener('input', updateSimulation);
    
    // Initial run to set values on page load
    updateSimulation();


    // --- CONTACT FORM SUBMISSION MOCK ---
    const contactForm = document.getElementById('contact-form');
    const formSuccessMessage = document.getElementById('form-success-message');
    
    if (contactForm && formSuccessMessage) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Basic client-side validation
            const nameInput = document.getElementById('contact-name');
            const emailInput = document.getElementById('contact-email');
            
            let isValid = true;
            
            // Simple validation resets
            [nameInput, emailInput].forEach(input => {
                if (input) {
                    input.style.borderColor = 'var(--border-color)';
                }
            });
            
            if (nameInput && nameInput.value.trim() === '') {
                nameInput.style.borderColor = '#ef4444';
                isValid = false;
            }
            
            if (emailInput && (emailInput.value.trim() === '' || !emailInput.value.includes('@'))) {
                emailInput.style.borderColor = '#ef4444';
                isValid = false;
            }
            
            if (isValid) {
                // Mock form sending
                const submitBtn = document.getElementById('contact-submit-btn');
                if (submitBtn) {
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = 'Enviando... <i data-lucide="loader" class="animate-spin"></i>';
                    if (window.lucide) window.lucide.createIcons();
                }
                
                setTimeout(() => {
                    // Show success block
                    formSuccessMessage.style.display = 'flex';
                    formSuccessMessage.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    
                    // Reset form fields
                    contactForm.reset();
                    
                    // Reset button state
                    if (submitBtn) {
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = 'Enviar Mensagem <i data-lucide="send"></i>';
                        if (window.lucide) window.lucide.createIcons();
                    }
                    
                    // Hide success message after 8 seconds
                    setTimeout(() => {
                        formSuccessMessage.style.fadeOut = true;
                        // Smoothly hide it
                        let opacity = 1;
                        const fadeEffect = setInterval(() => {
                            if (opacity > 0.1) {
                                opacity -= 0.1;
                                formSuccessMessage.style.opacity = opacity;
                            } else {
                                clearInterval(fadeEffect);
                                formSuccessMessage.style.display = 'none';
                                formSuccessMessage.style.opacity = 1;
                            }
                        }, 50);
                    }, 8000);
                    
                }, 1200);
            }
        });
    }

    // Dropdown toggle for mobile
    document.querySelectorAll('.dropdown-toggle').forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            if (window.innerWidth <= 992) {
                e.preventDefault();
                toggle.parentElement.classList.toggle('open');
            }
        });
    });

});



    // --- MOBILE MENU TOGGLE ---
    const menuToggle = document.getElementById('menu-toggle-btn');
    const navMenu = document.getElementById('nav-menu-list');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            
            // Toggle hamburger animation state
            const spans = menuToggle.querySelectorAll('span');
            if (menuToggle.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(6px, -6px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }
});
