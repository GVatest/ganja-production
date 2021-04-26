// widgets
var galaryPhoto = $('.galary-photo'),
    galaryVideo = $('.galary-video')
$('.photo-widget').on('click', function () {
    galaryPhoto.slideToggle()
    galaryVideo.slideUp()
})
$('.video-widget').on('click', function () {
        galaryPhoto.slideUp()
        galaryVideo.slideToggle()
})