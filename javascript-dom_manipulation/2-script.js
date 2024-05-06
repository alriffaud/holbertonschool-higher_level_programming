// This script adds the class red to the header element
// when the user clicks on the tag with id red_header.
function addClass () {
  const header = document.querySelector('header');
  header.classList.add('red');
}
const element = document.getElementById('red_header');
element.addEventListener('click', addClass);
