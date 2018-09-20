let images = [
  "main/images/0.jpg",
  "main/images/1.jpg",
  "main/images/2.jpg",
  "main/images/3.jpg",
  "main/images/4.jpg",
  "main/images/5.jpg"
  ];

let num = 0;

function next() {
  num++;
  if(num >= images.length) {
    num = 0;
  }
  $("body").css("background", "url('/static/" + images[num]+ "') no-repeat");
}

function prev() {
  num--;
  if(num < 0) {
    num = images.length - 1;
  }
  $("body").css("background", "url('/static/" + images[num]+ "') no-repeat");
}

//{% static 'main/app.js' %}

//$("body").css("background", "url('" + images[num]+ "') no-repeat");
