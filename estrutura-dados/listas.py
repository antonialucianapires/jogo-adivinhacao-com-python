"""
Listas

- permite armazenar um conjunto de itens em uma única variável
- os itens são armazenados de forma sequencial
- cada valor, ou item, na lista tem sua posição identificada por um índice
- o índice do primeiro valor é zero e a cada item inserido este valor é incrementado
- listas são MUTÁVEIS, ou seja, elas podem ser modificadas após a criação
- listas são iteráveis
- listas, no python, tem a característica de serem heterogenias, o que significa
poder armazenar items com tipos diferentes (int, string, etc)

"""

nomes = ['Antonia', 'Luciana']
print('lista sem alterações: ', nomes)

tipagemVariavel = type(nomes)
print('tipo: ', tipagemVariavel)

tamanhoDaLista = len(nomes)
print('tamanho: ', tamanhoDaLista)

primeiroItem = nomes[0];
print('primeiro da lista: ', primeiroItem)

# alterar o primeiro item da lista
nomes[0] = "Julia"

print('lista com primeiro nome alterado: ', nomes)

# adicionar item no final da lista
nomes.append('João')
print('lista com novo item incluído no final: ', nomes)

# lista com um item incluído no início da lista
nomes.insert(0, 'Roberta')
print('lista com novo item incluído no início: ', nomes)

# lista com um item incluído no meio da lista (índice 2)
nomes.insert(2, 'Maria')
print('lista com novo item incluído no meio: ', nomes)

# remover item da lista pelo valor
# neste caso, por trás do método remove, a lista é iterada até encontrar o valor
nomes.remove('Maria')
print('lista sem o item maria: ', nomes)

# remover item da lista pelo índice do item
nomes.pop(2)
print('lista sem o item Luciana: ', nomes)

# se tentar remover um item por um index que não existe, será lançado o seguinte
# erro IndexError: pop index out of range

# lista com valores de tipos diferentes
pessoas = ['João', 30, 1.70]
print('lista com valores de tipos diferentes: ', pessoas)
