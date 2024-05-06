// This script toggles the class of the header element
// when the user clicks on the tag with id toggle_header.
function toggleClass () {
  const header = document.querySelector('header');
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.add('red');
  }
}
const element = document.getElementById('toggle_header');
element.addEventListener('click', toggleClass);
