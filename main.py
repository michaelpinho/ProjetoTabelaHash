from tabela_hash_dupla import TabelaHashDupla, Objeto

tabela = TabelaHashDupla(tamanho=100)

objeto1 = Objeto(chave="abcde", valor="Michael")
objeto2 = Objeto(chave="fghij", valor="Atividade")
objeto3 = Objeto(chave="klmno", valor="Estrutura")
objeto4 = Objeto(chave="pqrst", valor="Dados")

tabela.inserir(objeto1)
tabela.inserir(objeto2)
tabela.inserir(objeto3)
tabela.inserir(objeto4)

#O programa deve imprimir "Michael", os índices da tabela e os valores dos objetos em cada índice.
resultado = tabela.buscar("abcde")
if resultado:
    print(resultado.valor)
else:
    print("Chave ainda não existe.")

tabela.imprimir_tabela()