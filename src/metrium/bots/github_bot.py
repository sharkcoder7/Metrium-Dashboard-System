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

from metrium import models

from . import base

SLEEP_TIME = 1200.0
""" The default sleep time to be used by the bots
in case no sleep time is defined in the constructor,
this bot uses a large value as its tick operation is
a lot expensive and should be used with care """

class GithubBot(base.Bot):

    def __init__(self, sleep_time = SLEEP_TIME, *args, **kwargs):
        base.Bot.__init__(self, sleep_time, *args, **kwargs)
        self.api = None

    def tick(self):
        api = self.get_api()
        config = models.GithubConfig.singleton()

        activity = self.activity(api, config)
        contrib = self.contrib(api, config)
        issues = self.issues(api, config)

        commits_total = self.commits_total(api, activity)
        commits_data = self.commits_data(api, activity)
        issues_users = self.issues_users(api, issues)
        commits_users = self.commits_users(api, contrib)

        _github = models.Github.get(raise_e = False)
        if not _github: _github = models.Github()
        _github.commits_total = commits_total
        _github.commits_data = commits_data
        _github.issues_users = issues_users
        _github.commits_users = commits_users
        _github.save()

        pusher = quorum.get_pusher()
        pusher.trigger("global", "github.commits_total", {
            "commits_total" : commits_total
        })
        pusher.trigger("global", "github.commits_data", {
            "commits_data" : commits_data
        })
        pusher.trigger("global", "github.issues_users", {
            "issues_users" : issues_users
        })
        pusher.trigger("global", "github.commits_users", {
            "commits_users" : commits_users
        })

    def activity(self, api, config):
        activity = dict()
        for repo in config.repos:
            owner, repo = repo.split("/", 1)
            item = api.stats_activity_repo(owner, repo)
            activity[repo] = item
        return activity

    def participation(self, api, config):
        participation = dict()
        for repo in config.repos:
            owner, repo = repo.split("/", 1)
            item = api.stats_participation_repo(owner, repo)
            participation[repo] = item
        return participation

    def contrib(self, api, config):
        contrib = dict()
        for repo in config.repos:
            owner, repo = repo.split("/", 1)
            item = api.stats_contrib_repo(owner, repo)
            contrib[repo] = item
        return contrib

    def issues(self, api, config):
        issues = dict()
        for repo in config.repos:
            owner, repo = repo.split("/", 1)
            _issues = api.issues_repo(owner, repo)
            issues[repo] = _issues
        return issues

    def commits_total(self, api, activity):
        count = [0] * 2

        for _repo, item in activity.items():
            if not item: continue
            item_l = len(item)
            current = item[-1]
            previous = item[-2] if item_l > 1 else dict(total = 0)
            current_t = current["total"]
            previous_t = previous["total"]
            count[0] += previous_t
            count[1] += current_t

        return count

    def commits_data(self, api, activity):
        count = [0] * 7

        for _repo, item in activity.items():
            if not item: continue
            item = reversed(item)
            item = list(item)
            item = item[:7]

            for index in quorum.legacy.range(len(item)):
                current = item[index]
                value = current["total"]
                count[index] += value

        count = reversed(count)
        count = list(count)
        return count

    def issues_users(self, api, issues):
        issues_users = dict()

        for _repo, item in issues.items():
            for issue in item:
                assignee = issue["assignee"]
                if not assignee: continue
                user = assignee["login"]
                state = issue["state"]
                if not state in ("open", "closed"): continue
                data = issues_users.get(user, [0, 0, user])
                if state == "open": data[0] += 1
                if state == "closed": data[1] += 1
                issues_users[user] = data

        issues_users = issues_users.values()
        issues_users = list(issues_users)
        issues_users.sort(reverse = True)
        return issues_users

    def commits_users(self, api, contrib):
        commits_users = dict()

        for _repo, item in contrib.items():
            for structure in item:
                author = structure["author"]
                if not author: continue
                user = author["login"]
                weeks = structure["weeks"]
                last = weeks[-1]
                data = commits_users.get(user, [0, 0, user])
                data[0] += last["a"] - last["d"]
                data[1] += last["c"]
                commits_users[user] = data

        commits_users = commits_users.values()
        commits_users = list(commits_users)
        commits_users.sort(reverse = True)
        return commits_users

    def get_api(self):
        if self.api: return self.api
        self.api = models.GithubConfig.get_api()
        return self.api
