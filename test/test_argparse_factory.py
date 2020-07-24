import unittest
from argparse_factory import parse_cf_args


class MyTestCase(unittest.TestCase):
    def test_argument_parsing(self):
        args = parse_cf_args(["--repo", "/foo/bar"])
        self.assertEqual(args.repo, "/foo/bar")


if __name__ == '__main__':
    unittest.main()
