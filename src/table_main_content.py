# import ipdb; ipdb.set_trace(context=10)

import pandas as pd
from utils import (
    remove_new_line_field,
    remove_new_line_text,
    ListWithGet,
)

def get_table_main_content(df, new_df_dict, sheet_name, indexes):

    for i, index in enumerate(indexes):
        for column in range(0, column_len:= len(df.columns)):

            print(f'Avaliando coluna {column + 1} de {column_len} da {i+1}º tabela da planilha {sheet_name}')
            content = df.iloc[:,column]
            next_i = ListWithGet(indexes)[i+1]

            if content[index] == 'FICHA DE FISCALIZAÇÃO':
                new_df_dict['sheet'].append(sheet_name)
                new_df_dict['tipificacao_resumida'].append(remove_new_line_field(content[index + 1]))
                new_df_dict['amparo_legal'].append(remove_new_line_field(content[index + 2]))
                new_df_dict['tipificacao_enquadramento'].append(remove_new_line_field(content[index + 3]))
                new_df_dict['gravidade'].append(remove_new_line_field(content[index + 4]))
                new_df_dict['infrator'].append(remove_new_line_field(content[index + 5]))
                new_df_dict['pontuacao'].append(remove_new_line_field(content[index + 6]))
                new_df_dict['quando_autuar'].append(remove_new_line_text(content[index + 8]))
                for text in range(index + 9, next_i + 1):
                    if not pd.isna(content[text]) and content[text] != 'Informações Complementares:':
                        new_df_dict['quando_autuar'][-1] += f' {remove_new_line_text(content[text])}'
                    elif content[text] == 'Informações Complementares:':
                        new_df_dict['informacoes_complementares'].append(remove_new_line_field(content[text + 1]))
            elif len(content) > 3 and not pd.isna(content[index + 4]) and content[index + 4].startswith('Penalidade:'):
                new_df_dict['penalidade'].append(remove_new_line_field(content[index + 4]))
                new_df_dict['competencia'].append(remove_new_line_field(content[index + 5]))
                new_df_dict['constatacao_infracao'].append(remove_new_line_field(content[index + 6]))
                new_df_dict['quando_nao_autuar'].append(remove_new_line_text(content[index + 8]))
                for text in range(index + 9, next_i + 1):
                    if not pd.isna(content[text]):
                        new_df_dict['quando_nao_autuar'][-1] += f' {remove_new_line_text(content[text])}'
            elif len(content) > 3 and not pd.isna(content[index + 4]) and content[index + 4].startswith('Medida Administrativa'):
                new_df_dict['medida_administrativa'].append(remove_new_line_field(content[index + 4]))
                new_df_dict['definicoes_procedimentos'].append(remove_new_line_text(content[index + 8]))
                for text in range(index + 9, next_i + 1):
                    if not pd.isna(content[text]):
                        new_df_dict['definicoes_procedimentos'][-1] += f' {remove_new_line_text(content[text])}'
            elif len(content) > 1 and not pd.isna(content[index + 1]) and content[index + 1].startswith('Código do Enquadramento:'):
                new_df_dict['codigo_enquadramento'].append(remove_new_line_field(content[index + 1]))
                new_df_dict['pode_configurar_crime_transito'].append(remove_new_line_field(content[index + 4]))
                new_df_dict['exemplos_campo_observacoes_ait'].append(remove_new_line_text(content[index + 8]))
                for text in range(index + 9, next_i + 1):
                    if not pd.isna(content[text]):
                        new_df_dict['exemplos_campo_observacoes_ait'][-1] += f' {remove_new_line_text(content[text])}'
    return None
