---
layout     : post
title      : "Making an App in python using Kivy - Part 1"
categories : website python kivy
tags       : blog
author     : Timothy
comments   : false
---

In the summer semester for the Computing for Mathematics module we were required to create 'companies' of 4. 
The goal was for us to create a 'product' which involes programming and mathematics. 
For this our company decided to make an mobile app, to aid with learning mathematics through giving content and quiz. 

Once we have decided to make the app I looked at varies [GUI frameworks](https://wiki.python.org/moin/GuiProgramming) based on python which we could use.
From this list we decided that [Kivy](http://kivy.org/) would be best suited for what we required. 

## Creating a basic Kivy app

Below is the code for a basic app that has the label of 'Hello World'. 

{% gist timothyf1/75b20064a50e51651efa %}

The output is rather simple

![Hello World]({{site.baseurl}}/blog/static/images/kivy-hello-world.png)

## Widgets

In Kivy widgets are the building blocks of the GUI interface, which we created for our app. 
The main app takes 1 widget when built. 
In order to have muiltiple widgets there are layout out widgets that allow muiltple widgets to be attached to it. 

There are 6 different [layout widgets](http://kivy.org/docs/guide/widgets.html#organize-with-layouts) in kivy.

- BoxLayout
- GridLayout
- StackLayout
- AnchorLayout
- FloatLayout
- RelativeLayout

Of the different layouts in our we used box the most and grid for tables. 

When using muiltple widgets you form a widget tree where there is a root widget which is usally a layout. 

Kivy includes examples of how to use each of the widgets. I would recommened looking through these to identify the best widget to use for each element of the app. 

## Kv Language

Kivy uses it's own [Kv Language](http://kivy.org/docs/guide/lang.html) in order to create widget trees. 
When testing out different layouts using the Kv language makes it easier for you to experment with different widgets. 


