---
layout: page
title: Reference
categories: inspiration
---

Welcome to the reference section of the code club site. Here you will find
information on a wide range of programming languages, frameworks and tools to
help you find something which interests you and how to get started!

This section of the site is under constant development and if you find that we
are missing something than we strongly recommend that you 
[get involved](/getinvolved.html) and send us a pull request containing the
missing information.

## Programming Languages
There are more programming languages than stars in the galaxy... OK
*slight* exaggeration but there are a lot of them. Created for any
possible purpose imaginable from building video games to driving rovers on Mars
or simply trying to [confuse](/languages/brainfk.html) the programmer using
them!


Some of the more popular languages include [Java](/languages/java.html),
[Python](/languages/python.html) and [C++](/languages/C++.html).
However there are many more than that! Below is just a sample of them.

<div class="two-cols">
    <ul>
        {% for page in site.languages %}
	        {% unless page.tags contains "forfun" %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
	        {% endunless %}
        {% endfor %}
    </ul>
</div>

Now what do programmers do when they are bored? Well they invent their own
programming langauges of course!
These languages are not meant to be practical but rather offer some quirky or
interesting way of trying to make a computer do something - and often in the 
most painful way possible! These languages are often referrred to as
"Esoteric Languages".

Below is a list of some of these languages but I recommend you check out the
[EsoLang Wiki](https://esolangs.org/wiki/Language_list) where you can find
a long list of these languages!

<div class="two-cols">
    <ul>
        {% for page in site.languages %}
	        {% if page.tags contains "forfun" %}
                <li><a href="{{ page.url }}">{{ page.title }}</a></li>
	        {% endif %}
        {% endfor %}
    </ul>
</div>

## Tools

There are many tools you can use below is just a sample.

<div class="two-cols">
    <ul>
        {% for page in site.tools %}
            <li><a href="{{ page.url }}">{{ page.title }}</a></li>
        {% endfor %}
    </ul>
</div>
