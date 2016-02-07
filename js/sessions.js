$(document).ready(function() {

    // This controls the toggling of sessions by year
    $(".session-year > h4").click(function (){

        // Get the year that the user clicked on
        var year = $(this).attr("class");

        // Build the select query (don't forget to prepend the dot
        // which indicates a class in CSS
        $("." + year + " > .session-term").slideToggle("slow");
    });

    // This controls the toggling of sessions by term
    $(".session-term > h5").click(function () {

        // Get the term that was clicked on
        var classes = $(this).attr("class").split(" ");
        var term = "." + classes[0];
        var year = "." + classes[1];

        // Build the select query (don't forget to prepend the dot
        // which indicates a class in CSS)
        $("div.session-term" + year + term + " > ul").slideToggle("slow");
    });

    // This sets the default layout for the page
    $(".session-year > .session-term").hide();

});
