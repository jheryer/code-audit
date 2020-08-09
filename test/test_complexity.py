import unittest
from complexity import get_complexity_from_file_content_processing_frame
import pandas as pd
from pandas.testing import assert_frame_equal


def _build_mock_content_file_frame():
    return pd.DataFrame({
        "file_name": ['/test/test.txt', '/test/test.txt', '/test/test.txt'],
        "line": [' a', '    a', '      a'],
        "line_number": [1, 2, 3],
    })


def _build_mock_content_file_frame_with_comments():
    return pd.DataFrame({
        "file_name": ['/test/test.txt', '/test/test.txt', '/test/test.txt', '/test/test.txt',
                      '/test/test.txt', '/test/test.txt'],
        "line": [' a', '    a', '#  comment', '// comment', '/* comment */', '      a'],
        "line_number": [1, 2, 3, 4, 5, 6],
    })


def _build_mock_content_file_frame_with_comments_and_empty_lines():
    return pd.DataFrame({
        "file_name": ['/test/test.txt', '/test/test.txt', '/test/test.txt', '/test/test.txt',
                      '/test/test.txt', '/test/test.txt', '/test/test.txt', '/test/test.txt'],
        "line": [' a', '    a', '#  comment', '// comment', ' ', '    ', '/* comment */', '      a'],
        "line_number": [1, 2, 3, 4, 5, 6, 7],
    })


class MyTestCase(unittest.TestCase):

    # noinspection PyMethodMayBeStatic
    def test_given_content_file_data_frame_then_source_data_frame_should_be_correct(self):
        mock_content_file_frame = _build_mock_content_file_frame()
        result = get_complexity_from_file_content_processing_frame(mock_content_file_frame, "/test/")
        expected = pd.DataFrame({
            'file_name': ['test.txt'],
            'lines': [3],
            'indents': [11],
            'complexity': [3.666667]
        })
        assert_frame_equal(expected, result)

    # noinspection PyMethodMayBeStatic
    def test_given_content_file_with_comments_then_data_frame_then_source_data_frame_should_be_correct(self):
        mock_content_file_frame = _build_mock_content_file_frame_with_comments()
        result = get_complexity_from_file_content_processing_frame(mock_content_file_frame, "/test/")
        expected = pd.DataFrame({
            'file_name': ['test.txt'],
            'lines': [3],
            'indents': [11],
            'complexity': [3.666667]
        })
        print(expected)
        print(result)
        assert_frame_equal(expected, result)

    # noinspection PyMethodMayBeStatic
    def test_given_content_file_with_comments_and_empty_lines_then_data_frame_then_source_data_frame_should_be_correct(
            self):
        mock_content_file_frame = _build_mock_content_file_frame_with_comments_and_empty_lines()
        result = get_complexity_from_file_content_processing_frame(mock_content_file_frame, "/test/")
        expected = pd.DataFrame({
            'file_name': ['test.txt'],
            'lines': [3],
            'indents': [11],
            'complexity': [3.666667]
        })
        print(expected)
        print(result)
        assert_frame_equal(expected, result)


if __name__ == '__main__':
    unittest.main()
