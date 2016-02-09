---
layout: post
title: Introducing Themes and More!
categories: news
author: Alex
comments: true
---

As you may or may not have noticed, the code club website has had the basic
facilities for adding your own custom theme to the website.

Well today I'm happy to announce theses themes are ready for general use! Go on
try it out now, scroll to the bottom of the page you will see a dropdown menu
under a header called `Change Theme:`. Click on it and you will see (at the time
of this announcement) 2 themes to choose from. The original theme for the
website `Code Club Classic` and a new one `Minimal`. 

Choosing a different theme will cause the page to reload briefly as your browser
downloads the new theme but very soon you will be looking at an entirely new
code club website!

Of course it's not very exciting having only 2 themes to choose from, so I
invite you to create your own theme and submit it to the website especially
since there is now...

## A Competition!

As of now the code club is launching it's first competiton! We want you to
create your own look and feel for the website and submit it to the repository.

We will close submissions at the start of the last hour of the last code club
this semester. During the last hour of that same code club, all submissions will
be judged and the winner will be picked as the default theme for all new
visitors to the website!

## How to submit a theme

Now in this post I won't go through how to actually make your theme but that
will be coming up in a future tutorial series, so be on the look out for that,
but this post will tell you how to install and submit your theme once you've
made it.

Your theme should be consist of a single `.scss` file in the `css` folder and
any other sass files that make up your theme should be in their own folder in
the `_sass` folder.

The only thing other than that which you need to do is "install" it. On the
website we have a file called `_data/themes.yml` which we use to tell the
website about the themes we have there for it to use

So to install a theme you need to make an entry similar to this one:

```yml
- name: Minimalist
  shortname: minimal
  version: 0.1
  author: Alex 

```
Where `name` is the name that you want displayed on the website when your theme
is displayed, `shortname` is the name of your `.scss` file in the `css` folder.
`version` is just some number that represents how well developed you think your
theme is and of course `author` should be your name so we know who made that
awesome theme!

Don't worry if you need help installing your theme on the website, there will
always be someone at code club who will be able to help you.
