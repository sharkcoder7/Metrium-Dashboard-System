{% extends "partials/layout_config.html.tpl" %}
{% block title %}GitHub{% endblock %}
{% block name %}Config :: GitHub{% endblock %}
{% block content %}
    <form action="{{ url_for('do_github_config') }}" method="post" class="form">
        {% if config.username %}
            <div class="label">
                <label>Username</label>
            </div>
            <div class="input">
                <input class="text-field" value="{{ config.username }}" data-disabled="1" />
            </div>
            <div class="label">
                <label>Repos</label>
            </div>
             <div class="input">
                 {% for repo in repos %}
                    <div class="option">
                        <span class="float-left">{{ repo.full_name }}</span>
                        {% if repo.full_name in config.repos %}
                            <input class="float-right" type="checkbox"
                                   name="repos" value="{{ repo.full_name }}" checked="1" />
                        {% else %}
                            <input class="float-right" type="checkbox"
                                   name="repos" value="{{ repo.full_name }}" />
                        {% endif %}
                        <div class="clear"></div>
                    </div>
                {% endfor %}
            </div>
            <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
            //
            <span class="button" data-submit="true">Update</span>
        {% endif %}
        <div class="alternative">
            <span class="button"
                  data-link="{{ url_for('github_authorize', next = url_for('base_config')) }}">Link Account</span>
        </div>
    </form>
{% endblock %}
