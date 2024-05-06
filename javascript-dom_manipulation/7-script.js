// This script fetches and lists the title for all movies by using this URL:
// https://swapi-api.hbtn.io/api/films/?format=json
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const element = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const newElement = document.createElement('li');
      newElement.textContent = movie.title;
      element.appendChild(newElement);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
