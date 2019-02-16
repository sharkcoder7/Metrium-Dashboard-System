{% extends "partials/layout_account_l.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}New Account{% endblock %}
{% block content %}
    <form action="{{ url_for('create_account') }}" method="post" class="form">
        <div class="label">
            <label>Username</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="username" placeholder="eg: johndoe" value="{{ account.username }}"
                   data-error="{{ errors.username }}" />
        </div>
        <div class="label">
            <label>Password</label>
        </div>
        <div class="input">
            <input type="password" class="text-field" name="password" placeholder="eg: jonhdoepass"
                   value="{{ account.password }}" data-error="{{ errors.password }}" />
        </div>
        <div class="label">
            <label>Confirm Password</label>
        </div>
        <div class="input">
            <input  type="password" class="text-field" name="password_confirm" placeholder="eg: jonhdoepass"
                    value="{{ account.password_confirm }}" data-error="{{ errors.password_confirm }}" />
        </div>
        <div class="label">
            <label>Email</label>
        </div>
        <div class="input">
            <input class="text-field" name="email" placeholder="eg: johndoe@example.com" value="{{ account.email }}"
                   data-error="{{ errors.email }}" />
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input left">
            {% if account.type == 1 or not account.type %}
                <input type="radio" name="type" id="user" value="1" checked="1" />
            {% else %}
                <input type="radio" name="type" id="user" value="1" />
            {% endif %}
            <label class="radio-label" for="user">User</label>
            {% if account.type == 2 %}
                <input type="radio" name="type" id="admin" value="2" checked="1" />
            {% else %}
                <input type="radio" name="type" id="admin" value="2" />
            {% endif %}
            <label class="radio-label" for="admin">Admin</label>
        </div>
        <div class="quote">
            By clicking Submit Account, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Account</span>
    </form>
{% endblock %}
