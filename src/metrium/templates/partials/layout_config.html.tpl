{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("config.base") %}
            {% if sub_link == "base" %}
                <a href="{{ url_for('base_config') }}" class="active">base</a>
            {% else %}
                <a href="{{ url_for('base_config') }}">base</a>
            {% endif %}
        {% endif %}
        {% if acl("config.basic") %}
            //
            {% if sub_link == "basic" %}
                <a href="{{ url_for('basic_config') }}" class="active">basic</a>
            {% else %}
                <a href="{{ url_for('basic_config') }}">basic</a>
            {% endif %}
        {% endif %}
        {% if acl("config.mail") %}
            //
            {% if sub_link == "mail" %}
                <a href="{{ url_for('mail_config') }}" class="active">mail</a>
            {% else %}
                <a href="{{ url_for('mail_config') }}">mail</a>
            {% endif %}
        {% endif %}
        {% if acl("config.messages") %}
            //
            {% if sub_link == "messages" %}
                <a href="{{ url_for('messages_config') }}" class="active">messages</a>
            {% else %}
                <a href="{{ url_for('messages_config') }}">messages</a>
            {% endif %}
        {% endif %}
        {% if acl("config.pending") %}
            //
            {% if sub_link == "pending" %}
                <a href="{{ url_for('pending_config') }}" class="active">pending</a>
            {% else %}
                <a href="{{ url_for('pending_config') }}">pending</a>
            {% endif %}
        {% endif %}
        {% if acl("config.omni") %}
            //
            {% if sub_link == "omni" %}
                <a href="{{ url_for('omni_config') }}" class="active">omni</a>
            {% else %}
                <a href="{{ url_for('omni_config') }}">omni</a>
            {% endif %}
        {% endif %}
        {% if acl("config.github") %}
            //
            {% if sub_link == "github" %}
                <a href="{{ url_for('github_config') }}" class="active">github</a>
            {% else %}
                <a href="{{ url_for('github_config') }}">github</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
