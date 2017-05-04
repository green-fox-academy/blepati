/*1. store the element that says 'The King' in the 'king' variable.
console.log it.
2. store the element that contains the text 'The Conceited Man'
in the 'conceited' variable.
show the result in an 'alert' window.
3. store 'The Businessman' and 'The Lamplighter'
in the 'businessLamp' variable.
console.log each of them.
4. store 'The King' and 'The Conceited Man'
in the 'conceitedKing' variable.
alert them one by one.
5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
in the 'noBusiness' variable.
console.log each of them.
6. store 'The Businessman' in the 'allBizniss' variable.
show the result in an 'alert' window.*/

var king = document.getElementById('b325');
console.log(king.textContent);

var conceited = document.querySelector('.b326');
alert(conceited.textContent);

var businessLamp = document.querySelectorAll('.big');
businessLamp.forEach(function(el, i) {
  console.log(businessLamp[i].textContent);
});

var conceitedKing = [];
conceitedKing.push(king);
conceitedKing.push(conceited);
conceitedKing.forEach(function(el, i) {
  alert(conceitedKing[i].textContent);
});

var noBusiness = [];
var lamp = document.querySelector('.b329');
noBusiness.push(king);
noBusiness.push(conceited);
noBusiness.push(lamp);
noBusiness.forEach(function(el, i) {
  console.log(noBusiness[i].textContent);
});

var allBizniss = businessLamp[0];
console.log(allBizniss.textContent);
