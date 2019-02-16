{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config{% endblock %}
{% block content %}
    <ul>
        <li>
            <div class="name">
                <a href="{{ url_for('basic_config') }}">Basic</a>
            </div>
            <div class="description">Global basic configuration of metrium</div>
        </li>
        <li>
            <div class="name">
                <a href="{{ url_for('mail_config') }}">Mail</a>
            </div>
            <div class="description">IMAP client configuration</div>
        </li>
        <li>
            <div class="name">
                <a href="{{ url_for('pending_config') }}">Pending</a>
            </div>
            <div class="description">Settings for the list of pending things</div>
        </li>
        <li>
            <div class="name">
                <a href="{{ url_for('omni_config') }}">Omni</a>
            </div>
            <div class="description">Settings for the Omni infra-structure</div>
        </li>
        <li>
            <div class="name">
                <a href="{{ url_for('github_config') }}">GitHub</a>
            </div>
            <div class="description">Settings for the GitHub website</div>
        </li>
    </ul>
{% endblock %}
