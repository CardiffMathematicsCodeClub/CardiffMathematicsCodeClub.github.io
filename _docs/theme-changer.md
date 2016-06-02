---
layout: page
title: Theme Changer
---

This page explains how the theme changer is implemented as well as trying to
provide some commentary as to why certain descisions or approaches were made. It
does _NOT_ explain how these themes are made. The only thing this page cares
about is that there is a `css/` folder containing a number of themes.

The creation of themes is a different matter entirely. There will be a link here
to how the themes are actually made when the documentation for it has been
written.

## The General Idea

As you probably know webpages are styled using CSS and that these styles are
usually stored in a seperate file. To apply these styles to a webpage you need
to tell the browser to load the corresponding stylesheet, this is usually done
in the `<head>` section of the HMTL as follows:

```html
<head>
    <!-- Other head items go here -->
    
    <link rel="stylesheet" href="/path/to/file.css">
</head>
```

You change the filepath in the `href` attribute, you change the styles which get
applied to the webpage and hence the theme. Ultimately the theme changer boils
down to just changing this attribute the rest is to add a few things to make the
user's experience more enjoyable.

The theme changer is built using a few lines of Javascript which swaps out the
filepath in the `href` attribute based on a choice from the user. The user's
choice is collected using a dropdown menu which is written using HTML that we
generate with Jekyll.

## The HTML

While there are many ways to collect information from a user, radio buttons,
checkboxes, text fields the list goes on. The most obvious choice for our case
here is a dropdown menu which when clicked on will display a list of valid
choices for the user to pick from. The HTML for a dropdown menu is as follows:

```html
<select>
  <option value="theme1">Theme 1's Name</option>
  <option value="theme2">Theme 2's Name</option>
  ...
</select>
```

Each `value` attribute will be the filename of the CSS file containing that
theme (without the extension). So we just need to write this inserting the
correct theme and file names.

We could do it by hand, it doesn't seem like much does it? At the time of
writing there are currently 11 themes on the site, so that would amount to 13
lines of HTML we could easily write that by hand. But what happens when a theme
maker adds a new theme to the site? Are we going to come back everytime to edit
the HTML and add the option in?

Or perhaps we could get the theme maker to add it themselves, after all it will
only be a single line? However neither of these seems ideal, someone might
forget to add it, leaving the theme unaccessible until someone notices and adds
it. Or say we decide at some point down the line to change the dropdown to radio
buttons, are we going to force all theme makers to relearn how they add themes
to the site because we decide on something "better"?

### Introducing _data/

Instead we will get Jekyll to automatically write this HTML for us when it
generates the site. That way no one will ever forget to add everything needed
for a new theme and (assuming we set it up correctly) even if we change from say
a dropdown to radio buttons the theme makers won't notice anything different.

We do however need some information from the theme makers about their theme.
Namely what is it called and what file is it in? Thankfully Jekyll provides us
with the perfect way to store and retrieve this data, the `_data/` folder.

Essentially in this folder you can store data in a number of formats including
[YAML][yaml] which we will be using here. This data is then accesible in your
website's templates via `site.data.<filename>`. If you are interested you can
find more information about the `_data` folder [here][jekyll-data]

So go ahead and open `_data/themes.yml` in your copy of the project, or if you
don't have a copy you can find it [here][theme-data]. In this file is all the
data for each of the themes we currently have 'installed' on the website. Let's
look at the entry for the website's current default theme `Cardiff Red`:

```yaml
- name:      Cardiff Red
  shortname: cardiffred
  version:   0.5
  author:    Alex

```

So that's all the data a theme maker needs to provide to have their theme added
to the website, its `name`, its filename (`shortname`), the `author` and a
somewhat arbitrary `version` number. Also see the dash (`-`) before the name,
that means this entry is part of a list and it allows us to loop over all themes
in the file in our template. 

### Writing the Template Code

_Note:_ This page assumes you already know how Jekyll and templates work, a link
will be added here once the docs for that have been written.

Now that we have all the data we need, it's relatively easy to go ahead and
write the template code. We want the user to be able to change the theme
anywhere on the website so we add it to the site's footer.

Items in the dropdown appear in the order there are added, so it's a good idea
to sort the themes alphabetically. The following snippet pulls out all the
themes from `_data/themes.yml`, sorts them alphabetically and then stores the
result in a variable called `themes`:

```liquid
{% raw %}{% assign themes = site.data.themes | sort: 'name' %}{% endraw %}
```

Now that we have the themes in place it's simply a matter of looping through
each theme and putting its name and filename into the correct places in the HTML:

```html
{% raw %}<select id="theme-chooser">
  {% for theme in themes %}
    <option value="{{theme.shortname}}">{{theme.name}}</option>
  {% endfor %}
</select>{% endraw %}
```

We give the dropdown an id name so that we can find it easily in our javascript
later.

That's all we need to have a functional theme changer, but what about the other
information we collected from the theme makers? Wouldn't it be good to credit
the theme maker when their theme is being shown?

So just before we jump over to the Javascript let's quickly add some information
about the theme to the footer as well.

```html
{%raw%}{% for theme in site.data.themes %}
  <div id="{{theme.shortname}}">
    <p>Theme: {{theme.name}} v{{theme.version}}</p>
    <p>Made by: {{theme.author}}</p>
  </div>
{% endfor %}{%endraw%}
```

Now I know what you're thinking, won't that display the information about all
the themes all the time? Well, yes it will but don't worry too much as we'll fix
that in the Javascript.

