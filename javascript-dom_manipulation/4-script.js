// This script adds a li element to a list
// when the user clicks on the element with id add_item.
function addsLi () {
  const myList = document.querySelector('.my_list');
  const newElement = document.createElement('li');
  newElement.textContent = 'Item';
  myList.appendChild(newElement);
}
const element = document.getElementById('add_item');
element.addEventListener('click', addsLi);
