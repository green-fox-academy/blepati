//fill output1 with the first paragraph's content, text only.
//fill output2 with the first paragraph's content keeping the cat strong.

var basic = document.querySelectorAll('p');
var changeFirst = document.getElementsByClassName('output1');
var changeSec = document.getElementsByClassName('output2');
changeFirst[0].innerHTML = basic[0].textContent;
changeSec[0].innerHTML = basic[0].innerHTML;
