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

import quorum

from . import base

class MessagesConfig(base.Config):

    first_title = dict()

    second_title = dict()

    first_items = dict(
        type = list
    )

    second_items = dict(
        type = list
    )

    @classmethod
    def get_state(cls):
        events = cls.get_events()
        return {
            "messages.update" : [{
                "messages" : events
            }]
        }

    @classmethod
    def get_events(cls, count = 10):
        message = cls.singleton()
        return message.get_event()

    def post_save(self):
        base.Config.post_create(self)

        pusher = quorum.get_pusher()
        pusher.trigger("global", "messages.update", {
            "messages" : self.get_event()
        })

    def get_event(self):
        return [
            dict(
                title = self.first_title,
                items = [dict(message = value) for value in self.first_items]
            ), dict(
                title = self.second_title,
                items = [dict(message = value) for value in self.second_items]
            )
        ]
