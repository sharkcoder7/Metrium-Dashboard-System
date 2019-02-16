#!/usr/bin/python
# -*- coding: utf-8 -*-

# Metrium System
# Copyright (c) 2008-2019 EdenTech Labs.
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
import setuptools

setuptools.setup(
    name = "metrium",
    version = "0.1.5",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Pingu Web Interface",
    license = "Apache License, Version 2.0",
    keywords = "metrium dashboard metrics television",
    url = "http://metrium.com",
    zip_safe = False,
    packages = [
        "metrium",
        "metrium.bots",
        "metrium.models",
        "metrium.models.config",
        "metrium.views",
        "metrium.views.api",
        "metrium.views.web"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    package_data = {
        "metrium" : [
            "static/css/*",
            "static/images/*.png",
            "static/images/*.ico",
            "static/images/logos/*.png",
            "static/js/*.js",
            "static/js/*.join",
            "static/js/base/*.js",
            "static/sounds/*",
            "templates/*.tpl",
            "templates/account/*.tpl",
            "templates/boards/*.tpl",
            "templates/config/*.tpl",
            "templates/debug/*.tpl",
            "templates/log/*.tpl",
            "templates/partials/*.tpl"
        ]
    },
    install_requires = [
        "flask",
        "quorum",
        "pymongo",
        "redis",
        "pusher",
        "omni_api",
        "github_api_python"
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
