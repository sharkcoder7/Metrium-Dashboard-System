{% extends "partials/layout_simple.html.tpl" %}
{% block title %}Login{% endblock %}
{% block name %}Login{% endblock %}
{% block content %}
    <div class="quote">
        Please provide your credentials to be able to access the restricted
        resources.<br />
        These values will <strong>not be visible to any element</strong>.
    </div>
    {% if error %}
        <div class="quote error">{{ error }}</div>
    {% endif %}
    <form action="{{ url_for('login', next = next) }}" method="post" class="form slim">
        <div class="input">
            <input class="small" name="username" value="{{ username }}" placeholder="username" />
        </div>
        <div class="input">
            <input class="small" name="password" placeholder="password" type="password" />
        </div>
        <span class="button" data-link="#">Clear</span>
        //
        <span class="button" data-submit="true">Login</span>
    </form>
{% endblock %}
