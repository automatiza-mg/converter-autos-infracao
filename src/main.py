import pandas as pd
from .table_main_content import get_table_main_content
from .utils import (
    remove_new_line_text,
)

excel_file = pd.ExcelFile('so_table.xlsx')
sheet_names = excel_file.sheet_names

def convert_all_content_to_dict(sheet_names):
    for sheet_name in sheet_names:
        print(f'-------Avaliando {sheet_name} de {len(sheet_names)}-------')
        df = pd.read_excel('so_table.xlsx', sheet_name=sheet_name)

        if len(first_column:= df.iloc[:,0]) > 0 and first_column[0] == 'FICHA DE FISCALIZAÇÃO':
            indexes = [i for i, item in enumerate(first_column) if item == 'FICHA DE FISCALIZAÇÃO']
            new_df_dict = get_table_main_content(df, sheet_name, indexes)
        elif len(first_column[0]) > 0 and first_column[0] == 'Informações Complementares:':
            new_df_dict['sheet'][-1] += f' / {sheet_name}'
            new_df_dict['informacoes_complementares'].append(remove_new_line_text(first_column[1]))
            # if sheet_name == 'Table 2':
            #     import ipdb; ipdb.set_trace(context=10)
            #     new_df = pd.DataFrame(new_df_dict)
            #     new_df.to_csv('teste.csv')
    return new_df_dict
