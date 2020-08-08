import subprocess
import glob
import pandas as pd
from typing import List, Text

pd.set_option('display.max_columns', None)


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


def get_content_by_file(file: Text):
    if not file:
        raise Exception("File must be provided")

    file_content = pd.read_csv(file, encoding='latin1', sep='\n', skip_blank_lines=False, names=['line'])
    file_content.insert(0, 'file_name', file)
    return file_content


def get_content_by_file_list(file_list: List, repo: Text):
    if not file_list:
        raise Exception("File list must be provided")

    if len(file_list) <= 0:
        raise Exception("File list must not be empty")

    content_dataframe = []
    for file in file_list:
        file_df = get_content_by_file(file)
        content_dataframe.append(file_df)

    content = pd.concat(content_dataframe)
    _clean_file_name(content, repo)
    _tabs_not_spaces(content)
    _inject_line_numbers(content)
    _inject_comment_empty(content)

    return content


def _clean_file_name(content, repo):
    name = 'file_name'
    content.head()
    content[name] = pd.Categorical(content[name])
    content[name] = content[name].str.replace("\\", "/").str.replace(repo, "")


def _tabs_not_spaces(content):
    line = 'line'
    spaces = " " * 4
    content[line] = content[line].fillna("")
    content[line] = content[line].str.replace("\t", spaces)
    content.head(1)


def _inject_line_numbers(content):
    content['line_number'] = content.index + 1
    content.reset_index(drop=True)
    content.head(1)


def _inject_comment_empty(content):
    content['is_comment'] = content['line'].str.match(r'^ *(#|//|/\*|\*).*')
    content['is_empty'] = content['line'].str.replace(" ", "").str.len() == 0
    content.head(1)
