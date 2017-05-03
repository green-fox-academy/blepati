'use strict';
// - Create a variable named `p1`
//   with the following content: `[1, 2, 3]`
// - Create a variable named `p2`
//   with the following content: `[4, 5]`
// - Log to the console if `p2` has more elements than `p1`

var p1 = [1, 2, 3];
var p2 = [4, 5];

function compareArrays(ar1, ar2) {
  if (ar2.length > ar1.length) {
    return '`p2` has more elements than `p1`';
  } else if (ar2.length < ar1.length) {
    return '`p1` has more elements than `p2`';
  } else {
    return 'maybe they are empty or have the same amount of value'
  }
}

console.log(compareArrays(p1, p2))
