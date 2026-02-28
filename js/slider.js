// JavaScript for image slider/carousel

class Slider {
  constructor(containerSelector, interval=3000) {
    this.container = document.querySelector(containerSelector);
    this.slides = this.container.querySelectorAll('.slide');
    this.currentIndex = 0;
    this.interval = interval;
    this.timer = null;

    this.init();
  }

  init() {
    this.showSlide(this.currentIndex);
    this.startTimer();

    // Optional - add next/prev buttons if present
    const nextBtn = this.container.querySelector('.next');
    const prevBtn = this.container.querySelector('.prev');

    if(nextBtn) nextBtn.addEventListener('click', () => this.nextSlide());
    if(prevBtn) prevBtn.addEventListener('click', () => this.prevSlide());

    this.container.addEventListener('mouseenter', () => this.pauseTimer());
    this.container.addEventListener('mouseleave', () => this.startTimer());
  }

  showSlide(index) {
    this.slides.forEach(slide => slide.classList.remove('active'));
    this.slides[index].classList.add('active');
  }

  nextSlide() {
    this.currentIndex = (this.currentIndex + 1) % this.slides.length;
    this.showSlide(this.currentIndex);
  }

  prevSlide() {
    this.currentIndex = (this.currentIndex - 1 + this.slides.length) % this.slides.length;
    this.showSlide(this.currentIndex);
  }

  startTimer() {
    this.timer = setInterval(() => this.nextSlide(), this.interval);
  }

  pauseTimer() {
    clearInterval(this.timer);
  }
}

// Usage example (commented out, add to your initialization script):
// new Slider('.slider-container', 5000);
