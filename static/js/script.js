$(document).ready(function(){
    $('.sidenav').sidenav( {edge: "right"});
});


// Verify Password Code, Obtained from [1] in readme acknowledgements.
$("#pwconfirm").on("keyup", function (e) {
    if ($("#password").val() != $(this).val()) {
        $(this).removeClass("valid").addClass("invalid");
    } else {
        $(this).removeClass("invalid").addClass("valid");
    }
});


// function that will open the youtube video in the modal and autoplay it. The setting src of the iframe was used from [3] in readme file.
$('.modal-trigger').on("click", function() { 
    var theModal = $(this).data( "target" ),
    videoSRC = $(this).attr( "data-theVideo" ), 
    videoSRCauto = videoSRC+"?autoplay=1" ;
    $('#' +theModal+' iframe').attr('src', videoSRCauto);
    $('#' +theModal+' .modal-close').click(function () {
        $('#' + theModal+' iframe').attr('src', videoSRC);
    });
    $('#' + theModal).modal();
})