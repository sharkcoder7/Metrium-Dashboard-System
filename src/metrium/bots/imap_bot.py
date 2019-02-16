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
import imaplib

import email.utils
import email.header

from metrium import models

from . import base

SLEEP_TIME = 30.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

ATOM_SPECIALS = "(){ %*\""
""" String sequence containing the complete set of
characters considered to be special in the IMAP protocol,
this characters need to be escaped """

class ImapBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)

    def tick(self):
        imap = self.get_imap()

        try:
            folders = self.get_folders()
            self.outdate_folders(folders)
            for folder in folders: self.update_folder(imap, folder = folder)
        finally:
            imap.logout()

    def get_folders(self):
        config = models.PendingConfig.get()
        folders = config.folders
        return folders

    def get_imap(self):
        config = models.MailConfig.get()
        imap = imaplib.IMAP4_SSL(config.host)
        imap.login(config.username, config.password)
        return imap

    def outdate_folders(self, folders):
        outdated = models.Mail.find(folder = {"$nin" : folders})
        for mail in outdated: mail.delete()

    def update_folder(self, imap, folder = "inbox", limit = -1):
        folder_e = self._encode_folder(folder)
        result, data = imap.select(folder_e, readonly = True)
        if not result == "OK": return

        try:
            result, data = imap.uid("SEARCH", "1:*")
            if not result == "OK": return

            ids = data[0]
            id_list = ids.split()
            id_list.reverse()

            if not limit == -1: id_list = id_list[:limit]
            self.sync_folder(imap, id_list, folder)
        finally:
            imap.close()

    def sync_folder(self, imap, id_list, folder):
        mails = models.Mail.find(folder = folder)

        for mail in mails:
            if mail.uid in id_list: continue
            mail.delete()

        for mail_id in id_list:
            self.save_mail(imap, mail_id, folder)

    def save_mail(self, imap, mail_id, folder):
        mail = models.Mail.find(uid = mail_id, folder = folder)
        if mail: return

        _result, data = imap.uid("FETCH", mail_id, "(rfc822)")
        contents = data[0][1]
        message = email.message_from_string(contents)

        message_id = message.get("message-id", None)
        message_id = message_id and message_id.strip()
        message_id = self.decode_header(message_id)

        _from = message.get("from", None)
        _from = _from and _from.strip()
        sender_extra, sender = email.utils.parseaddr(_from)
        sender_extra = self.decode_header(sender_extra)

        date = message.get("date", None)
        date = date and date.strip()
        date = self.decode_header(date)
        date_tuple = email.utils.parsedate(date)
        timestamp = time.mktime(date_tuple)

        subject = message.get("subject", None)
        subject = subject and subject.strip()
        subject = self.decode_header(subject)

        mail = models.Mail.find(message_id = message_id)
        if mail: return

        mail = models.Mail()
        mail.uid = mail_id
        mail.message_id = message_id
        mail.sender = sender
        mail.sender_extra = sender_extra
        mail.folder = folder
        mail.date = timestamp
        mail.subject = subject
        mail.save()

    def decode_header(self, value):
        dec = lambda base, charset: base.decode(charset) if charset else base
        partials = email.header.decode_header(value)
        value_d = " ".join([dec(base, charset) for base, charset in partials])
        return value_d

    def _encode_folder(self, name):
        name = name.encode("utf-7")
        if self._needs_quote(name): return self._quote(name)
        return name

    def _needs_quote(self, s):
        if s == "": return 1
        for c in s:
            if c < "\x20" or c > "\x7f": return 1
            if c in ATOM_SPECIALS: return 1
        return 0

    def _quote(self, s):
        return "\"%s\"" % (s.replace("\\", "\\\\").replace("\"", "\\\""),)
