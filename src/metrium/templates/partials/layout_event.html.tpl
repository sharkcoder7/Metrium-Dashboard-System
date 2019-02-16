{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("event.base") %}
            {% if sub_link == "base" %}
                <a href="{{ url_for('base_events') }}" class="active">base</a>
            {% else %}
                <a href="{{ url_for('base_events') }}">base</a>
            {% endif %}
        {% endif %}
        {% if acl("event.video") %}
            //
            {% if sub_link == "video" %}
                <a href="{{ url_for('video_event') }}" class="active">video</a>
            {% else %}
                <a href="{{ url_for('video_event') }}">video</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
