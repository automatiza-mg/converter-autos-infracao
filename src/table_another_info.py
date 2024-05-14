# import ipdb; ipdb.set_trace(context=10)
import pandas as pd
from .utils import (
    remove_new_line_text,
)

def get_table_another_info(df, new_df_dict, sheet_name):

    for column in range(0, column_len:= len(df.columns)):
        print(f'Avaliando coluna {column + 1} de {column_len} da planilha {sheet_name}')
        content = df.iloc[:,column]

        if column == 0:
            new_df_dict['sheet'][-1] += f' / {sheet_name}'
            new_df_dict['informacoes_complementares'].append(remove_new_line_text(content[1]))
        elif column == 0 and not content.name.startswith('Unnamed:'):
            new_df_dict['quando_autuar'][-1] += f' {remove_new_line_text(content.name)}'
        elif column == 1 and not content.name.startswith('Unnamed:'):
            new_df_dict['quando_nao_autuar'][-1] += f' {remove_new_line_text(content.name)}'
        elif column == 2 and not content.name.startswith('Unnamed:'):
            new_df_dict['definicoes_procedimentos'][-1] += f' {remove_new_line_text(content.name)}'
        elif column == 2 and not content.name.startswith('Unnamed:'):
            new_df_dict['exemplos_campo_observacoes_ait'][-1] += f' {remove_new_line_text(content.name)}'
    return None
