{% extends "partials/layout_event.html.tpl" %}
{% block title %}Events{% endblock %}
{% block name %}New Video{% endblock %}
{% block content %}
    <form action="{{ url_for('do_video_event') }}" method="post" class="form">
        <div class="video-preview">
            <div class="label">
                <label>URL</label>
            </div>
            <div class="input">
                <input class="text-field focus" name="url" placeholder="eg: youtube.com/watch?xxxx"
                       value="{{ video.url }}" data-error="{{ errors.url }}" />
            </div>
            <div class="preview-panel">
                <div class="label">
                    <label>Preview</label>
                </div>
                <div class="video-target" data-width="540" data-height="300"></div>
            </div>
        </div>
        <div class="quote">
            By clicking Submit Video, you agree to our Service Agreement and that you have
            read and understand our Privacy Policy.
        </div>
        <span class="button" data-submit="true">Submit Video</span>
    </form>
{% endblock %}
