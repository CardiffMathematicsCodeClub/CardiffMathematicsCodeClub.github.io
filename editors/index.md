---
layout: page
title: Index
---
<div class="two-cols">
    <ul>
        {% for pages in site.pages %}
            {% if pages.categories contains 'editors' %}
                <li><a href="{{ site.baseurl }}{{ pages.url }}">{{ pages.title }}</a>
            {% endif %}
        {% endfor %}
    </ul>
</div>
