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

import hashlib

import quorum

from . import log
from . import base
from . import conversation

SEVERITIES = dict(
    critical = 10,
    major = 20,
    minor = 30,
    trivial = 40
)
""" The map defining the various severity levels and the
corresponding integer based priority value """

class Pending(base.Base):

    priority = dict(
        type = int,
        index = True
    )

    severity = dict(
        index = True
    )

    severity_i = dict(
        type = int,
        index = True
    )

    pre = dict(
        index = True
    )

    description = dict(
        index = True
    )

    author = dict(
        index = True
    )

    folder = dict(
        index = True
    )

    conversation = dict(
        type = quorum.reference(
            conversation.Conversation,
            name = "id"
        )
    )

    @classmethod
    def validate_new(cls):
        return super(Pending, cls).validate_new() + [
            quorum.not_null("priority"),

            quorum.not_null("severity"),
            quorum.not_empty("severity"),

            quorum.not_null("pre"),
            quorum.not_empty("pre"),

            quorum.not_null("description"),
            quorum.not_empty("description"),

            quorum.not_null("folder"),
            quorum.not_empty("folder")
        ]

    @classmethod
    def reset(cls):
        pendings = cls.find()
        for pending in pendings: pending.delete()

    @classmethod
    def get_state(cls):
        events = cls.get_events()
        return {
            "pending.update" : [{
                "pendings" : events
            }]
        }

    @classmethod
    def get_events(cls, count = 10):
        pendings = cls.find(sort = [("severity_i", 1), ("priority", 1)], limit = count)
        return [pending.get_event() for pending in pendings]

    @classmethod
    def get_signature(cls, count = 10):
        signature = hashlib.sha256()
        pendings = cls.find(sort = [("severity_i", 1), ("priority", 1)], limit = count)
        for pending in pendings:
            buffer = pending.get_buffer()
            buffer_s = buffer.encode("utf-8")
            signature.update(buffer_s)
        return signature.hexdigest()

    def pre_create(self):
        base.Base.pre_create(self)

        self.severity_i = SEVERITIES.get(self.severity, 0)

    def post_create(self):
        base.Base.post_create(self)

        log.Log.notify(
            self.description,
            type = "info",
            owner_extra = "pending"
        )

    def post_delete(self):
        base.Base.post_create(self)

        log.Log.notify(
            "Removed: " + self.description,
            type = "warning",
            owner_extra = "pending"
        )

    def get_event(self):
        return dict(
            priority = self.priority,
            severity = self.severity,
            pre = self.pre,
            description = self.description,
            author = self.author
        )

    def get_buffer(self):
        return str(self.priority) + self.pre + self.description + self.author
