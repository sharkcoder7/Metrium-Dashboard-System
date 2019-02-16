{% extends "partials/layout_settings.html.tpl" %}
{% block title %}Import{% endblock %}
{% block name %}Import{% endblock %}
{% block content %}
    <div class="quote">
        Please provide the file containing the database data to be imported
        to the data source.<br />
        Remember this is a <strong>dangerous operation</strong>.
    </div>
    <div class="separator-horizontal"></div>
    {% if error %}
        <div class="quote error">{{ error }}</div>
    {% endif %}
    <form enctype="multipart/form-data" action="{{ url_for('import_do') }}" method="post" class="form tiny">
        <div class="input single">
             <a data-name="import_file" class="uploader">Select & Upload the import file</a>
        </div>
        <span class="button" data-link="{{ url_for('settings') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Upload</span>
    </form>
{% endblock %}
