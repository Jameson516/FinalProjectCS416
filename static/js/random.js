// Change Image Randomly
let images1 = ['News1.jpg', 'News2.jpg', 'News3.jpg'];
let images2 = ['Movies1.jpg', 'Movies2.jpg', 'Movies3.jpg'];
let images3 = ['Games1.jpg', 'Games2.jpg', 'Games3.jpg'];
let images4 = ['Health1.jpg', 'Health2.png', 'Health3.jpg'];
let images5 = ['Money1.jpg', 'Money2.jpg', 'Money3.jpg'];
let images6 = ['Art1.jpg', 'Art2.jpg', 'Art3.jpg'];

// const timer = setInterval(changeImage, 5000);

$('#random').click(changeImage);

function changeImage() {
    /**
    $('img').each(function (index, element) {
        $(element).attr("src", "../../static/images/"+ images[generateRandom()]);
    });
     **/
    $('#imgRand1').attr("src", "../../static/images/"+ images1[generateRandom1()]);
    $('#imgRand2').attr("src", "../../static/images/"+ images2[generateRandom2()]);
    $('#imgRand3').attr("src", "../../static/images/"+ images3[generateRandom3()]);
    $('#imgRand4').attr("src", "../../static/images/"+ images4[generateRandom4()]);
    $('#imgRand5').attr("src", "../../static/images/"+ images5[generateRandom5()]);
    $('#imgRand6').attr("src", "../../static/images/"+ images6[generateRandom6()]);

    // clearInterval(timer);
}

function generateRandom1() {
    return Math.floor(Math.random() * images1.length)
}

function generateRandom2() {
    return Math.floor(Math.random() * images2.length)
}

function generateRandom3() {
    return Math.floor(Math.random() * images3.length)
}

function generateRandom4() {
    return Math.floor(Math.random() * images4.length)
}

function generateRandom5() {
    return Math.floor(Math.random() * images5.length)
}

function generateRandom6() {
    return Math.floor(Math.random() * images6.length)
}

// window.setInterval("changeImage()",5000);

/**
//Add following inside script tag
//Add id to your image tag
let theImages = new Array();
theImages[0] = 'images/first.gif' // replace with names of images
theImages[1] = 'images/second.gif' // replace with names of images
theImages[2] = 'images/third.gif' // replace with names of images

let j = 0
let p = theImages.length;
let preBuffer = new Array();

for (let i = 0; i < p; i++){
    preBuffer[i] = new Image();
    preBuffer[i].src = theImages[i];
}
let whichImage = Math.round(Math.random()*(p-1));

function showImage(){
    document.getElementById("imgRand").src = theImages[whichImage];
}

//call the function
showImage();
 **/