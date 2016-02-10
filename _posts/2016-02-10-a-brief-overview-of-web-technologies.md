---
layout: post
title: A brief overview of web technologies
author: Alex
categories: tutorial
tags: web html css javascript getstarted
comments: true
---

For those of you who haven't had much experience with web development before
this guide serves to give you a brief overview of what the main technologies
are. In this guide I won't actually tell you how to do anything it's merely to
give you a bird's eye view of web development as a whole, what you might be
interested in and where to go from here to find out more.

The web experience is run by three main technologies:

- *HTML* (Hyper Text Markup Language): This controls what goes on the page, the
  text, images, videos etc. In other words the content you view when you
  navigate to a webpage.
  
- *CSS* (Cascading Style Sheets): The controls how the page looks, how big the
  title is, what colour the background is, where does the sidebar go? This is
  also responsible for making the website *responsive* - more on this later.
  
- *Javascript*: This is a programming language you may or may not have heard of (it's
  also nothing to do with Java despite the similar names). This powers the users'
  experience on the website, it allows you to comment on posts (like this one),
  play games and is unfortantely responsible for all those annoying popup ads!
  
**Note:** While there is some overlap between these technologies, for example I
can write some HTML to make the text italic, or some Javascript to insert the
contents of an article into the page from a hardcoded string, it's generally
best to use the tools for what they are designed for primarily. If anything it
just makes it easier to maintain your website by keeping related things in one
place.

On another note, the technologies listed above is not an exhaustive list of
technologies which run the web, for example I have left out things like *PHP*,
*Flash* and *Java Applets* (not to be confused with Javascript). However the
three listed above are by far the most popular technologies and many of the
others are on their way out having been superseeded by better ones. So if you
focus on the technologies listed above then you can't go far wrong.


So that's it then? Time to go tutorial hunting? Well not quite, we've only
scratched the surface....

## The Problem with Scale 

Unfortunately the technical complexity of our modern day websites has far
outstripped the abilities of the tools used to create them. Take for example the list above
where I introduced the different technologies, if I was to write this in HTML it
would look something like the following:

```html
<ul>
    <li>
        <p>
            <em>HTML</em> (Hypertext Markup Language): This controls what goes
            on the page, the text, images, videos etc. In other words the
            content you view when you navigate to a webpage
        </p>
    </li>
    <li>
        <p>
           <em>CSS</em> (Cascading Style Sheets): This controls how the page
           looks, how big the title is, what colour the background is, where
           does the sidebar go? This is also responsible for making the website
           <em>responsive</em> - more on this later.
       </p>
    </li>
    <li>
        <p>
           <em>Javascript</em>: This is a programming language you may or may
           not have heard of (it's also nothing to do with Java despite the
           similar names). This powers the users' experience on the website, it
           allows you to comment on posts (like this one), play games and is
           unfortantely responsible for all those annoying popup ads!
       </p>
    </li>
</ul>
```

Wow. All that for just a simple list! Unfortunately it doesn't get much better
than that, go ahead see for yourself, right click on this page and select "View
Page Source" I'll wait for you. See how quickly you can find the snippet I gave
above while  also keep in mind that this is a relatively simple website. Try the
same thing on a website like Youtube!

Then don't forget once you've written the HTML you then still have to make it
look good! As you can probably tell this doesn't scale well to large websites,
I think you would even struggle writing all the HTML for this website by hand.

### A quick note on responsiveness

When we talk about responsive websites, we mean websites which respond well to
devices with different screen sizes, resizing elements and adjusting their
layouts so that the content is still displayed well, easy to read and navigate.

So how is it really done? Well, before we dive into that I think it's worthwhile
if we take a quick de-tour and talk about *Static* and *Dynamic* websites.

## Static vs Dynamic Websites

You can divide most websites on the internet into two categories *Static* and
*Dynamic*.

Static websites are "fixed" in the sense that whoever creates the website
decides what will go on the website and then create it. By the time the website
is sat on the server ready to be viewed, the content which appears on every page
is fixed and will not change until the author(s) decide to update it. Users who
visit the site will see the site (hopefully) in exactly the same way as the
author sees it on their machine.

