$(window).scroll(function () {
    if ($(this).scrollTop() > 500) {
        $('#navBar').fadeOut(1500);
    } else {
        $('#navBar').fadeIn(500);
    }
});