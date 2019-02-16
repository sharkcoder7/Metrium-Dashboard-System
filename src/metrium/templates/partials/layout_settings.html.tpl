{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("settings") %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('settings') }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('settings') }}">show</a>
            {% endif %}
        {% endif %}
        {% if acl("import") %}
            //
            {% if sub_link == "import" %}
                <a href="{{ url_for('import_a') }}" class="active">import</a>
            {% else %}
                <a href="{{ url_for('import_a') }}">import</a>
            {% endif %}
        {% endif %}
        {% if acl("export") %}
            //
            {% if sub_link == "edit" %}
                <a href="{{ url_for('export_do') }}" class="active no-async">export</a>
            {% else %}
                <a href="{{ url_for('export_do') }}" class="no-async">export</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
