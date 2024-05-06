// This script updates the text of the header element to New Header!!!
// when the user clicks on the tag with id the element with id update_header.
function updateText () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
}
const element = document.getElementById('update_header');
element.addEventListener('click', updateText);
