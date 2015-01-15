---
layout     : post
title      : "Making an App in python using Kivy - Part 1"
categories : website python kivy
tags       : blog
author     : Timothy
comments   : false
---

In the summer semester for the Computing for Mathematics module we were required to create 'companies' of 4. 
The goal was for each company to create a 'product' which involes programming and mathematics. 
For this my company decided to make an mobile app, to aid with learning mathematics through giving content and quiz. 

Once we have decided to make the app I looked at varies [GUI frameworks](https://wiki.python.org/moin/GuiProgramming) based on python which we could use.
From this list we decided that [Kivy](http://kivy.org/) would be best suited for what we required. 

## Creating a basic Kivy app

Below is the code for a basic app that has the label of 'Hello World'. 

{% gist timothyf1/75b20064a50e51651efa %}

The output is rather simple

![Hello World]({{site.baseurl}}/blog/static/images/kivy-hello-world.png)

## Kv Language

Kivy uses it's own [Kv Language](http://kivy.org/docs/guide/lang.html) in order to create widget trees. 
When testing out different layouts using the Kv language makes it easier for you to experment with different widgets. 

For example the equilevent of the Hello World using KV from above is.


Depending on your needs you can do either of the following:

- Just use python code and ignore the KV lang. 
- Mix python code and KV lang for layouts. 
- Use KV lang for all layouts. 

I found this useful to only use the python code as I was building the layout depended on how many items there were in a database.

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

