import pandas as pd
from table_main_content import get_table_main_content

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

    if sheet_name == 'Table 3':
        import ipdb; ipdb.set_trace(context=10)
    if len(first_column:= df.iloc[:,0]) > 0 and first_column[0] == 'FICHA DE FISCALIZAÇÃO':
        indexes = [i for i, item in enumerate(first_column) if item == 'FICHA DE FISCALIZAÇÃO']
        new_df_dict['sheet'].append(sheet_name)
        get_table_main_content(df, sheet_name, indexes, new_df_dict)
        # elif first_column[0] == 'Informações Complementares:':
    #     new_df_dict['sheet'][-1] += f' / {sheet_name}'
    #     new_df_dict['informacoes_complementares'].append(remove_new_line_text(content[1]))