On the other Dynamic websites, aren't fixed. When the author creates the website
they actually construct a set of rules that the server follows to build the
website as users ask to see it and send them the result. Take Google for
example, the designers couldn't possibly predict what everyone will search for
ahead of time, let alone keep it up to date with the thousands of new websites
which are created year on year.

So instead when you search for something, the server will look for matches in
its database and compile a list of results which it then converts into HTML and
sends it off to your browser which you then see.

## So how is it really done?

Over the years developers have created many tools which try to help automate the
process building websites allowing you to focus on what really matters, your
awesome design and content.

In this last section I will list some of these tools, this will no way be
exhaustive but it should give you an idea of what it out there and give a few
directions to start researching what is right for you.

First of all I'll quickly outline what we use to build this very website:

- [Jekyll](http://jekyllrb.com): This is known as a static site generator,
  written in Ruby and sort of acts as a glue between various technologies to
  create a system well suited to sites like this.
  
- [Markdown](https://daringfireball.net/projects/markdown/): This allows us to
  write our content in plain text while using a few special characters to format
  it. For example, you know the HTML I showed you above? Well this is how I 
  actually wrote it when writing this guide:
  
  ```md
  - *HTML* (Hyper Text Markup Language): This controls what goes on the page, the
     text, images, videos etc. In other words the content you view when you
     navigate to a webpage.
  
  - *CSS* (Cascading Style Sheets): The controls how the page looks, how big the
    title is, what colour the background is, where does the sidebar go? This is
    also responsible for making the website *responsive* - more on this later.
  
  - *Javascript*: This is a programming language you may or may not heard of (it's
    also nothing to do with Java despite the similar names). This powers the users'
    experience on the website, it allows you to comment on posts (like this one),
    play games and is unfortantely responsible for all those annoying popup ads!
  
  ```
  
- [Liquid](http://liquidmarkup.org/): Unfortunately we still have to write HTML at some point,
  however Liquid is a templating system which lets us create the structure of
  the webpage leaving "holes" for jekyll to fill in with content when it comes
  to building the website.
  
- [Sass](http://sass-lang.com/): This is what's known as a *preprocessor* for our CSS.
  What this means is that we still essentially write CSS as you normally would
  but with a few extra goodies such as variables, "functions" and the ability to
  split it up into seperate files and "compile" it into a single stylesheet. 
  
- [jQuery](https://jquery.com/): This is a Javascript library, which makes
  writing interactive webpages much easier than it would be in regular
  Javascript. It also handles the differences between different web browsers so
  you don't have to. We use it to implement things like the collapsible sections
  on the Past Sessions page, the menu you see when on mobile and the theme
  changer in the footer of this website.
  
  That pretty much covers everthing we use on this website, but there is much
  more out there.
  
## Other tools and technologies

Here is a selection of other tools that you might want to look into, in no
particular order:

- [Django](https://www.djangoproject.com/): Django is a Python based framework
  for creating dynamic websites, providing easy to use database and user account
  management. Used by websites like Pinterest, National Geographic and
  Instagram.
  
- [Flask](http://flask.pocoo.org/): Another python framework, somewhat similar to
  Django but more lightweight
  
- [Ruby on Rails](http://rubyonrails.org/): Again similar to Django, this time written
  in Ruby based on the Model-View-Controller paradigm. Used by websites such as
  Github and Twitch and Soundcloud.

- [AngularJS](https://angularjs.org/): A Javascript framework this time (one of
  the many, *many* Javascript frameworks) used by Amazon and Wolfram Alpha.
  
- [Happstack](http://happstack.com): A Haskell framework which does everything from
  routing, templating and database management
  
- [ClojureScript](http://clojure.org/about/clojurescript): A compiler for the lisp
  based programming language Clojure which generates Javascript code.
  
- [CoffeeScript](http://coffeescript.org/): Essentially Javascript but with a less
  verbose syntax
  
- [Purescript](http://www.purescript.org): A Haskell inspired programming language
  which compiles to Javascript
  
This barely scratches the surface of web development, there are so many tools
and frameworks out there it would be impossible to cover them all here. But I
hope that this guide has been informative and helps you find the right tool for
whatever it is you wish to make.
