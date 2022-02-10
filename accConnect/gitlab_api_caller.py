"""
Calls GitLab API for group/subgroup/repositories endpoints.
"""

import gitlab

wizards_group_id = 16050998

gl = gitlab.Gitlab(
    url="https://gitlab.com",
    private_token="glpat-ksDCwhxBhC-CYMpppDM8",
)


class GitLabAPICaller:
    """
    Calls GitLab API for group/subgroup/repositories endpoints.

    Docs: https://python-gitlab.readthedocs.io/en/stable
    """

    def __init__(self, id=wizards_group_id):
        self.group_ = gl.groups.get(id)
        self.projects_ = self.group_.projects.list()
        self.users_ = self.group_.members_all.list(all=True)

    @property
    def group(self):
        return self.group_

    @property
    def projects(self):
        return self.projects_

    @property
    def users(self):
        return self.users_
