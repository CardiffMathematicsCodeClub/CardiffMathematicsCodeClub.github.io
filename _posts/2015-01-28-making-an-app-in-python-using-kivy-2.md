---
layout     : post
title      : "Making an App in python using Kivy - Part 2 - Widgets"
categories : blog kivy
tags       : blog
author     : Timothy
comments   : false
---

In the [first part]({% post_url 2015-01-16-making-an-app-in-python-using-kivy-1 %}) I talked about how to create an app. 
Now I'm going to talk about the some of different widgets that can be used in Kivy, that I found helpful.

## Widgets

In Kivy widgets are the building blocks of the GUI interface, which we created for our app. 
The main app takes 1 widget, as the root widget, when built. 

Kivy includes examples of how to use each of the widgets. 
I would recommend looking through these to identify the best widget to use for each element of the app. 

In the [Hello World example](https://gist.github.com/timothyf1/75b20064a50e51651efa) from part 1 we see that on line 5 I imported the label widget, so that it can be used in line 11 to create an label. 
For each widget you want to use it is needed to be imported.

### Screen Manager 

In most apps you will require a different layout for each type of page. 
For this I would recommend using the [screen manager](http://kivy.org/docs/api-kivy.uix.screenmanager.html), 
although there are other options such as [carousel](http://kivy.org/docs/api-kivy.uix.carousel.html) depending on your needs.

Below is a sample of the different screens we used in our group last year. 

![Screen Manager]({{site.baseurl}}/blog/static/images/kivy-screen-manager.png)

Note that the screen manager doesn't need to be the root widget leading to the whole screen changing.
For example you can have a vertical boxlayout (layouts are explained next), with an header as the first widget and the screen manager as the second.

{% gist 1f51fc7cdcf9b7a12694 screenmanager.py %}

The KV code can be found [here](https://gist.github.com/timothyf1/1f51fc7cdcf9b7a12694#file-screenmanager-kv)

Here we making the screen manager the root widget with there being 4 screens added to the manager. 
Each of the screens are similar with a different background colour and number. 

If we take a look at the code for the next button in the KV we have

{% gist 72af082e37599e19887d NextButton %}

- Text is the text that is displayed on the button
- size_hint is used by default to decide on how big a widget will be, it defaults to (1, 1).
- pos_hint 
- size is how big the button is, note that if size_hint isn't set to (None, None) then this doesn't have an effect.
- on_release is the action that occurs once a user has click on and released the button. 

Lets take a closer look at what on_release is doing.
Firstly root refers to the custom screen as looking in the KV code it comes under _CustomScreen_.
Next we are referring to the [manager attribute](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.Screen.manager) of the screen which gives us the screen manager it's attached to. 
We are then setting the [current attribute](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.current) of the screen manager to change the screen. 

Now to see what it's being set to we see that it follows the root.manager again. 
But this time we are using the [next method](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.next) of the screen manager to get the name of next screen.
The next method looks at the [screen_names](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.screen_names), which is a list the screens added to the screen manager. 
The order in which next() and similarly [previous()](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.previous) works is based upon the order that the screens were added to the screen manager. 

#### Transitions

We also see that in the above example there are multiple transitions. 
The transitions are changed by changing the screen managers [transition attribute](http://kivy.org/docs/api-kivy.uix.screenmanager.html#kivy.uix.screenmanager.ScreenManager.transition). 

### Layouts 

In order to have multiple widgets there are layout out widgets that allow multiple widgets to be attached to it. 

There are 6 different [layout widgets](http://kivy.org/docs/guide/widgets.html#organize-with-layouts) in kivy.

- [BoxLayout](http://kivy.org/docs/api-kivy.uix.boxlayout.html)
- [GridLayout](http://kivy.org/docs/api-kivy.uix.gridlayout.html)
- [StackLayout](http://kivy.org/docs/api-kivy.uix.scatterlayout.html)
- [AnchorLayout](http://kivy.org/docs/api-kivy.uix.anchorlayout.html)
- [FloatLayout](http://kivy.org/docs/api-kivy.uix.floatlayout.html)
- [RelativeLayout](http://kivy.org/docs/api-kivy.uix.relativelayout.html)

Of the different layouts in our we used boxlayout the most and grid for tables. 

In the boxlayout example from part 1, [code can be found here](https://gist.github.com/timothyf1/adeb2eaa141ac4314981).
We note that size hinting was used here but what does it do?

In the screen manager example we see that just size_hint was used. 
This took 2 values the first for the x direction and then for the y direction.
But in the Boxlayout example they are changed separately.

So for the first block pictured below, it is a vertical boxlayout.

![]({{site.baseurl}}/blog/static/images/kivy-boxlayout-example-1.png)

We see that the size_hint_y hasn't been changed so virtually each button is taking up a third of the available space.
What has been changed is the size_hint_x, so the first and the last buttons are only 40% of the available width that they were given.
The second button is given 20% of the width. 
Due to the positioning of each button means that they don't overlap.
