{% extends "partials/layout.html.tpl" %}
{% block title %}Debug{% endblock %}
{% block name %}Debug{% endblock %}
{% block content %}
    <ul class="filter" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_debug_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template table-row">
            <div class="date text-left" data-width="160">%[timestamp_l]</div>
            <div class="message text-left" data-width="420">
                <a href="{{ url_for('show_debug', id = 0) }}%[id]">%[message]</a>
            </div>
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
