import pandas as pd

excel_file = pd.ExcelFile('so_table.xlsx')
sheet_names = excel_file.sheet_names

super_count = 0
for sheet_name in sheet_names:
    print(f'-------Avaliando {sheet_name} de {len(sheet_names)}-------')
# df = pd.read_excel('so_table.xlsx', sheet_name='Table 26')
    df = pd.read_excel('so_table.xlsx', sheet_name=sheet_name)

    for column in range(0, column_len:= len(df.columns)):
        # import ipdb; ipdb.set_trace(context=10)
        content = df.iloc[:,column]

        count = 0
        if len(content) > 0 and content[0] == 'FICHA DE FISCALIZAÇÃO':
            for text in content:
                if text == 'FICHA DE FISCALIZAÇÃO':
                    count += 1
        if count > 1:
            super_count += 1
            print(f'{sheet_name} tem {count} folhas.-------------------------{super_count}')
