import unittest
from argparse_factory import parse_vcaudit_args


class MyTestCase(unittest.TestCase):
    def test_given_argument_repo_then_value_should_exist(self):
        args = parse_vcaudit_args(["--repo", "/foo/bar", "--audit", "frequency"])
        self.assertEqual(args.repo, "/foo/bar")
        self.assertEqual(args.audit, "frequency")

    def test_given_arguments_repo_and_limit_then_values_should_exist(self):
        args = parse_vcaudit_args(["--repo", "/foo/bar", "--limit", "1", "--audit", "frequency"])
        self.assertEqual(args.repo, "/foo/bar")
        self.assertEqual(args.audit, "frequency")
        self.assertEqual(args.limit, "1")


if __name__ == '__main__':
    unittest.main()
