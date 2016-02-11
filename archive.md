---
layout: page
title: Archive
---

Welcome to the archives! From here you can find the latest [blog posts][blog],
upcoming [workshops][workshop] and the best quotes from the last few code club
[sessions][pastsessions].

Or if you feel like digging then you can also find any session quote, blog post
or tutorial that has ever been released on the site. So what are you waiting
for? Dive in! - who knows what treasures you might find...

## Workshops

Every once in a while during code club someone will run a quick (usually about
30 minutes long) workshop to get you introduced to a particular tool or concept.
Here you can find any upcoming workshops:

{%capture workshops%}{% for ws in site.workshops %}{% assign now = "now" | date: "%s" %}{% assign wsdate = ws.when | date: "%s" %}{% if wsdate > now %}<li>{{ws.when}}: <a href="{{ws.url}}">{{ws.title}}</a> by {{ws.leader}}</li>{% endif %}{% endfor %}{%endcapture %}

{% if workshops.size > 0 %}
<div class="session-list">
    {{ workshops }}
</div>
{% else %}

It doesn't look like we have any workshops scheduled. If you'd like to see us
run a workshop on a particular topic then be sure to
[open an issue](https://github.com/CardiffMathematicsCodeClub/CardiffMathematicsCodeClub.github.io/issues)
and let us know!

{% endif %}

Or if you'd like to see a full list and any past workshops then be sure to check
them all out [here][workshop]

## Blog

Here is a selection of the latest code club blog posts. But be sure to check out
the full blog [here][blog]:

<ul class="posts">
  {% for post in site.posts limit:3 %}
       {% include post_link.html %}
  {% endfor %}
</ul>

## Past Sessions

Want to get an idea to what we've been up to? Well here is a selection of some
the most recent sessions. Don't miss the full list [here][pastsessions]
though:

<div class="session-list">
   {% assign recentsessions = site.data.sessions[0].terms.spring | reverse %}
   {% for session in recentsessions limit:3 %}
   {% assign person = site.data.contributors[session.author] %}
   <div class="session">
       {% include session_info.html %}
   </div>
   {% endfor%}
</div>

[blog]: /blog/
[workshop]: /workshops/
[pastsessions]: /sessions.html
