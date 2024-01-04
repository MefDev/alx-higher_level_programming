#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const ID = argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${ID}`;

const getMovieData = async (body) => {
  return JSON.parse(body);
};

const getActorNames = async (characters) => {
  const callPromises = characters.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, _, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  });
  return Promise.all(callPromises);
};

const getCharacterNames = async (movieData) => {
  const characters = movieData.characters;
  const actorNames = await getActorNames(characters);
  return actorNames;
};

const printCharacterNames = () => {
  request(url, async (error, response, body) => {
    if (error) throw error;
    const movieData = await getMovieData(body);
    const characterNames = await getCharacterNames(movieData);
    characterNames.forEach(character => {
      console.log(character.name);
    });
  });
};

printCharacterNames();
