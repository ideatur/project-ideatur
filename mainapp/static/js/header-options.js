$(window).scroll(function(){
    if($(this).scrollTop() > 1){
        $('header').addClass('header-fluid');
        $('header').removeClass('my-header')
    }
    else {
        $('header').removeClass('header-fluid')
        $('header').addClass('my-header')
    }
})