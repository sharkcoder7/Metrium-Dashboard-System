{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("accounts.list") %}
            {% if sub_link == "list" %}
                <a href="{{ url_for('list_accounts') }}" class="active">list</a>
            {% else %}
                <a href="{{ url_for('list_accounts') }}">list</a>
            {% endif %}
        {% endif %}
        {% if acl("accounts.new") %}
            //
            {% if sub_link == "create" %}
                <a href="{{ url_for('new_account') }}" class="active">create</a>
            {% else %}
                <a href="{{ url_for('new_account') }}">create</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
