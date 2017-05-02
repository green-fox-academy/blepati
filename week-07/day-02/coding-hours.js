'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

var codingHours = 6
var studyDays = 5
var studyWeeks = 17
var workingHours = 52

console.log(codingHours * studyDays * studyWeeks)
console.log(100/(workingHours / (codingHours * studyDays)))
