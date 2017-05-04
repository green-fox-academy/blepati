//replace the list items' content with items from this list:
var contentList = ['apple', 'banana', 'cat', 'dog'];

var contentPlace = document.getElementsByTagName('li');
function fillCont() {
  for (var item in contentPlace) {
    contentPlace[item].innerHTML = contentList[item];
  }
}

fillCont();
