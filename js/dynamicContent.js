// JavaScript for dynamic content loading

document.addEventListener('DOMContentLoaded', () => {
  const loadButton = document.getElementById('load-more-content');
  const contentContainer = document.getElementById('dynamic-content');

  if(loadButton && contentContainer) {
    loadButton.addEventListener('click', () => {
      fetch('more-content.html')
        .then(response => {
          if (!response.ok) throw new Error('Network response was not ok');
          return response.text();
        })
        .then(html => {
          contentContainer.insertAdjacentHTML('beforeend', html);
        })
        .catch(error => {
          console.error('Error loading content:', error);
        });
    });
  }
});
