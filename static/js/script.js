$(document).ready(function(){
    var oneWeekAgo = new Date();
    oneWeekAgo.setDate(oneWeekAgo.getDate() - 7);
    
    // Materialize Intialisation of Components
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
    $('.modal').modal({
        onCloseEnd(){
            $("#videoModal iframe").attr("src", $("#videoModal iframe").attr("src").replace("?autoplay=1", ''));
        }
    });
});

// Upon resizing the window this will update all the esports cards so they are the same height.
window.onresize = function(event) {
    resizeEpicCards();
    $('.carousel').carousel({
        indicators: true,
        numVisible: 5, 
    });
};

// Verify Password Code, Obtained from [1] in readme acknowledgements.
$("#pwconfirm").on("keyup", function (e) {
    if ($("#password").val() != $(this).val()) {
        $(this).removeClass("valid").addClass("invalid");
    } else {
        $(this).removeClass("invalid").addClass("valid");
    }
});


// Function will open the youtube video in the modal and autoplay it. The setting src of the iframe was used from [3] in readme file.
// Function will handle all modal popup types.
$(document).on("click", ".modal-trigger", function() {
    var theModal = $(this).data( "target" );

    if(theModal == "videoModal"){
        var videoSRC = $(this).attr( "data-video" ), 
        epicTitle = $(this).attr( "data-epic" ),
        videoSRCauto = videoSRC+"?autoplay=1" ;
        $("#vod-modal-title").html(epicTitle);
        $('#' +theModal+' iframe').attr('src', videoSRCauto);
        $('#' +theModal+' .modal-close').click(function () {
            $('#' + theModal+' iframe').attr('src', videoSRC);
        });
    }
    else if(theModal == "deleteEpicModal"){
        var epicTitle = $(this).attr( "data-epic" ),
        epicId = $(this).attr( "data-epic-id" ),
        htmlTitlePrefix = "Are you sure you want to delete the post:<br>",
        urlForDeleteTask = "/delete_epic/"+ epicId;
        $('#delete-epic-confirm-button').prop("href", urlForDeleteTask);
        $("#delete-epic-title").html(htmlTitlePrefix + epicTitle);
    }
    else if(theModal == "deleteEventModal"){
        var epicTitle = $(this).attr( "data-event" ),
        eventId = $(this).attr( "data-event-id" ),
        htmlTitlePrefix = "Are you sure you want to delete the event:<br>",
        urlForDeleteTask = "/delete_event/"+ eventId;
        $('#delete-event-confirm-button').prop("href", urlForDeleteTask);
        $("#delete-event-title").html(htmlTitlePrefix + epicTitle);
    }
    else if(theModal == "deleteNewsModal"){
        var storyTitle = $(this).attr( "data-story" ),
        storyId = $(this).attr( "data-story-id" ),
        htmlTitlePrefix = "Are you sure you want to delete the news post:<br>",
        urlForDeleteTask = "/delete_news/"+ storyId;
        $('#delete-news-confirm-button').prop("href", urlForDeleteTask);
        $("#delete-news-title").html(htmlTitlePrefix + storyTitle);
    }
    else if(theModal == "deleteUserModal"){
        var userId = $(this).attr( "data-user-id" ),
        htmlTitlePrefix = "Are you sure you want to delete your account?",
        urlForDeleteTask = "/delete_user/"+ userId;
        $('#delete-user-confirm-button').prop("href", urlForDeleteTask);
        $("#delete-user-title").html(htmlTitlePrefix);
    }
});

// Function makes esports cards same height.
function resizeEpicCards() {
    var maxHeight = 0;

    $('.epic-image').each(function() {
        $(this).find('.epic-image').height($(this).find('.epic-image').width());    
    });

    $('.epic-card').each(function() {
        $(this).find('.epic-image').height($(this).find('.epic-image').width());    
        $(this).height('auto');
    });
    $('.epic-card').each(function() {
        var height = $(this).height();
        if(height > maxHeight){
            maxHeight = height;
        }
    });
    $('.epic-card').each(function() {
        $(this).height(maxHeight);
    });
}

// loader obtained from [18] in readme acknowledgements
$(window).on('load', function(){
    $(".se-pre-con").fadeOut();
    $(".site-content").show();
    $('.carousel').carousel({
        indicators: true,
        numVisible: 5, 
    });
    resizeEpicCards();
 });