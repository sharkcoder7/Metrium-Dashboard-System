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

import os
import datetime
import tempfile

from metrium.main import app
from metrium.main import flask
from metrium.main import quorum

NAME = "metrium"
""" The default name to be used as prefix for the database
export file in the export operation """

@app.route("/settings", methods = ("GET",))
@quorum.ensure("settings")
def settings():
    return flask.render_template(
        "settings/show.html.tpl",
        link = "settings",
        sub_link = "show"
    )

@app.route("/import", methods = ("GET",))
@quorum.ensure("import")
def import_a():
    return flask.render_template(
        "settings/import.html.tpl",
        link = "settings",
        sub_link = "import"
    )

@app.route("/import", methods = ("POST",))
@quorum.ensure("import")
def import_do():
    # retrieves the import file values (reference to the
    # uploaded file) and then validates if it has been
    # defined, in case it fails prints the template with
    # the appropriate error variable set
    import_file = quorum.get_field("import_file", None)
    if import_file == None or not import_file.filename:
        return flask.render_template(
            "settings/import.html.tpl",
            link = "settings",
            sub_link = "import",
            error = "No file defined"
        )

    # creates a temporary file path for the storage of the file
    # and then saves it into that directory
    fd, file_path = tempfile.mkstemp()
    import_file.save(file_path)

    # retrieves the database and creates a new export manager for
    # the currently defined entities then imports the data defined
    # in the current temporary path
    adapter = quorum.get_adapter()
    manager = quorum.export.ExportManager(
        adapter,
        multiple = quorum.resolve()
    )
    try: manager.import_data(file_path)
    finally: os.close(fd); os.remove(file_path)
    return flask.redirect(
        flask.url_for(
            "import_a",
            message = "Database file imported with success"
        )
    )

@app.route("/export", methods = ("GET",))
@quorum.ensure("export")
def export_do():
    adapter = quorum.get_adapter()
    file = quorum.legacy.BytesIO()
    manager = quorum.export.ExportManager(
        adapter,
        multiple = quorum.resolve()
    )
    manager.export_data(file)

    date_time = datetime.datetime.utcnow()
    date_time_s = date_time.strftime("%Y%m%d")
    file_name = "%s_%s.dat" % (NAME, date_time_s)

    return flask.Response(
        file.getvalue(),
        headers = {
            "Content-Disposition" : "attachment; filename=\"%s\"" % file_name
        },
        mimetype = "application/octet-stream"
    )

@app.route("/reset", methods = ("GET",))
@quorum.ensure("reset")
def reset_do():
    quorum.drop_mongo_db()
    return flask.redirect(
        flask.url_for("settings")
    )
