---
layout: page
title: Index
---
<div class="two-cols">
    <ul>
        {% for pages in site.pages %}
            {% if pages.categories contains 'editors' %}
                <li><a href="{{ pages.url }}">{{ pages.title }}</a></li>
            {% endif %}
        {% endfor %}
    </ul>
</div>
