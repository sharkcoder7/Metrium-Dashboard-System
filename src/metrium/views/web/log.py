#!/usr/bin/python
# -*- coding: utf-8 -*-

# Metrium System
# Copyright (c) 2008-2019 Hive Solutions Lda.
#
# This file is part of Metrium System.
#
# Metrium System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Metrium System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Metrium System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from metrium import models

from metrium.main import app
from metrium.main import flask
from metrium.main import quorum

@app.route("/logs", methods = ("GET",))
@quorum.ensure("logs.list")
def list_logs():
    return flask.render_template(
        "log/list.html.tpl",
        link = "logs",
        sub_link = "list"
    )

@app.route("/logs.json", methods = ("GET",), json = True)
@quorum.ensure("logs.list", json = True)
def list_logs_json():
    object = quorum.get_object(alias = True, find = True)
    logs = models.Log.find(map = True, sort = [("timestamp", -1)], **object)
    return logs

@app.route("/logs/new", methods = ("GET",))
@quorum.ensure("logs.new")
def new_log():
    return flask.render_template(
        "log/new.html.tpl",
        link = "logs",
        sub_link = "create",
        log = {},
        errors = {}
    )

@app.route("/logs", methods = ("POST",))
@quorum.ensure("logs.new")
def create_log():
    # creates the new log, using the provided arguments and
    # then saves it into the data source, all the validations
    # should be ran upon the save operation
    log = models.Log.new()
    try: log.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "log/new.html.tpl",
            link = "logs",
            sub_link = "create",
            log = error.model,
            errors = error.errors
        )

    # redirects the user to the page that displays the list
    # of logs for the current account in session
    return flask.redirect(
        flask.url_for("list_logs")
    )
