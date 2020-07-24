import pandas as pd
from git import change_frequency_command
from collections import Counter


def _remove_empty_strings(file_list):
    return list(filter(None, file_list))


def _get_unique(file_list):
    return list(set(file_list))


def change_frequency(path, run):
    file_list = run(change_frequency_command(path))
    file_list = _remove_empty_strings(file_list)

    unique_file_list = list(Counter(file_list).keys())
    unique_file_count = list(Counter(file_list).values())

    data_frame = {
        "frequency": unique_file_count,
        "file": unique_file_list
    }

    fc_model = pd.DataFrame(data_frame)
    return fc_model
