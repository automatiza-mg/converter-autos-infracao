

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




# meu index é o último
# preciso ir dele + 1 até o infinito

# mas eu posso usar o mesmo objeto

# valor inicial do range index + 1 se o index existir, caso contrário index
# final, caso

# se o proximo index existir é pq tem outra tabela
# se o proximo index não existir não tem tabela
# valor final index
# se o próximo index existir o final é próximo index
# se o próximo index não existir vou até o final da tabela + 1
