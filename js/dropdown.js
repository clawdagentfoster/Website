// JavaScript for dropdown menus

document.addEventListener('DOMContentLoaded', () => {
  const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
  dropdownToggles.forEach(toggle => {
    toggle.addEventListener('click', (event) => {
      event.preventDefault();
      const dropdownMenu = toggle.nextElementSibling;
      dropdownMenu.classList.toggle('show');
    });
  });

  // Close dropdown if clicking outside
  document.addEventListener('click', (event) => {
    dropdownToggles.forEach(toggle => {
      const dropdownMenu = toggle.nextElementSibling;
      if (!toggle.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.remove('show');
      }
    });
  });
});
