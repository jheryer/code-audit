from typing import Text, List
import pandas as pd
from process import data_frame_from_file_list


def get_complexity_by_file(file: Text, query_root: Text):
    return get_complexity_by_file_list([file], query_root)


def get_complexity_by_file_list(file_list: List, query_root: Text):
    file_data_frame = data_frame_from_file_list(file_list)
    return get_complexity_from_file_content_processing_frame(file_data_frame, query_root)


def get_complexity_from_file_content_processing_frame(data_frame, query_root):
    # TODO: processing_frame validation

    processing_frame = pd.DataFrame.copy(data_frame)
    _clean_file_name(processing_frame, query_root)
    _tabs_not_spaces(processing_frame)
    _inject_line_numbers(processing_frame)
    _inject_comment_empty(processing_frame)
    _inject_indentation(processing_frame)
    complexity_frame = _create_complexity_frame(processing_frame)
    return complexity_frame


def _create_complexity_frame(file_frame):
    filtered_file_frame = file_frame.drop(file_frame[file_frame['is_comment'] | file_frame['is_empty']].index)
    filtered_file_frame.reindex()
    complexity_frame = filtered_file_frame.groupby('file_name')['indent'].agg(['count', 'sum'],
                                                                              as_index=True).reset_index()
    complexity_frame.columns = ['file_name', 'lines', 'indents']
    complexity_frame.head()
    complexity_frame.reset_index()
    complexity_frame['complexity'] = complexity_frame['indents'] / complexity_frame['lines']
    complexity_frame.head(1)
    return complexity_frame


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
    content['is_comment'] = content['line'].str.match(r'^ *(#|//|(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)).*')
    content['is_empty'] = content['line'].str.replace(" ", "").str.len() == 0
    content.head(1)


def _inject_indentation(content):
    content['indent'] = content['line'].str.len() - content['line'].str.lstrip().str.len()
    content.head(1)
