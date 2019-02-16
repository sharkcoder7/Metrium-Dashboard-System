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

@app.route("/", methods = ("GET",))
@app.route("/index", methods = ("GET",))
@quorum.ensure("index")
def index():
    return flask.render_template(
        "index.html.tpl",
        link = "home"
    )

@app.route("/about", methods = ("GET",))
@quorum.ensure("about")
def about():
    return flask.render_template(
        "about.html.tpl",
        link = "about"
    )

@app.route("/signin", methods = ("GET",))
def signin():
    next = quorum.get_field("next")
    return flask.render_template(
        "signin.html.tpl",
        next = next
    )

@app.route("/signin", methods = ("POST",))
def login():
    # retrieves the next field that may be used latter
    # to re-direct the user back to the original place
    next = quorum.get_field("next")

    # retrieves the username and the password fields
    # and uses them to run the login logic raising an
    # error in case an invalid authentication occurs
    username = quorum.get_field("username")
    password = quorum.get_field("password")
    try: account = models.Account.login(username, password)
    except quorum.OperationalError as error:
        return flask.render_template(
            "signin.html.tpl",
            username = username,
            next = next,
            error = error.message
        )

    # updates the current user (name) in session with
    # the username that has just be accepted in the login
    flask.session["username"] = account.username
    flask.session["tokens"] = account.tokens

    # makes the current session permanent this will allow
    # the session to persist along multiple browser initialization
    flask.session.permanent = True

    return flask.redirect(
        next or flask.url_for("index")
    )

@app.route("/signout", methods = ("GET", "POST"))
def logout():
    next = quorum.get_field("next")

    if "username" in flask.session: del flask.session["username"]
    if "tokens" in flask.session: del flask.session["tokens"]

    return flask.redirect(
        flask.url_for("signin", next = next)
    )

@app.route("/state", methods = ("GET",), json = True)
@quorum.ensure("state", json = True)
def state():
    log_state = models.Log.get_state()
    omni_state = models.Omni.get_state()
    github_state = models.Github.get_state()
    pending_state = models.Pending.get_state()
    messages_state = models.MessagesConfig.get_state()

    state = dict(
        log = log_state,
        omni = omni_state,
        github = github_state,
        pending = pending_state,
        messages = messages_state
    )
    return state

@app.route("/board", methods = ("GET",))
@quorum.ensure("board")
def board():
    variant = quorum.get_field("variant", "sales")
    return flask.render_template(
        "board.html.tpl",
        variant = variant
    )

@app.route("/video", methods = ("GET",))
@quorum.ensure("video")
def video():
    url = quorum.get_field("url")

    pusher = quorum.get_pusher()
    pusher.trigger("global", "video.open", {
        "url" : url
    })

    return flask.redirect(
        flask.url_for("index")
    )
