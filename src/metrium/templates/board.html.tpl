{% extends "partials/layout_full.html.tpl" %}
{% block title %}Dashboard{% endblock %}
{% block name %}Dashboard{% endblock %}
{% block content %}
    {% set logo_url = request.args.logo_url %}
    {% set logo_url = conf("METRIUM_LOGO_URL", logo_url) %}
    <div class="dashboard {{ variant }}">
        <audio class="sound"></audio>
        <div class="video" data-width="1280" data-height="780" data-hd="1"
             data-chromeless="1" data-auto_play="1"></div>
        <div class="pusher" data-key="{{ conf('PUSHER_KEY') }}"
             data-cluster="{{ conf('PUSHER_CLUSTER')|default('', True) }}"></div>
        <div class="header">
            <div class="logo" style="{% if logo_url %}background-image: url({{ logo_url }});{% endif %}"></div>
            <ul class="sections">
                {% if variant == "sales" %}
                    <li class="active">global</li>
                    <li>vendas</li>
                    <li>pendentes</li>
                {% elif variant == "commits" %}
                    <li class="active">global</li>
                {% elif variant == "store" %}
                    <li class="active">mensagens</li>
                {% endif %}
            </ul>
        </div>
        <div class="message success">
            <span class="author"></span>
            <span class="separator">-</span>
            <span class="contents"></span>
        </div>
        <div class="frame {% if variant in ('store',) %}full{% endif %}">
            <div class="context">
                <div class="date">
                    <div class="week-day"></div>
                    <div class="day"></div>
                    <div class="time"></div>
                </div>
                {% if variant == "sales" %}
                    <div class="news"></div>
                {% endif %}
            </div>
            <div class="boards">
                {% if variant == "sales" %}
                    {% include "boards/sales/global.html.tpl" %}
                    {% include "boards/sales/sales.html.tpl" %}
                    {% include "boards/sales/pending.html.tpl" %}
                {% elif variant == "commits" %}
                    {% include "boards/commits/global.html.tpl" %}
                {% elif variant == "store" %}
                    {% include "boards/store/messages.html.tpl" %}
                {% endif %}
            </div>
        </div>
    </div>
{% endblock %}
