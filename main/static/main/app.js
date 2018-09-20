let images = [
  "images/0.jpg",
  "images/1.jpg",
  "images/2.jpg",
  "images/3.jpg",
  "images/4.jpg",
  "images/5.jpg"
  ];

let num = 0;

function next() {
  num++;
  if(num >= images.length) {
    num = 0;
  }
  $("body").css("background", "url(\"" + images[num]+ "\") no-repeat");
}

function prev() {
  num--;
  if(num < 0) {
    num = images.length - 1;
  }
  $("body").css("background", "url(\"" + images[num]+ "\") no-repeat");
}
