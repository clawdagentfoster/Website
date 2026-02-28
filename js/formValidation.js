// JavaScript for form validation

document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('form.validate');

  forms.forEach(form => {
    form.addEventListener('submit', (event) => {
      let valid = true;
      const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');

      inputs.forEach(input => {
        input.classList.remove('error');
        if (!input.value) {
          valid = false;
          input.classList.add('error');
        }
      });

      if (!valid) {
        event.preventDefault();
        const errorMsg = form.querySelector('.error-message');
        if (errorMsg) {
          errorMsg.textContent = 'Please fill in all required fields.';
          errorMsg.style.display = 'block';
        }
      }
    });
  });
});
