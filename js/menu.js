$(document).ready(function() {


    // This makes the menu show/hide when the menu name is clicked
    $(".menu-name").click(function () {
        $(".menu-item").slideToggle("slow");
    });


    // This function handles everything we need for a responsive menu
    var responsiveMenu = function () {
        // Hide the "menu" item
        $(".menu-name").hide();
        $(".menu-item").show();

        // Unless of course we are on mobile in which case show it
        if ($(window).width() < 800) {
            $(".menu-name").show();

            // But instead hide the menu items
            $(".menu-item").hide();
        }
    };

    // We pass this function as handler for the 'resize' event so that
    // the menu is recalibrated each time the window changes size
    $(window).resize(responsiveMenu);

    // Also call the function once to handle the initial setup of the window
    responsiveMenu();
});
