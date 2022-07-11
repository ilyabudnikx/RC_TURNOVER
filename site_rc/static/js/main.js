// window.onload = function () {
//     document.body.classList.add('loaded_hiding');
//     window.setTimeout(function () {
//         document.body.classList.add('loaded');
//         document.body.classList.remove('loaded_hiding');
//     }, 500);
// }

// window.onload = function () {
//     const anim = lottie;
//     anim.loadAnimation({
//         container: document.querySelector('#lottie_preload'),
//         renderer: 'svg',
//         loop: true,
//         autoplay: true,
//         path: './js/lottie_animation.json',
//     });
//     window.setTimeout(function () {
//         document.body.classList.add('loaded_hiding');
//         typeWriter();
//         // document.getElementsByClassName('preloader')[0].remove();
//     }, 2500);
//     window.setTimeout(function () {
//         document.getElementsByClassName('preloader')[0].remove() }, 2700);
// }

$('.div_menu').hide();
$('#category').click(function() {
    if ($('.div_menu').is(':visible')){
        $('.div_menu').hide();
    } else {
        $('.div_menu').show();
    }
});

if (document.getElementById('country')){
    $('#country').change(function() {
        if ($('#country').val() == 'off') {
            $('#city').attr("disabled", true);
        } else {
            $('#city').attr("disabled", false);
        }
    });
}