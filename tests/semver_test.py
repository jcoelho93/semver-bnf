import unittest
from semver_bnf import SemanticVersion
from semver_bnf.exceptions import InvalidSemver


class TestSemver(unittest.TestCase):
    
    valid_versions = [
        "1.2.3",
        "1.2.0",
        "1.2.3-rc",
        "1.2.32-rc.1",
        "1.2.32-rc.1+build2010",
    ]

    invalid_versions = [
        "1.2",
        "1..2.3",
        "10.10..3",
        "2",
        "v1.2.3"
    ]

    def test_valid_versions(self):
        for version in self.valid_versions:
            try:
                SemanticVersion(version)
            except InvalidSemver:
                self.fail(f"SemanticVersion reported {version} as being invalid!")

    def test_invalid_versions(self):
        for version in self.invalid_versions:
            self.assertRaises(InvalidSemver, SemanticVersion, version)

if __name__ == '__main__':
    unittest.main()