# import ipdb; ipdb.set_trace(context=10)
import json
from ..main import convert_all_content_to_dict


def test_convert_all_content_to_dict():
    file_path = 'src/tests/final_result_until_table_8.json'
    with open(file_path, 'r') as json_file:
        test_result = json.load(json_file)
    sheet_names = [f'Table {i}' for i in range(1, 10)]
    new_df_dict = convert_all_content_to_dict(sheet_names)
    assert new_df_dict == test_result
