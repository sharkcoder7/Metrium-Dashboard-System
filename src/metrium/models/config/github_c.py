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

import github
import quorum

from . import base

SCOPE = (
    "user",
    "repo"
)

class GithubConfig(base.Config):

    access_token = dict(
        index = True
    )

    username = dict(
        index = True
    )

    repos = dict(
        type = list
    )

    @classmethod
    def validate_new(cls):
        return super(GithubConfig, cls).validate_new() + [
            quorum.not_null("access_token"),
            quorum.not_empty("access_token"),

            quorum.not_null("username"),
            quorum.not_empty("username")
        ]

    @classmethod
    def get_api(cls, scope = SCOPE):
        config = cls.singleton()
        api = github.API(scope = scope)
        api.access_token = config and config.access_token
        return api

    def pre_create(self):
        base.Config.pre_create(self)

        self.name = "github"
