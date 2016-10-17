var blue = document.getElementById("landing");
var orange = ["url(../img/sizandI.jpg)", "url(../img/pastlove.jpg", "url(../img/pic.jpg)", "url(../img/myroots.jpg)", "url(../img/closefriends.jpg)", "url(../img/christmaspic.jpg)"];
var counter = 0;

function slider() {
    blue.style.backgroundImage = orange[counter];
    counter++;

    if (counter >= orange.length) {
        counter = 0;
    }
}
setInterval(slider, 3000);
