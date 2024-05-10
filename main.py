import pandas as pd

df = pd.read_excel('so_table.xlsx', sheet_name='Table 1')

def remove_new_line(text):
    text_list = text.split(':')[-1].split('\n')
    final_text = [item for item in text_list if item]
    return ' '.join(final_text)

new_df = {}
for column in range(0, len(df.columns)):
    content = df.iloc[:,0]
    if df.iloc[:,0][0] == 'FICHA DE FISCALIZAÇÃO':
        new_df['tipificacao_resumida'] = remove_new_line(content[1])
        new_df['amparo_legal'] = remove_new_line(content[2])
        new_df['tipificacao_enquadramento'] = remove_new_line(content[3])
        new_df['gravidade'] = remove_new_line(content[4])
        new_df['infrator'] = remove_new_line(content[5])
        new_df['pontuacao'] = remove_new_line(content[6])
        new_df['quando_autuar'] = remove_new_line(content[8])
        import ipdb; ipdb.set_trace(context=10)
