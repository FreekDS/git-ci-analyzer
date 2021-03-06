from typing import List

from analyzer.AntiPatterns.AntiPattern import AntiPattern
from analyzer.Builds.Build import Build
from analyzer.config import BROKEN_RELEASE


class BrokenRelease(AntiPattern):
    RELEASE_NAMES = ["main", "master", "my-master"]

    def __init__(self, builds: List[Build], custom_release_branches: List[str] or None = None, default_branch=None):
        super().__init__(builds, BROKEN_RELEASE)
        self.builds = self.sort_chronologically()
        if custom_release_branches:
            self.custom_branches = custom_release_branches
        else:
            self.custom_branches = []
        if default_branch:
            self.custom_branches.append(default_branch)

    def get_release_branch_builds(self):
        filtered_builds = {}
        for wf, builds in self.builds.items():
            filtered = list(
                filter(
                    lambda build: build.branch in self.RELEASE_NAMES + self.custom_branches,
                    builds
                )
            )
            if filtered:
                filtered_builds[wf] = filtered
        return filtered_builds

    @staticmethod
    def get_failing(release_builds):
        failing_builds = {}
        for wf, builds in release_builds.items():
            filtered = list(
                filter(
                    lambda build: build.state in ['failure', 'errored', 'failed'],
                    builds
                )
            )
            failing_builds[wf] = filtered
        return failing_builds

    def detect(self) -> dict:
        all_release_builds = self.get_release_branch_builds()
        failing_releases = self.get_failing(all_release_builds)
        results = {}
        for wf, builds in failing_releases.items():
            results[wf] = {}
            results[wf]['data'] = list()
            for build in builds:
                results[wf]['data'].append(
                    {
                        'started_at': build.started_at,
                        'used_tool': build.used_tool,
                        'number': build.number
                    }
                )
            if builds:
                results[wf]["tool"] = builds[0].used_tool
            results[wf]["release_build_count"] = len(all_release_builds.get(wf, 0))
        return results
