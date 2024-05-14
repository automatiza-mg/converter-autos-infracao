
def build_new_df_dict():
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
    return {key: [] for key in new_df_columns}


def remove_new_line_field(text):
    text_list = text.split(':')[-1].split('\n')
    final_text = [item for item in text_list if item]
    return ' '.join(final_text)

def remove_new_line_text(text):
    text_list = text.split('\n')
    final_text = [item for item in text_list if item]
    return ' '.join(final_text)

class ListWithGet:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return self.data[-1]
