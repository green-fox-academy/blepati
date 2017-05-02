'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:

var height = 12;
var length = 33;
var width = 20;

var surface = 2 * ((height * length) + (length * width) + (width * height))
var volume = height * length * width

console.log('the surface is ' + surface)
console.log('the volume is ' + volume)
