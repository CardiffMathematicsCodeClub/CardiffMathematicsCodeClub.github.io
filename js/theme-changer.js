$(document).ready(function () {


    // Hopefully so that the code is easier to follow we define our selectors
    // now
    var stylesheet = "link#theme-def";
    var themenames = "div.themes";
    var themechooser = "select#theme-chooser";

    // This function handles everything to do with changing the theme
    // including:
    //             - Changing the stylesheet
    //             - Updating the footer text
    //             - Updating the dropdown selection
    //             - If the facility is available, saving the user preference
    var changeTheme = function(shortname) {

	// Change the stylesheet
	$(stylesheet).attr("href", "/css/" + shortname + ".css");

	// Hide all theme details
	$(themenames).hide();

	// Unhide the relevant theme
	$(themenames + "#" + shortname).show();

	// Update the dropdown
	$(themechooser).val(shortname);

	// If local storage is available, save the theme so the change
	// is persistent both accross page loads and entire sessions
	if (typeof(Storage) !== undefined) {
	    localStorage.setItem("theme", shortname);
	}
    };

    // In case there already is a saved preference, load that theme
    // otherwise load the default
    if (localStorage.theme) {
	changeTheme(localStorage.theme);
    } else {
	changeTheme("main");
    }

    // Finally this code is only run when the user makes a choice using the
    // dropdown in the footer
    $(themechooser).change(function() {

	var new_theme = $(themechooser).val();
	changeTheme(new_theme);

    });
});
