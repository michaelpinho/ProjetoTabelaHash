class Objeto:
    #Inicialização do objeto a ser usado na tabela hash dupla.
    def __init__(self, chave, valor):
        self.chave = chave
        self.valor = valor

class TabelaHashDupla:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        #Criação de um vetor com 10 ponteiros para os vetores.
        self.primeiro_nivel = [None] * 10
        #Setando o segundo nível.
        for i in range(10):
            self.primeiro_nivel[i] = [None] * (tamanho // 10)

    def hash_primeiro_nivel(self, chave):
        #Função hash que utiliza o tamanho da tabela e o hash (função do Python).
        return hash(chave) % 10

    def hash_segundo_nivel(self, chave):
        #Função hash que utiliza a soma dos valores dos caracteres da chave.
        soma = sum(ord(c) for c in chave)
        return soma % (self.tamanho // 10)

    def inserir(self, objeto):
        indice_primeiro_nivel = self.hash_primeiro_nivel(objeto.chave)
        indice_segundo_nivel = self.hash_segundo_nivel(objeto.chave)
        #Vai na posição desejada do segundo nível e insere o objeto.
        self.primeiro_nivel[indice_primeiro_nivel][indice_segundo_nivel] = objeto

    def buscar(self, chave):
        indice_primeiro_nivel = self.hash_primeiro_nivel(chave)
        indice_segundo_nivel = self.hash_segundo_nivel(chave)
        objeto = self.primeiro_nivel[indice_primeiro_nivel][indice_segundo_nivel]
        #Vai na posição desejada do segundo nível e retorna o objeto, caso a chave exista.
        if objeto and objeto.chave == chave:
            return objeto
        else:
            return None

    def imprimir_tabela(self):
        for i in range(10):
            for j in range(self.tamanho // 10):
                objeto = self.primeiro_nivel[i][j]
                if objeto:
                    print(f"Índice ({i}, {j}): Chave = {objeto.chave}, Valor = {objeto.valor}")
                else:
                    print(f"Índice ({i}, {j}): Vazio")

