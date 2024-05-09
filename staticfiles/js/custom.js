// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

const alert = document.querySelector(".message_alert");
function closeAlert() {
    alert.classList.add("close");
}
setTimeout(closeAlert, 4000) 

getYear();


// script.js 
const myBtn = document.querySelector(".uparrow")

window.addEventListener("scroll", () => {
    if(document.documentElement.scrollTop > 120) {
        myBtn.classList.add("show")
    } else {
        myBtn.classList.remove("show")  
    }
    console.log(document.documentElement.scrollTop);
}) 

$('.custom_slick_slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    fade: true,
    adaptiveHeight: true,
    asNavFor: '.slick_slider_nav',
    responsive: [{
        breakpoint: 768,
        settings: {
            dots: false
        }
    }]
})

$('.slick_slider_nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.custom_slick_slider',
    centerMode: false,
    focusOnSelect: true,
    variableWidth: true
});


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}