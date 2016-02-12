---
layout: page
title: Micro Workshops
permalink: "/workshops/"
---

Code club runs 30 minute workshops that aim to introduce topics that students
would otherwise not learn.

Here are the upcoming workshops:

{% for ws in site.workshops %}
- {{ws.when}}: [{{ws.title}}]({{ ws.url }}) by {{ws.leader}}

  {% if ws.software-pre-reqs %}_Software requirements: ({{ ws.software-pre-reqs }})_ {% endif %}
{% endfor %}
