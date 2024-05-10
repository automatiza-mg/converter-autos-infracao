import pandas as pd

def remove_new_line_field(text):
    text_list = text.split(':')[-1].split('\n')
    final_text = [item for item in text_list if item]
    return ' '.join(final_text)

def remove_new_line_text(text):
    text_list = text.split('\n')
    final_text = [item for item in text_list if item]
    return ' '.join(final_text)

excel_file = pd.ExcelFile('so_table.xlsx')
sheet_names = excel_file.sheet_names
new_df_columns = [
    'sheet',
    'tipificacao_resumida',
    'codigo_enquadramento',
    'amparo_legal',
    'tipificacao_enquadramento',
    'gravidade',
    'penalidade',
    'medida_administrativa',
    'pode_configurar_crime_transito',
    'infrator',
    'competencia',
    'pontuacao',
    'constatacao_infracao',
    'quando_autuar',
    'quando_nao_autuar',
    'definicoes_procedimentos',
    'exemplos_campo_observacoes_ait',
    'informacoes_complementares',
    ]
new_df_dict = {key: [] for key in new_df_columns}

new_df = pd.DataFrame(columns=new_df_columns)

for sheet_name in sheet_names:
    print(f'-------Avaliando {sheet_name} de {len(sheet_names)}-------')
    df = pd.read_excel('so_table.xlsx', sheet_name=sheet_name)

    for column in range(0, column_len:= len(df.columns)):
        if sheet_name == 'Table 10':
            new_df = pd.DataFrame(new_df_dict)
            import ipdb; ipdb.set_trace(context=10)

        print(f'Avaliando coluna {column + 1} de {column_len} da {sheet_name}')
        content = df.iloc[:,column]


        if content[0] == 'FICHA DE FISCALIZAÇÃO':
            new_df_dict['sheet'].append(sheet_name)
            new_df_dict['tipificacao_resumida'].append(remove_new_line_field(content[1]))
            new_df_dict['amparo_legal'].append(remove_new_line_field(content[2]))
            new_df_dict['tipificacao_enquadramento'].append(remove_new_line_field(content[3]))
            new_df_dict['gravidade'].append(remove_new_line_field(content[4]))
            new_df_dict['infrator'].append(remove_new_line_field(content[5]))
            new_df_dict['pontuacao'].append(remove_new_line_field(content[6]))
            new_df_dict['quando_autuar'].append(remove_new_line_text(content[8]))
            for text in range(9, len(content) - 1):
                if not pd.isna(content[text]) and content[text] != 'Informações Complementares:':
                    new_df_dict['quando_autuar'][-1] += f' {remove_new_line_text(content[text])}'
                elif content[text] == 'Informações Complementares:':
                    new_df_dict['informacoes_complementares'].append(remove_new_line_field(content[text + 1]))
        elif content[0] == 'Informações Complementares:':
            new_df_dict['sheet'][-1] += f' / {sheet_name}'
            new_df_dict['informacoes_complementares'].append(remove_new_line_text(content[1]))
        elif len(content) > 3 and not pd.isna(content[4]) and content[4].startswith('Penalidade:'):
            new_df_dict['penalidade'].append(remove_new_line_field(content[4]))
            new_df_dict['competencia'].append(remove_new_line_field(content[5]))
            new_df_dict['constatacao_infracao'].append(remove_new_line_field(content[6]))
            new_df_dict['quando_nao_autuar'].append(remove_new_line_text(content[8]))
            for text in range(9, len(content) - 1):
                if not pd.isna(content[text]):
                    new_df_dict['quando_nao_autuar'][-1] += f' {remove_new_line_text(content[text])}'
        elif len(content) > 3 and not pd.isna(content[4]) and content[4].startswith('Medida Administrativa'):
            new_df_dict['medida_administrativa'].append(remove_new_line_field(content[4]))
            new_df_dict['definicoes_procedimentos'].append(remove_new_line_text(content[8]))
            for text in range(9, len(content) - 1):
                if not pd.isna(content[text]):
                    new_df_dict['definicoes_procedimentos'][-1] += f' {remove_new_line_text(content[text])}'
        elif len(content) > 1 and not pd.isna(content[1]) and content[1].startswith('Código do Enquadramento:'):
            new_df_dict['codigo_enquadramento'].append(remove_new_line_field(content[1]))
            new_df_dict['pode_configurar_crime_transito'].append(remove_new_line_field(content[4]))
            new_df_dict['exemplos_campo_observacoes_ait'].append(remove_new_line_text(content[8]))
            for text in range(9, len(content) - 1):
                if not pd.isna(content[text]):
                    new_df_dict['exemplos_campo_observacoes_ait'][-1] += f' {remove_new_line_text(content[text])}'
