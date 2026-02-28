// JavaScript for modal pop-ups

document.addEventListener('DOMContentLoaded', () => {
  const modalTriggers = document.querySelectorAll('[data-modal-target]');
  const modals = document.querySelectorAll('.modal');
  const modalCloseButtons = document.querySelectorAll('.modal-close');

  modalTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const target = trigger.getAttribute('data-modal-target');
      const targetModal = document.getElementById(target);
      targetModal.classList.add('active');
    });
  });

  modalCloseButtons.forEach(button => {
    button.addEventListener('click', () => {
      const modal = button.closest('.modal');
      modal.classList.remove('active');
    });
  });

  // Close modals when clicking outside content
  modals.forEach(modal => {
    modal.addEventListener('click', (event) => {
      if(event.target === modal) {
        modal.classList.remove('active');
      }
    });
  });
});
