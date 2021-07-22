$(document).ready(function(){
    var oneWeekAgo = new Date();
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
    $('.sidenav').sidenav( {edge: "right"});
    $('.carousel').carousel({
        indicators: true,
        numVisible: 5, 
    });
    $('.datepicker').datepicker({
        minDate: oneWeekAgo
    });
    $('.timepicker').timepicker();
    $("#flash-message-block").delay(2000).slideUp(300);
    $('.collapsible').collapsible();
    resizeEpicCards();
});

window.onresize = function(event) {
    resizeEpicCards();
};

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
    videoSRC = $(this).attr( "data-video" ), 
    epicTitle = $(this).attr( "data-epic" ),
    videoSRCauto = videoSRC+"?autoplay=1" ;
    $("#vod-modal-title").html(epicTitle)
    $('#' +theModal+' iframe').attr('src', videoSRCauto);
    $('#' +theModal+' .modal-close').click(function () {
        $('#' + theModal+' iframe').attr('src', videoSRC);
    });
    $('#' + theModal).modal();
})

function resizeEpicCards() {
    var maxHeight = 0
    $('.epic-card').each(function() {
        var height = $(this).height();
        if(height > maxHeight){
            maxHeight = height
        }
    });
    $('.epic-card').each(function() {
        var heightVodBtn = $(this).find('.vod-modal-btn').height();
        var heightDescription = $(this).find('.epic-description').height();
        $(this).find('.epic-image').height(maxHeight - heightDescription - heightVodBtn - 20 -  0.15*maxHeight);
        $(this).height(maxHeight);
    });

}