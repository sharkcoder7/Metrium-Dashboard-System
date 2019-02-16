{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Omni{% endblock %}
{% block content %}
    <form action="{{ url_for('do_omni_config') }}" method="post" class="form">
        <div class="label">
            <label>Base URL</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="base_url" placeholder="eg: http://xyz.frontdoorhd.com/"
                   value="{{ config.base_url }}" data-error="{{ errors.base_url }}" />
        </div>
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe" value="{{ config.username }}"
                   data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" placeholder="eg: jonhdoepass"
                   value="{{ config.password }}" data-error="{{ errors.password }}" />
        </div>
        <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
