#!/usr/bin/node

const request = require('request');
const { argv } = require('process');
const url = argv[2];

const completedTasks = (body) => {
  const tasks = {

  };
  data = JSON.parse(body);
  for (const obj in data) {
    if (data[obj].completed) {
      if (tasks[data[obj].userId]) {
        tasks[data[obj].userId] += 1;
      } else {
        tasks[data[obj].userId] = 1;
      }
    }
  }
  return tasks;
};
request(url, (error, response, body) => {
  if (error) throw error;
  const tasks = completedTasks(body);
  console.log(tasks);
});
