/*1. Alert the content of the heading.--
2. Write the content of the first paragraph to the console.--
3. Alert the content of the second paragraph.--
4. Replace the heading's content with 'New content'.--
5. Replace the last paragraph's content with the first paragraph's content*/

var alertContent = document.getElementsByTagName('h1');
//alert(alertContent[0].textContent);

var firstCont = document.getElementsByTagName('p');
console.log(firstCont[0].textContent);

var secAlert = document.getElementsByClassName('other');
//alert(secAlert[0].textContent);

alertContent[0].innerHTML = "New content";

var lastCont = document.getElementsByClassName('result');
lastCont[0].innerHTML = firstCont[0].textContent;
