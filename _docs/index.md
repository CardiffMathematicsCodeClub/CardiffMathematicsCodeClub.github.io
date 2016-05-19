---
layout: page
title: Documentation
---

Welcome to the Code Club Website's Documentation! Here you will find out how
we build the website, everything from adding blog posts and language pages to
how the theme changer works!

_Note:_ This part of the website is still very young, so we haven't quite
figured out how best to structure the documentation yet. Don't worry we are
working to fix it and should have someting better in the coming months.

<ul>
  {% for doc in site.docs %}
    {% unless {{doc.title}} == "Documentation" %}
      <li><a href="{{doc.url}}">{{doc.title}}</a></li>
    {% endunless %}
  {% endfor %}
</ul>
