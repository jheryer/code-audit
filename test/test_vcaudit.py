from unittest import TestCase, mock, main
from vcaudit import find_cf


class CFTestCase(TestCase):
    # noinspection PyMethodMayBeStatic
    def test_given_a_path_assert_change_frequency_was_called(self):
        with mock.patch('vcaudit.version_control') as patched_function:
            find_cf('test', 2)

        patched_function.change_frequency.assert_called_once()


if __name__ == '__main__':
    main()
