import pandas as pd
from git import change_frequency_command
from collections import Counter


def _remove_empty_strings(file_list):
    return list(filter(None, file_list))


def change_frequency(path, limit, run):
    if not path:
        raise Exception("Provided path is not valid or empty")

    if not callable(run):
        raise Exception("Provided run is not callable")

    file_list = run(change_frequency_command(path))
    file_list = _remove_empty_strings(file_list)
    unique_file_list = list(Counter(file_list).keys())
    unique_file_count = list(Counter(file_list).values())

    print(limit)

    data_frame = {
        "frequency": unique_file_count if limit is None else unique_file_count[0:int(limit)],
        "file": unique_file_list if limit is None else unique_file_list[0:int(limit)]
    }

    fc_model = pd.DataFrame(data_frame)
    return fc_model
