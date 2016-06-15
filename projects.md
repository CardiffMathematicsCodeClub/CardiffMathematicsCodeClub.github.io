---
layout: page
title: Projects
permalink: "/projects/"
---

<ul class="posts">
{% for project in site.projects %}
    <li>
       <p class="project-name">{{project.name}}</p>
       <p class="project-desc">{{project.description}}</p>
       <p><a href="{{project.url}}">More Info</a></p>
    </li>
{% endfor %}
</ul>
