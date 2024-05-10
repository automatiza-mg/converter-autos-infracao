import pandas as pd

def remove_new_line(text):
    text_list = text.split(':')[-1].split('\n')
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
    'quando_autuar',
    'penalidade',
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
            new_df_dict['tipificacao_resumida'] = remove_new_line(content[1])
            new_df_dict['amparo_legal'] = remove_new_line(content[2])
            new_df_dict['tipificacao_enquadramento'] = remove_new_line(content[3])
            new_df_dict['gravidade'] = remove_new_line(content[4])
            new_df_dict['infrator'] = remove_new_line(content[5])
            new_df_dict['pontuacao'] = remove_new_line(content[6])
            new_df_dict['quando_autuar'] = remove_new_line(content[8])
            new_df.loc[len(new_df)] = new_df_dict
        if content[4].startswith('Penalidade:'):
            last_df_row = new_df.loc[len(new_df)-1]
            last_df_row['penalidade'] = remove_new_line(content[4])
        elif content[0] == 'Informações Complementares:':
            last_df_row = new_df.loc[len(new_df)-1]
            last_df_row['informacoes_complementares'] = remove_new_line(content[1])
            import ipdb; ipdb.set_trace(context=10)
