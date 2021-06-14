$(document).ready(function(){
    $('.sidenav').sidenav( {edge: "right"});
});

// Obtained from [1] in readme acknowledgements.
$("#pwconfirm").on("keyup", function (e) {
    if ($("#password").val() != $(this).val()) {
        $(this).removeClass("valid").addClass("invalid");
    } else {
        $(this).removeClass("invalid").addClass("valid");
    }
});