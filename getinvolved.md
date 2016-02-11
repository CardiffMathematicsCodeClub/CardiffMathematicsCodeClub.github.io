---
layout: page
title: Get Involved
categories: getinvolved
---

## Active Projects

There are many concurrent projects being worked on at code club, below is a
list of all the active projects currently being developed. If you wish want to see
a list of all projects then you can find them
[here](/projects/) (if you see a project that interests
you there then by all means bring it back from the dead!)

<ul class="posts">
 {% for project in site.projects %}
  {% if project.active %}
    {% include project_link.html %}
  {% endif %}
{% endfor %}
</ul>

Or if you have an idea for a project of your own and you'd like others to help/
work on it with you then send us a pull request and get it put up here!

## Programming Challenges

Don't feel ready yet to contribute to a full blown project? Don't worry below is a list of
programming challenges where you can develop your skills further and if you get stuck there
will be plenty of people at code club willing to help you get unstuck!

- [Project Euler](https://projecteuler.net) - A site with over 450 problems
  many with a mathematical focus to get your teeth into!
- [Daily Programmer](http://www.reddit.com/r/dailyprogrammer/) - A subreddit
  with new problems released on a Monday, Wednesday and Friday increasing in difficulty
  throughout the week. Challenges are based on a wide variety of topics, often submitted by
  fellow users of the subreddit.
- [Platinum Rift](http://www.codingame.com/home/platinum-rift) - An online game.
- [Programming Praxis](http://programmingpraxis.com/) - A blog with new
  exercises posted every few days on a range of topics. 
  Many of them are presented as a word problem.
- [Vince's website](http://vknight.org/) - A link to the Computing for 
  Mathematics homepage.


Here is a video that shows the various contributors so far (as of 4th of December 2014):

<div class="video">
    <figure>
        <iframe width="560" height="315" align='middle' src="//www.youtube.com/embed/UdbXWZJSwnE" frameborder="0" allowfullscreen></iframe>
    </figure>
</div>

## Contributors

{% for contributor in site.data.contributors %}
{% assign person = contributor[1] %}
  - **{{person.name}}** *([{{person.title | default: '...Pending...'}}]({{person.github-page}}))*
{% endfor %}

* <center>Disclamer: This is NOT done in any particular order.
It's definitly NOT in ALPHABETICAL order. </center> *
