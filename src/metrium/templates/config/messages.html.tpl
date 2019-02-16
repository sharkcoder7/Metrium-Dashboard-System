{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Messages{% endblock %}
{% block content %}
    <form action="{{ url_for('do_messages_config') }}" method="post" class="form">
        <div class="label">
            <label>First Title</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="first_title" placeholder="eg: My Title"
                   value="{{ config.first_title }}" data-error="{{ errors.first_title }}" />
        </div>
        <div class="label">
            <label>First Items</label>
        </div>
        <table class="table table-edit" data-error="{{ errors.first_items }}">
            <input name="first_items[]" type="hidden" class="table-empty-field" />
            <thead>
                <tr>
                    <th class="longer-input">Message</th>
                </tr>
            </thead>
            <tbody>
                <tr class="template">
                    <td>
                        <input type="text" name="first_items" class="text-field" />
                    </td>
                </tr>
                {% for item in config and config.first_items or [] %}
                    <tr>
                        <td>
                            <input type="text" name="first_items" class="text-field" value="{{ item }}" />
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
            <tfoot>
                <tr>
                    <td class="table-new-line-row">
                        <span class="button table-new-line">Add Line</span>
                    </td>
                </tr>
            </tfoot>
        </table>
        <div class="label">
            <label>Second Title</label>
        </div>
        <div class="input">
            <input class="text-field focus" name="second_title" placeholder="eg: My Title"
                   value="{{ config.second_title }}" data-error="{{ errors.second_title }}" />
        </div>
        <div class="label">
            <label>Second Items</label>
        </div>
        <table class="table table-edit" data-error="{{ errors.first_items }}">
            <input name="first_items[]" type="hidden" class="table-empty-field" />
            <thead>
                <tr>
                    <th class="longer-input">Message</th>
                </tr>
            </thead>
            <tbody>
                <tr class="template">
                    <td>
                        <input type="text" name="second_items" class="text-field" />
                    </td>
                </tr>
                {% for item in config and config.second_items or [] %}
                    <tr>
                        <td>
                            <input type="text" name="second_items" class="text-field" value="{{ item }}" />
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
            <tfoot>
                <tr>
                    <td class="table-new-line-row">
                        <span class="button table-new-line">Add Line</span>
                    </td>
                </tr>
            </tfoot>
        </table>
        <span class="button" data-link="{{ url_for('base_config') }}">Cancel</span>
        //
        <span class="button" data-submit="true">Update</span>
    </form>
{% endblock %}
