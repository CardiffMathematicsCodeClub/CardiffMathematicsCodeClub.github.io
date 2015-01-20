---
layout     : post
title      : "Making an App in python using Kivy - Part 2"
categories : website python kivy
tags       : blog
author     : Timothy
comments   : false
---

In the first part I talked about how to create an app. Now I'm going to talk about the different widgets.

## Widgets

In Kivy widgets are the building blocks of the GUI interface, which we created for our app. 
The main app takes 1 widget when built. 

Kivy includes examples of how to use each of the widgets. 
I would recommened looking through these to identify the best widget to use for each element of the app. 

In the above Hello World example we see that on line 5 I imported the label widget, so that it can be used in line 11 to create an label. 
For each widget you want to use it is needed to be imported. 

### Screen Manager 

In most apps you will require a different layout for each type of page. 
For this I would recommend using the [screen manager](http://kivy.org/docs/api-kivy.uix.screenmanager.html), 
although there are other options such as [carousel](http://kivy.org/docs/api-kivy.uix.carousel.html) depending on your needs.

Below is a sample of the different screens we used in our group last year. 

![Screen Manager]({{site.baseurl}}/blog/static/images/kivy-screen-manager.png)

Note that the screen manager doesn't need to change the wholescreen.
You can put an header at the top which stays the same and have the screen manager below for example.

### Layouts 

In order to have muiltiple widgets there are layout out widgets that allow muiltple widgets to be attached to it. 

There are 6 different [layout widgets](http://kivy.org/docs/guide/widgets.html#organize-with-layouts) in kivy.

- BoxLayout
- GridLayout
- StackLayout
- AnchorLayout
- FloatLayout
- RelativeLayout

Of the different layouts in our we used boxlayout the most and grid for tables. 

