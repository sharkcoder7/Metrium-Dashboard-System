{% extends "partials/layout_event.html.tpl" %}
{% block title %}Events{% endblock %}
{% block name %}Events{% endblock %}
{% block content %}
    <ul>
        <li>
            <div class="name">
                <a href="{{ url_for('video_event') }}">Video</a>
            </div>
            <div class="description">Generate an event for video showing</div>
        </li>
    </ul>
{% endblock %}