You can see all of the above template code in context by opening
`_includes/footer.html` in your copy of the project, or if you haven't got a
copy of the project you can see the whole file [here][footer-html]

## The Javascript

So currently our theme changer looks something like this:

![Theme Changer sans Javascript][changer-nojs]

You can see the details of all the themes in the left column and on the right is
the dropdown menu. Now without any Javascript choosing items in the dropdown has
no effect, so it's time we actually made our theme changer.. well change themes.

To do this we use a very popular Javascript library called [jQuery][jquery]. Now
I won't go into too much detail here, but jQuery makes interacting and
manipulating elements of a webpage really easy. 

Using the library boils down to issuing commands with the following format:

```javascript
$(<selector>).<do stuff>;
```

where `<selector>` is any valid [CSS Selector][css-selectors] and `<do stuff>`
can be anything from show/hiding that element, to animating color changes on
buttons to _completely rewriting the HTML that makes up the page_. 

If you don't know what CSS Selectors are then I recommend you go and follow the
link above and quickly read up on them. While you can probably understand what
follows if you don't, it will certainly help if you do. As a quick test, if you
know what the following selectors would select on a webpage then you should have
no problems with what we will be using soon:

- `p`, `div`, `link` and `select`
- `p.quote`
- `p#martha`
- `p.quote#martha`

Our theme changer is essentially a single function that is run once as the
webpage loads. So in `/js/theme-changer.js` we start off with the following:

```javascript
$(document).ready(function () {
    // Our code goes here
});
```

Which says to the browser when the webpage (`document`) has finished loading
(`ready`) run this function.

### Responding to Input

The most important aspect of the theme changer is that when the user makes a
choice in the dropdown menu, the webpage responds and loads the new theme.
Thankfully jQuery provides us with the `change` event which allows us to
register a function that we want it to run every time the value is changed.

```javascript
$("select#themechooser").change(function () {

    var new_theme = $("select#themechooser").val();
    changeTheme(new_theme);
})
```

So we simply get the current selection in the dropdown using the `val()`
function and we pass it to a function `changeTheme` (which we have to write) to
say theme we want the page to change to.

Just to remind you `new_theme` is the filename of the css file containing the
new theme without the css extension.

### Changing the Theme

Here is where the "magic" happens, to change a theme on the website we need to
do the following:

- Change the `href` attribute in the `<head>` section of the page, as we
  discussed above.
- Show the correct information snippet about the theme in the footer.
- Ensure the value in the dropdown matches the current theme.

Thankfully jQuery allows us to do all this in a few short lines:

```javascript
var changeTheme = function(shortname) {

    $("link#theme-def").attr("href", "/css/" + shortname + ".css");
```

Since all the themes are stored in the same folder (`/css`) and have the same
extension (`.css`) it's realtively easy to construct the correct filepath to the
theme using just its name. Next we hide all the theme information blocks.

```javascript
    $("div.themes").hide();
```

Then we unhide the block for the new theme

```javascript
    $("div.themes#" + shortname).show();
```

Finally force the dropdown to display the correct value

```javascript
    $("select#theme-chooser").val(shortname);
};
```

### Remebering the Choice

If we left it as it stands, we would know have a functioning theme chnager. The
user is able to make a choice and the webpage would respond and load the new
theme. However this change would be lost whenver the user goes to a new page on
the website or even refreshes the current one. 

Somehow we need to get the browser to remember this choice and automatically
apply it whenever it loads a new page. Fortunately most modern browsers provide
a feature called [Local Storage][local-storage] which allows us to save a small
amount of information to a user's machine for us to use later - such as the name
of a theme.

Again I won't go into too much detail here but keep the following in mind when
using local storage:

- Storage is isolated between domains and protocols i.e a page on
  `http://website.com` _cannot_ access data from `https://website.com` or any
  other site for that matter.
- Storage is done as key-value pairs, only strings can be saved.
- Storage size is at the user's discretion and can be disabled completely! But
  the default for most browsers appears to be between 5-10MB.
  
So as well as defining our `changeTheme` function and setting up the callbacks
we need to see if there is a saved preference that we need to load. If there
isn't then we'll just apply the default theme (currently `Cardiff Red`). Local
storage is accessed through the `localStorage` object.

``` javascript
if (localStorage.theme) {
    changeTheme(localStorage.theme);
} else {
    changeTheme("cardiffred");
}
```

But where does this `theme` attribute come from? Well, we need to go back to our
`changeTheme` function and set it when we switch to a new theme. We also need to
make sure we check that the localStorage feature is supported before we try and
use it.

``` javascript
if (typeof(Storage) !== undefined) {
    localStorage.setItem("theme", shortname);
}
```

That's it! We now have a fully functioning theme changer that even remembers
your choice and applies it when you return even if it's days since you last
visited the site (provided you use the same browser on the same device as last
time).

You can view the full script in `/js/theme-changer.js` in your copy of the
project or if you don't have a copy you can find it [here][theme-changer-js] 

[changer-nojs]:     /res/doc_pics/theme-changer-nojs.png
[css-selectors]:    http://www.w3schools.com/cssref/css_selectors.asp
[footer-html]:      https://github.com/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io/blob/master/_includes/footer.html
[jekyll-data]:      https://jekyllrb.com/docs/datafiles/
[jquery]:           https://jquery.com/
[local-storage]:    http://www.w3schools.com/html/html5_webstorage.asp
[theme-changer-js]: https://github.com/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io/blob/master/js/theme-changer.js
[theme-data]:       https://github.com/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io/blob/master/_data/themes.yml
[yaml]:             http://yaml.org/



