//Write the image's url to the console.
//Replace the image with a picture of yourself.
//Make the link point to the Green Fox Academy website.
//Disable the second button.
//Replace its text with 'Don't click me!'.

var imageLink = document.querySelector('img');
console.log(imageLink.getAttribute('src'));
imageLink.setAttribute('src', 'http://placehold.it/200x200');

var pageLink = document.querySelector('a');
pageLink.getAttribute('href');
pageLink.setAttribute('href', 'https://www.greenfoxacademy.com/');

var disButton = document.querySelector('.this-one');
disButton.setAttribute('disabled', 'disabled');
disButton.innerHTML = "Don't click me!";
