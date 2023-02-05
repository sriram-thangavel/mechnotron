const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');

        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

const hiddenElements1 = document.querySelectorAll('.hidden1');
hiddenElements1.forEach((el) => observer.observe(el));


const observer1 = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const count1 = entry.target.querySelector('.hero__counts--count-1');
    //   const count2 = entry.target.querySelector('.hero__counts--count-2 span');
    //   const count3 = entry.target.querySelector('.hero__counts--count-3 span');
    //   const count4 = entry.target.querySelector('.hero__counts--count-4 span');
  
      if (entry.isIntersecting) {
        count1.classList.add('hero__counts--count-1-animated');
        // count2.classList.add('hero__counts--count-2-animated');
        // count3.classList.add('hero__counts--count-3-animated');
        // count4.classList.add('hero__counts--count-4-animated');
        return; // if we added the class, exit the function
      }
  
      // We're not intersecting, so remove the class!
      count1.classList.remove('hero__counts--count-1-animated');
    //   count2.classList.remove('hero__counts--count-2-animated');
    //   count3.classList.remove('hero__counts--count-3-animated');
    //   count4.classList.remove('hero__counts--count-4-animated');
    });
  });
  
//   observer1.observe(document.querySelector('.hero__counts'));
const counterobjects = document.querySelectorAll('.hero__counts');
counterobjects.forEach((el) => observer1.observe(el));