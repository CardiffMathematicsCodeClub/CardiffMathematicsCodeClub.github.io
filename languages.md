---
layout: page
title: Languages
permalink: "/languages/"
---

<div class="two-cols">
    <ul>
    {% for lang in site.languages %}
        <li><a href="{{ lang.url | prepend: site.baseurl }}">{{lang.title}}</a></li>
    {% endfor %}
    </ul>
</div>


