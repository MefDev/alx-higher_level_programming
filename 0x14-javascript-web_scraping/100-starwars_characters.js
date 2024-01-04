#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const ID = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

const getMovieData = async (body) => {
  const currentMovieData = await JSON.parse(body);
  return currentMovieData;
};
const printCharacterName = async (movieData) => {
  const characters = await movieData.characters;
  for (const character of characters) {
    request(character, async (error, response, body) => {
      if (error) throw error;
      const currentCharacter = await JSON.parse(body);
      console.log(currentCharacter.name);
    });
  }
};
request(url, async (error, response, body) => {
  if (error) throw error;
  const movieData = await getMovieData(body);
  printCharacterName(movieData);
});
