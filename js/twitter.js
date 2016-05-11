$(document).ready(function() {

    var tab = "div.sidetab";
    var feed = "div.tweets"

    var toggleDrawer = function() {

        if ($(tab).hasClass("toggled")) {

            // Start hiding the twitter feed
            $(feed).hide("slow");

            // Since tab is also open, close it
            $(tab).animate({"bottom": "0"}, "slow", "swing");

            // Remove the class
            $(tab).removeClass("toggled");
        } else {

            // Show the feed
            $(feed).show("slow");

            // Open the tab
            $(tab).animate({"bottom": "610px"}, "slow", "swing");

            // Add the class to indicate it's open
            $(tab).addClass("toggled");
        }
    };

    $("div.sidetab").click(toggleDrawer);
})
