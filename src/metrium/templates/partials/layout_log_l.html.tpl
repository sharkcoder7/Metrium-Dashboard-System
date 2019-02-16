{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("logs.list") %}
            {% if sub_link == "list" %}
                <a href="{{ url_for('list_logs') }}" class="active">list</a>
            {% else %}
                <a href="{{ url_for('list_logs') }}">list</a>
            {% endif %}
        {% endif %}
        {% if acl("logs.new") %}
            //
            {% if sub_link == "create" %}
                <a href="{{ url_for('new_log') }}" class="active">create</a>
            {% else %}
                <a href="{{ url_for('new_log') }}">create</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
