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
from . import mail

class Conversation(base.Base):

    sender = dict(
        index = True
    )

    sender_extra = dict(
        index = True
    )

    folder = dict(
        index = True
    )

    date = dict(
        type = float,
        index = True
    )

    subject = dict(
        index = True
    )

    mails = dict(
        type = quorum.references(
            mail.Mail,
            name = "id"
        )
    )

    @classmethod
    def validate_new(cls):
        return super(Conversation, cls).validate_new() + [
            quorum.not_null("sender"),
            quorum.not_empty("sender"),

            quorum.not_null("folder"),
            quorum.not_empty("folder"),

            quorum.not_null("date"),

            quorum.not_null("subject")
        ]

    @classmethod
    def from_mail(cls, mail):
        instance = cls()
        instance.sender = mail.sender
        instance.sender_extra = mail.sender_extra
        instance.folder = mail.folder
        instance.date = mail.date
        instance.subject = mail.get_subject_f()
        instance.mails = []
        return instance

    @classmethod
    def try_create(cls, mail):
        subject = mail.get_subject_f()
        conversation = cls.get(
            subject = subject,
            raise_e = False
        )

        if not conversation:
            conversation = cls.from_mail(mail)

        conversation.mails.append(mail.id)
        conversation.save()

    @classmethod
    def try_delete(cls, mail):
        subject = mail.get_subject_f()
        conversation = cls.get(
            subject = subject,
            raise_e = False
        )

        if not conversation: return

        exists = conversation.mails.contains(mail.id)
        if not exists: return

        conversation.mails.remove(mail.id)
        is_empty = conversation.mails.is_empty()
        if is_empty: conversation.delete()
        else: conversation.save()

    def get_event(self):
        return dict(
            sender = self.sender,
            sender_extra = self.sender_extra,
            folder = self.folder,
            date = self.date,
            subject = self.subject
        )

    def post_create(self):
        base.Base.post_create(self)

        pusher = quorum.get_pusher()
        pusher.trigger("global", "conversation.new", {
            "contents" : self.get_event()
        })

    def pre_delete(self):
        base.Base.pre_delete(self)

        import pending
        pendings = pending.Pending.find(conversation = self.id)
        for pending in pendings: pending.delete()
