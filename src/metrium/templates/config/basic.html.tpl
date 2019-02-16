{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Basic{% endblock %}
{% block content %}
    <form action="{{ url_for('do_basic_config') }}" method="post" class="form">
        <div class="label">
            <label>URL</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="url" placeholder="eg: http://metrium.host.com/" value="{{ config.url }}"
                   data-error="{{ errors.url }}" />
        </div>
        <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
