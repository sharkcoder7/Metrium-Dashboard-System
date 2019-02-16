{% extends "partials/layout_config.html.tpl" %}
{% block title %}Config{% endblock %}
{% block name %}Config :: Pending{% endblock %}
{% block content %}
    <form action="{{ url_for('do_pending_config') }}" method="post" class="form">
        <table class="table table-edit" data-error="{{ errors.folders }}{{ errors.severities }}">
            <input name="folders[]" type="hidden" class="table-empty-field" />
            <thead>
                <tr>
                    <th class="longer-input" data-width="384">Folder</th>
                    <th>Severity</th>
                </tr>
            </thead>
            <tbody>
                <tr class="template">
                    <td>
                        <input type="text" name="folders" class="text-field" />
                    </td>
                    <td>
                        <div name="severities" class="drop-field drop-field-select">
                            <ul class="data-source" data-type="local">
                                <li>critical</li>
                                <li>major</li>
                                <li>minor</li>
                                <li>trivial</li>
                            </ul>
                        </div>
                    </td>
                </tr>
                {% for folder, severity in config and config.items_f() or [] %}
                    <tr>
                        <td>
                            <input type="text" name="folders" class="text-field" value="{{ folder }}" />
                        </td>
                        <td>
                            <div name="severities" class="drop-field drop-field-select" value="{{ severity }}">
                                <ul class="data-source" data-type="local">
                                    <li>critical</li>
                                    <li>major</li>
                                    <li>minor</li>
                                    <li>trivial</li>
                                </ul>
                            </div>
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
