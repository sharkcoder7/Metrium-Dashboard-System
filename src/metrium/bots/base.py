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

import time
import threading
import traceback

from metrium import models

SLEEP_TIME = 1.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor """

class Bot(threading.Thread):

    GLOBAL_LOCK = threading.RLock()

    def __init__(self, sleep_time = SLEEP_TIME, name = None, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.sleep_time = sleep_time
        self.name = name or self.__class__.__name__
        self.daemon = True

    def run(self):
        self.active = True

        while self.active:
            Bot.GLOBAL_LOCK.acquire()
            models.Debug.log(
                "Tick operation started in %s" % self.name
            )
            try: self.tick()
            except BaseException as exception:
                lines = traceback.format_exc().splitlines()
                models.Debug.log(
                    "Failed tick due to %s (%s) in %s" %
                    (
                         str(exception),
                         exception.__class__.__name__,
                         self.name
                    ),
                    lines = lines
                )
            finally: Bot.GLOBAL_LOCK.release()
            models.Debug.log("Tick operation ended in %s" % self.name)
            models.Debug.log(
                "Sleeping for %d seconds in %s" %
                (self.sleep_time, self.name)
            )
            time.sleep(self.sleep_time)

    def stop(self):
        self.active = False

    def tick(self):
        pass
