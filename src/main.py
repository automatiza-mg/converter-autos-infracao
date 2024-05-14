import pandas as pd
from .table_main_content import get_table_main_content
from .table_another_info import get_table_another_info
from .utils import (
    build_new_df_dict,
)

excel_file = pd.ExcelFile('so_table.xlsx')
sheet_names = excel_file.sheet_names

def convert_all_content_to_dict(sheet_names):

    new_df_dict = build_new_df_dict()

    for sheet_name in sheet_names:
        print(f'-------Avaliando {sheet_name} de {len(sheet_names)}-------')
        df = pd.read_excel('so_table.xlsx', sheet_name=sheet_name)

        if len(first_column:= df.iloc[:,0]) > 0 and first_column[0] == 'FICHA DE FISCALIZAÇÃO':
            if sheet_name == 'Table 9':
                break
            indexes = [i for i, item in enumerate(first_column) if item == 'FICHA DE FISCALIZAÇÃO']
            get_table_main_content(df, new_df_dict, sheet_name, indexes)
        elif len(first_column[0]) > 0 and first_column[0] == 'Informações Complementares:':
            get_table_another_info(df, new_df_dict, sheet_name)
    return new_df_dict

if __name__ == '__main__':
    import ipdb; ipdb.set_trace(context=10)
    new_df_dict = convert_all_content_to_dict(sheet_names)
    for key, item in new_df_dict.items():
        print(key, ' - ', len(item))
    new_df = pd.DataFrame(new_df_dict)
    new_df.to_csv('multas.csv')
