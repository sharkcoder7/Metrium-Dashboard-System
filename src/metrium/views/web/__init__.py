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

from . import account
from . import base
from . import config
from . import debug
from . import event
from . import github
from . import log
from . import omni

from .account import list_accounts, list_accounts_json, new_account, create_account,\
    show_account, show_account_s, edit_account, update_account, delete_account
from .base import index, about, signin, login, logout, state, board, video
from .config import base_config, basic_config, do_basic_config, mail_config,\
    do_mail_config, pending_config, do_pending_config, omni_config, do_omni_config
from .debug import list_debug, list_debug_json, show_debug
from .event import base_events, video_event, do_video_event
from .github import github_oauth
from .log import list_logs, list_logs_json, new_log, create_log
from .omni import omni_callback
from .settings import settings, import_a, import_do, export_do, reset_do
