'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs:
// - how many candies are owned by students
function candyCounter() {
  var allCandy = 0;
  for (var key in students) {
    allCandy += students[key].candies;
  }
  return allCandy;
}

console.log(candyCounter())

// create a function that takes a list of students and logs:
// - Sum of the age of people who have less than 5 candies

function candyless() {
  var candylessKids = [];
  for (var key in students) {
    if (students[key].candies < 5) {
      candylessKids.push(students[key].name);
    }
  }
  return candylessKids;
}

console.log(candyless())
