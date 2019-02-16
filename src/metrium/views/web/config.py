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

@app.route("/config", methods = ("GET",))
@quorum.ensure("config.base")
def base_config():
    return flask.render_template(
        "config/base.html.tpl",
        link = "config",
        sub_link = "base"
    )

@app.route("/config/basic", methods = ("GET",))
@quorum.ensure("config.basic")
def basic_config():
    config = models.BasicConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/basic.html.tpl",
        link = "config",
        sub_link = "basic",
        config = config,
        errors = {}
    )

@app.route("/config/basic", methods = ("POST",))
@quorum.ensure("config.basic")
def do_basic_config():
    config = models.BasicConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/basic.html.tpl",
            link = "config",
            sub_link = "basic",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )

@app.route("/config/mail", methods = ("GET",))
@quorum.ensure("config.mail")
def mail_config():
    config = models.MailConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/mail.html.tpl",
        link = "config",
        sub_link = "mail",
        config = config,
        errors = {}
    )

@app.route("/config/mail", methods = ("POST",))
@quorum.ensure("config.mail")
def do_mail_config():
    config = models.MailConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/mail.html.tpl",
            link = "config",
            sub_link = "mail",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )

@app.route("/config/messages", methods = ("GET",))
@quorum.ensure("config.messages")
def messages_config():
    config = models.MessagesConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/messages.html.tpl",
        link = "config",
        sub_link = "messages",
        config = config,
        errors = {}
    )

@app.route("/config/messages", methods = ("POST",))
@quorum.ensure("config.messages")
def do_messages_config():
    config = models.MessagesConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/messages.html.tpl",
            link = "config",
            sub_link = "messages",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )

@app.route("/config/pending", methods = ("GET",))
@quorum.ensure("config.pending")
def pending_config():
    config = models.PendingConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/pending.html.tpl",
        link = "config",
        sub_link = "pending",
        config = config,
        errors = {}
    )

@app.route("/config/pending", methods = ("POST",))
@quorum.ensure("config.pending")
def do_pending_config():
    config = models.PendingConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/pending.html.tpl",
            link = "config",
            sub_link = "pending",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )

@app.route("/config/omni", methods = ("GET",))
@quorum.ensure("config.omni")
def omni_config():
    config = models.OmniConfig.get(raise_e = False) or {}
    return flask.render_template(
        "config/omni.html.tpl",
        link = "config",
        sub_link = "omni",
        config = config,
        errors = {}
    )

@app.route("/config/omni", methods = ("POST",))
@quorum.ensure("config.omni")
def do_omni_config():
    config = models.OmniConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/omni.html.tpl",
            link = "config",
            sub_link = "omni",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )

@app.route("/config/github", methods = ("GET",))
@quorum.ensure("config.github")
def github_config():
    config = models.GithubConfig.get(raise_e = False) or {}
    if config:
        api = config.get_api()
        repos = api.self_repos()
    else: repos = []
    return flask.render_template(
        "config/github.html.tpl",
        link = "config",
        sub_link = "github",
        config = config,
        repos = repos,
        errors = {}
    )

@app.route("/config/github", methods = ("POST",))
@quorum.ensure("config.github")
def do_github_config():
    config = models.GithubConfig.singleton()
    try: config.save()
    except quorum.ValidationError as error:
        return flask.render_template(
            "config/github.html.tpl",
            link = "config",
            sub_link = "github",
            config = error.model,
            errors = error.errors
        )

    # redirects the user to the overall configuration
    # selection, as this is the default behavior
    return flask.redirect(
        flask.url_for("base_config")
    )
