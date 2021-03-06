from analyzer.Builds.Build import Build
from analyzer.Cacher.CacherBase import CacherBase
from typing import List


class BuildCache(CacherBase):

    def __init__(self, repo_path, test=False):
        super().__init__(repo_path, 'builds.cache', test=test)

    def create(self, obj_to_cache: List[Build], override=True):
        serializable = [b.dict() for b in obj_to_cache]
        return super().create(serializable, override)

    def restore(self, default=None):
        builds_json = super().restore(default)
        return [Build.from_dict(b) for b in builds_json]
