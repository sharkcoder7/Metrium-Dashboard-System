{% extends "partials/layout.html.tpl" %}
{% block header %}
    {{ super() }}
    <div class="links sub-links">
        {% if acl("accounts.show") %}
            {% if sub_link == "show" %}
                <a href="{{ url_for('show_account', username = account.username) }}" class="active">show</a>
            {% else %}
                <a href="{{ url_for('show_account', username = account.username) }}">show</a>
            {% endif %}
        {% endif %}
        {% if acl("accounts.edit") %}
            //
            {% if sub_link == "edit" %}
                <a href="{{ url_for('edit_account', username = account.username) }}" class="active">edit</a>
            {% else %}
                <a href="{{ url_for('edit_account', username = account.username) }}">edit</a>
            {% endif %}
        {% endif %}
        {% if acl("accounts.delete") %}
            //
            {% if sub_link == "delete" %}
                <a href="{{ url_for('delete_account', username = account.username) }}" class="active warning link-confirm"
                   data-message="Do you really want to delete {{ account.username }}  ?">delete</a>
            {% else %}
                <a href="{{ url_for('delete_account', username = account.username) }}" class="warning link-confirm"
                   data-message="Do you really want to delete {{ account.username }} ?">delete</a>
            {% endif %}
        {% endif %}
    </div>
{% endblock %}
