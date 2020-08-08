import unittest
from process import files_in_path, get_content_by_file, get_content_by_file_list


class MyTestCase(unittest.TestCase):

    def test_Given_a_path_return_a_list_of_files(self):
        file_list = files_in_path("/home/jheryer/Projects/python/maat-scripts/**")
        self.assertGreater(len(file_list), 0)

    def test_Given_a_file_return_a_dataframe(self):
        file = "/home/jheryer/Projects/python/maat-scripts/miner/git_interactions.py"
        data_frame = get_content_by_file(file)
        data_frame.info()
        self.assertTrue(True)

    def test_Given_a_list_of_files_return_a_pd_dataframe(self):
        file_list = ["/home/jheryer/Projects/python/maat-scripts/miner/git_interactions.py",
                     ]
        repo = "/home/jheryer/Projects/python/maat-scripts/"
        data_frame = get_content_by_file_list(file_list, repo)
        data_frame.info()
        print(data_frame)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
