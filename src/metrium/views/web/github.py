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

@app.route("/github/authorize", methods = ("GET",))
@quorum.ensure("github.authorize")
def github_authorize():
    next = quorum.get_field("next")
    api = models.GithubConfig.get_api()
    return flask.redirect(
        api.oauth_authorize(state = next)
    )

@app.route("/github/oauth", methods = ("GET",))
def github_oauth():
    code = quorum.get_field("code")
    next = quorum.get_field("state")
    error = quorum.get_field("error")
    error_description = quorum.get_field("error_description")
    if error:
        return flask.render_template(
            "error.html.tpl",
            error = error,
            description = error_description
        )

    api = models.GithubConfig.get_api()
    access_token = api.oauth_access(code)
    user = api.self_user()
    config = models.GithubConfig.singleton()
    config.access_token = access_token
    config.username = user["login"]
    config.save()
    flask.session["gh.access_token"] = access_token
    return flask.redirect(
        next or flask.url_for("index")
    )
