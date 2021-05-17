---
layout: home
---
<div class="container-fluid">
<div class="row">
{% assign sections = site.sections | sort: "display.home" %}
{% for section in sections %}
{% if section.display.home %}
<div class="card  col-3 " >
  <div class="card-body mb-4">
  <a href="{{ section.url }}">

    <h4 class="card-title">
      <i class="bi bi-{{site.data.icons[section.name] | default: 'people' }}"></i>
      {{ section.title }}
    </h4>
    <p class="card-text">{{ section.abstract }}</p>
  </a>

  </div>
</div>
{% endif %}
{% endfor %}
</div>
</div>
