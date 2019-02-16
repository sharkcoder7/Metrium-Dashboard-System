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

import flask #@UnusedImport

import quorum

import metrium.models

SECRET_KEY = "bha7t47805sv5jvmnhlj4nx7r2o97jos"
""" The "secret" key to be at the internal encryption
processes handled by flask (eg: sessions) """

MONGO_DATABASE = "metrium"
""" The default database to be used for the connection with
the mongo database """

@quorum.onrun
def onrun():
    from metrium import bots
    omni_bot = bots.OmniBot()
    imap_bot = bots.ImapBot()
    github_bot = bots.GithubBot()
    pending_bot = bots.PendingBot()
    omni_bot.start()
    imap_bot.start()
    github_bot.start()
    pending_bot.start()

app = quorum.load(
    name = __name__,
    secret_key = SECRET_KEY,
    redis_session = True,
    mongo_database = MONGO_DATABASE,
    logger = "metrium.debug",
    models = metrium.models
)

import metrium.views #@UnusedImport

if __name__ == "__main__":
    quorum.run(server = "netius")
else:
    __path__ = []
