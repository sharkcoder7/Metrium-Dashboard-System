{% extends "partials/layout_log_l.html.tpl" %}
{% block title %}Log{% endblock %}
{% block name %}New Message{% endblock %}
{% block content %}
    <form action="{{ url_for('create_log') }}" method="post" class="form">
        <input type="hidden" name="owner_extra" />
        <div class="label">
            <label>Message</label>
        </div>
        <div class="input">
            <textarea class="text-area focus" name="message" placeholder="eg: hello everyone"
                   data-error="{{ errors.message }}">{{ log.message }}</textarea>
        </div>
        <div class="label">
            <label>Type</label>
        </div>
        <div class="input left">
            {% if log.type == 'info' or not log.type %}
                <input type="radio" name="type" id="info" value="info" checked="1" />
            {% else %}
                <input type="radio" name="type" id="info" value="info" />
            {% endif %}
            <label class="radio-label" for="info">Information</label>
            {% if log.type == 'success' %}
                <input type="radio" name="type" id="success" value="success" checked="1" />
            {% else %}
                <input type="radio" name="type" id="success" value="success" />
            {% endif %}
            <label class="radio-label" for="success">Success</label>
            {% if log.type == 'warning' %}
                <input type="radio" name="type" id="warning" value="warning" checked="1" />
            {% else %}
                <input type="radio" name="type" id="warning" value="warning" />
            {% endif %}
            <label class="radio-label" for="warning">Warning</label>
            {% if log.type == 'error' %}
                <input type="radio" name="type" id="error" value="error" checked="1" />
            {% else %}
                <input type="radio" name="type" id="error" value="error" />
            {% endif %}
            <label class="radio-label" for="error">Error</label>
        </div>
        <div class="quote">
            By clicking Submit Message, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Message</span>
    </form>
{% endblock %}
