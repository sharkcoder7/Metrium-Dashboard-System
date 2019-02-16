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

from . import base

class Omni(base.Base):

    sales_total = dict(
        type = list
    )

    sales_data = dict(
        type = list
    )

    sales_stores = dict(
        type = list
    )

    entries_stores = dict(
        type = list
    )

    top_stores = dict(
        type = list
    )

    top_employees = dict(
        type = list
    )

    @classmethod
    def get_state(cls):
        omni = cls.get(raise_e = False)
        if not omni: return dict()
        return {
            "omni.sales_total" : [{
                "sales_total" : omni.sales_total
            }],
            "omni.sales_data" : [{
                "sales_data" : omni.sales_data
            }],
            "omni.sales_stores" : [{
                "sales_stores" : omni.sales_stores
            }],
            "omni.entries_stores" : [{
                "entries_stores" : omni.entries_stores
            }],
            "omni.top_stores" : [{
                "top_stores" : omni.top_stores
            }],
            "omni.top_employees" : [{
                "top_employees" : omni.top_employees
            }]
        }
