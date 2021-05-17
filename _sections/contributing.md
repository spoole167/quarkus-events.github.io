---
name: Contributing
title: Contributing Content
abstract: Instructions on how to get content added to this website
layout: default
display:
  home: 100
  nav: 100
---
<h3>Contributing content</h3>

Is as easy as a PR or raising an issue

Each type of content has specific information that is needed.

<ul>
{% for g in site.guides %}
<li><a href="{{ g.url }}">{{ g.title }}</a></li>
{% endfor %}
</ul>
