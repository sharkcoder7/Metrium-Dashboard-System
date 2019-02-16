{% extends "partials/layout_log_l.html.tpl" %}
{% block title %}Log{% endblock %}
{% block name %}Log{% endblock %}
{% block content %}
    <ul class="filter" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_logs_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template table-row">
            <div class="owner text-left" data-width="140">%[_owner]</div>
            <div class="message text-left" data-width="360">%[message]</div>
            <div class="type text-right %[type]" data-width="80">%[type]</div>
            <div class="table-clear"></div>
        </li>
        <div class="filter-no-results quote">
            No results found
        </div>
        <div class="filter-more">
            <span class="button more">Load more</span>
            <span class="button load">Loading</span>
        </div>
    </ul>
{% endblock %}
