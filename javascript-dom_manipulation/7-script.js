// 7-script.js
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movieList = document.getElementById('list_movies');
    data.results.forEach(film => {
      const li = document.createElement('li');
      li.textContent = film.title;
      movieList.appendChild(li);
    });
  });
