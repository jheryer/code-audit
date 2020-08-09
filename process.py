import subprocess
import glob
import pandas as pd
from typing import List, Text

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def run(args: List) -> List:
    if not args:
        raise Exception("Arguments must be provided")
    return subprocess.check_output(args, universal_newlines=True).splitlines()


def files_in_path(args: Text) -> List:
    if not args:
        raise Exception("Arguments must be provided")

    file_list = glob.glob(args, recursive=True)

    if not file_list:
        return []
    return file_list


def data_frame_from_file(file: Text):
    if not file:
        raise Exception("File must be provided")

    file_data_frame = pd.read_csv(file, encoding='latin1', sep='\n', skip_blank_lines=False, names=['line'])
    file_data_frame.insert(0, 'file_name', file)
    return file_data_frame


def data_frame_from_file_list(file_list: List):
    content_dataframe = []
    for file in file_list:
        file_df = data_frame_from_file(file)
        content_dataframe.append(file_df)
    return pd.concat(content_dataframe)
