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
    'tipificacao_resumida',
    'amparo_legal',
    'tipificacao_enquadramento',
    'gravidade',
    'infrator',
    'pontuacao',
    'penalidade',
    'competencia',
    'constatacao_infracao'
    'quando_autuar',
    'quando_nao_autuar',
    'informacoes_complementares',
    ]
new_df = pd.DataFrame(columns=new_df_columns)

for sheet_name in sheet_names:
    print(f'-------Avaliando {sheet_name} de {len(sheet_names)}-------')
    new_df_dict = {}
    df = pd.read_excel('so_table.xlsx', sheet_name=sheet_name)

    for column in range(0, column_len:= len(df.columns)):
        print(f'Avaliando coluna {column} de {column_len}, da {sheet_name}.')
        content = df.iloc[:,column]
        if content[0] == 'FICHA DE FISCALIZAÇÃO':
            new_df_dict['tipificacao_resumida'] = remove_new_line_field(content[1])
            new_df_dict['amparo_legal'] = remove_new_line_field(content[2])
            new_df_dict['tipificacao_enquadramento'] = remove_new_line_field(content[3])
            new_df_dict['gravidade'] = remove_new_line_field(content[4])
            new_df_dict['infrator'] = remove_new_line_field(content[5])
            new_df_dict['pontuacao'] = remove_new_line_field(content[6])
            new_df_dict['quando_autuar'] = remove_new_line_text(content[8])
            new_df.loc[len(new_df)] = new_df_dict
        if not pd.isna(content[4]) and content[4].startswith('Penalidade:'):
            last_df_row = new_df.loc[len(new_df)-1]
            last_df_row['penalidade'] = remove_new_line_field(content[4])
            last_df_row['competencia'] = remove_new_line_field(content[5])
            last_df_row['constatacao_infracao'] = remove_new_line_field(content[6])
            last_df_row['quando_nao_autuar'] = remove_new_line_field(content[8])
            import ipdb; ipdb.set_trace(context=10)
        elif content[0] == 'Informações Complementares:':
            last_df_row = new_df.loc[len(new_df)-1]
            last_df_row['informacoes_complementares'] = remove_new_line_field(content[1])
