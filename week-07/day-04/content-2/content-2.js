 //fill every paragraph with the last one's content.

var lastPar = document.getElementsByClassName('dog');

var changePar = document.getElementsByTagName('p');

function changeCont() {
  for (var par in changePar) {
    changePar[par].innerHTML = lastPar[0].textContent;
  };
};

changeCont();
