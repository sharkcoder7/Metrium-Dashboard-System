{% extends "partials/layout.html.tpl" %}
{% block title %}Debug{% endblock %}
{% block name %}Debug :: {{ debug.id }}{% endblock %}
{% block content %}
    <div class="quote">{{ debug.message }}</div>
    <div class="separator-horizontal"></div>
    {% if debug.lines %}
        <pre>{% for line in debug.lines %}{{ line }}
{% endfor %}</pre>
    {% endif %}
{% endblock %}
