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

import datetime

from . import base

MAXIMUM_MESSAGES = 1000
""" The maximum allowed number of messages, messages after
this offset value will be deleted when the garbage collection
trigger value is enabled """

class Debug(base.Base):

    message = dict()

    lines = dict(
        type = list
    )

    @classmethod
    def log(cls, message, lines = []):
        debug = cls()
        debug.message = message
        debug.lines = lines
        debug.save()

        if not debug.id % MAXIMUM_MESSAGES == 0: return

        outdated = cls.find(skip = MAXIMUM_MESSAGES, sort = [("timestamp", -1)])
        for item in outdated: item.delete()

    @classmethod
    def _build(cls, model, map):
        super(Debug, cls)._build(model, map)
        timestamp = model.get("timestamp", None)
        timestamp_date = timestamp and datetime.datetime.utcfromtimestamp(timestamp)
        timestamp_string = timestamp_date and timestamp_date.strftime("%d/%m/%Y %H:%M:%S")
        model["timestamp_l"] = timestamp_string
