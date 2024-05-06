// This script fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
// displays the value of hello from that fetch in the HTML element with id hello.
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const element = document.getElementById('hello');
    element.textContent = data.hello;
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
