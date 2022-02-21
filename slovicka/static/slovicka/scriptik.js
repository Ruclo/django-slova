function schovat() {
var checkBox = document.getElementById("checkboxik")
var hotovedivy = document.getElementsByClassName('hotove')
console.log(checkBox)
console.log(hotovedivy)
if (checkBox.checked == true) {
for(var i = 0; i<hotovedivy.length; i++) {
hotovedivy[i].style.display = 'none';
}
} else {
for(var i = 0; i<hotovedivy.length; i++) {
hotovedivy[i].style.display = 'block';
}
}

}