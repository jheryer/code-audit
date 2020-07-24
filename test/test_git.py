import unittest
import git


class GitModuleTestCase(unittest.TestCase):
    def test_given_a_path_cf_command_should_be_valid(self):
        expected = ['git', '-C', '/foo/bar', 'log', '--format=format:', '--name-only']
        result = git.change_frequency_command("/foo/bar")
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test_given_empty_path_cf_command_should_be_valid(self):
        expected = ['git', 'log', '--format=format:', '--name-only']
        result = git.change_frequency_command("")
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)

    def test_given_current_path_cf_command_should_be_valid(self):
        expected = ['git', 'log', '--format=format:', '--name-only']
        result = git.change_frequency_command("./")
        self.assertCountEqual(result, expected)
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
