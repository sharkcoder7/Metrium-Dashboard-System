{% extends "partials/layout_simple.html.tpl" %}
{% block title %}Error{% endblock %}
{% block name %}Error{% endblock %}
{% block content %}
    <div class="quote">
        {{ error }}<br/>
        {{ description }}
    </div>
{% endblock %}
