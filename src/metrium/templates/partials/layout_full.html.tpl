{% include "partials/doctype.html.tpl" %}
{% set background_url = request.args.background_url %}
{% set background_url = conf("METRIUM_BACKGROUND_URL", background_url) %}
<head>
    {% block head %}
        {% include "partials/content_type.html.tpl" %}
        {% include "partials/includes.html.tpl" %}
        <title>Metrium / {% block title %}{% endblock %}</title>
    {% endblock %}
</head>
<body class="ux flat fullscreen wait-load" style="{% if background_url %}background-image: url({{ background_url }});{% endif %}">
    {% include "partials/error.html.tpl" %}
    <div id="overlay" class="overlay"></div>
    <div id="content">{% block content %}{% endblock %}</div>
</body>
{% include "partials/end_doctype.html.tpl" %}
