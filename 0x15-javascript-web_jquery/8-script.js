$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (movies) {
    for (const movie of movies.results) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  }
);
