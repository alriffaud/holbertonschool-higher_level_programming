// This script updates the text color of the header element to red (#FF0000)
// when the user clicks on the tag with id red_header.
function changeColor () {
  const header = document.querySelector('header');
  header.style.color = '#FF0000';
}
const element = document.getElementById('red_header');
element.addEventListener('click', changeColor);
