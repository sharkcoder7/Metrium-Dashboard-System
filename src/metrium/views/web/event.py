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

from metrium.main import app
from metrium.main import flask
from metrium.main import quorum

@app.route("/events", methods = ("GET",))
@quorum.ensure("event.base")
def base_events():
    return flask.render_template(
        "event/base.html.tpl",
        link = "events",
        sub_link = "base"
    )

@app.route("/events/videos/new", methods = ("GET",))
@quorum.ensure("event.video")
def video_event():
    return flask.render_template(
        "event/video.html.tpl",
        link = "events",
        sub_link = "video",
        video = {},
        errors = {}
    )

@app.route("/events/videos", methods = ("POST",))
@quorum.ensure("event.video")
def do_video_event():
    url = quorum.get_field("url")

    pusher = quorum.get_pusher()
    pusher.trigger("global", "video.open", {
        "url" : url
    })

    return flask.redirect(
        flask.url_for("base_events")
    )
