{% extends "partials/layout_account_l.html.tpl" %}
{% block title %}Accounts{% endblock %}
{% block name %}Accounts{% endblock %}
{% block content %}
    <ul class="filter" data-no_input="1">
        <div class="data-source" data-url="{{ url_for('list_accounts_json') }}" data-type="json" data-timeout="0"></div>
        <li class="template table-row">
            <div class="status text-left" data-width="210">
                 <a href="{{ url_for('show_account', username = '') }}%[username]">%[username]</a>
            </div>
            <div class="date text-left" data-width="160">%[last_login_l]</div>
            <div class="email text-left" data-width="80">%[email]</div>
            <div class="login-count text-right" data-width="130">%[login_count] times</div>
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
