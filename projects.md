---
title: Projects
layout: page
permalink: "/projects/"
---

<ul class="posts">
{% for project in site.projects %}
  {% include project_link.html %}
{% endfor %}
</ul>
