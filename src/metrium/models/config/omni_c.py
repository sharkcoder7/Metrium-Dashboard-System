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

import omni
import quorum

from . import base

class OmniConfig(base.Config):

    base_url = dict(
        index = True
    )

    username = dict(
        index = True
    )

    password = dict(
        index = True
    )

    registered = dict()

    @classmethod
    def validate_new(cls):
        return super(OmniConfig, cls).validate_new() + [
            quorum.not_null("base_url"),
            quorum.not_empty("base_url"),

            quorum.not_null("username"),
            quorum.not_empty("username"),

            quorum.not_null("password"),
            quorum.not_empty("password")
        ]

    @classmethod
    def get_api(cls):
        config = cls.singleton()
        api = omni.API(
            base_url = config and config.base_url,
            username = config and config.username,
            password = config and config.password
        )
        return api

    def pre_create(self):
        base.Config.pre_create(self)

        self.name = "omni"

    def is_registered(self, api, callback_url):
        # verifies that the registered field exists in case
        # it does not returns immediately false (no registration)
        if not hasattr(self, "registered"): return False
        if not self.registered: return False

        # retrieves the base url of the omni api from the api client
        # and then retrieves the (already) registered base url and
        # callback url values and compares them against the new ones
        # that are going to be used in case they are the same the
        # registration is considered to be the same
        base_url = api.base_url
        _base_url, _callback_url = self.registered.split("$", 1)
        return base_url == _base_url and callback_url == _callback_url
