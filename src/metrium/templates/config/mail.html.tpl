{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Mail{% endblock %}
{% block content %}
    <form action="{{ url_for('do_mail_config') }}" method="post" class="form">
        <div class="label">
            <label>IMAP Host</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="host" placeholder="eg: imap.host.com" value="{{ config.host }}"
                   data-error="{{ errors.host }}" />
        </div>
        <div class="label">
            <label>Email</label>
        </div>
        <div class="input">
            <input class="text-field" name="username" placeholder="eg: johndoe@host.com" value="{{ config.username }}"
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
