function titleText (el) {
    el.classList.add('tracking-in-expand-fwd');
}



ScrollReveal().reveal('.hero__counts',{ beforeReveal: titleText});
ScrollReveal().reveal('.about_achievements__about--title',{ beforeReveal: titleText});
ScrollReveal().reveal('.about_achievements__achievements--title',{ beforeReveal: titleText});
ScrollReveal().reveal('.events__title',{ beforeReveal: titleText});
ScrollReveal().reveal('.events__technical--more-text',{ beforeReveal: titleText});
ScrollReveal().reveal('.events__non-technical--more-text',{ beforeReveal: titleText});
ScrollReveal().reveal('.workshop__title',{ beforeReveal: titleText});
ScrollReveal().reveal('.webinar__title',{ beforeReveal: titleText});



ScrollReveal().reveal('.about_achievements__about--discription-wrapper', { delay: 400 });;
ScrollReveal().reveal('.about_achievements__achievements--discription-wrapper', { delay: 400 });
ScrollReveal().reveal('.events__cards--card', { delay: 400 });
ScrollReveal().reveal('.workshop__cards--card', { delay: 400 });
ScrollReveal().reveal('.webinar__cards--card', { delay: 400 });
