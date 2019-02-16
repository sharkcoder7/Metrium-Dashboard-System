<div class="header-notifications-container">
    {% if request.args.message %}
        <div class="header-notification link-close {{ request.args.message_t|default('info') }}">{{ request.args.message }}</div>
    {% endif %}
</div>
