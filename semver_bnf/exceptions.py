

class InvalidSemver(Exception):
    def __init__(self, semver_string):
        self.message = f"invalid semantic version: {semver_string}"
        super().__init__(self.message)