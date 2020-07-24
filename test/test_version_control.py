from unittest import TestCase, mock, main
from version_control import change_frequency
import pandas as pd
from pandas.testing import assert_frame_equal


class VersionControlTestCase(TestCase):
    # noinspection PyMethodMayBeStatic
    def test_given_a_path_and_no_limit_assert_basic_change_frequency(self):
        file_list = ['three', 'two', 'one']

        expected = pd.DataFrame({
            "frequency": [1, 1, 1],
            "file": file_list,
        })

        run_mock = mock.Mock()
        run_mock.return_value = file_list
        result = change_frequency("/path", None, run_mock)
        run_mock.assert_called_once()
        assert_frame_equal(expected, result)

    # noinspection PyMethodMayBeStatic
    def test_given_a_path_and_no_limit_assert_complex_change_frequency(self):
        file_list = ['three', 'two', 'one', 'one', 'one', 'two']

        expected = pd.DataFrame({
            "frequency": [1, 2, 3],
            "file": ['three', 'two', 'one'],
        })

        run_mock = mock.Mock()
        run_mock.return_value = file_list
        result = change_frequency("/path", None, run_mock)
        run_mock.assert_called_once()
        assert_frame_equal(expected, result)

    # noinspection PyMethodMayBeStatic
    def test_given_a_path_and_limit_1_assert_complex_change_frequency(self):
        file_list = ['three', 'two', 'one', 'one', 'one', 'two']

        expected = pd.DataFrame({
            "frequency": [1],
            "file": ['three'],
        })

        run_mock = mock.Mock()
        run_mock.return_value = file_list
        result = change_frequency("/path", 1, run_mock)
        print(result)
        run_mock.assert_called_once()
        assert_frame_equal(expected, result)


if __name__ == '__main__':
    main()
