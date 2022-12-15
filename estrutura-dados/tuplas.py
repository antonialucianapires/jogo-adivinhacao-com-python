"""
Tuplas

- Uma tupla ( tuple ) em Python é uma sequência imutável de valores de qualquer tipo
- são úteis para representar registros (mas sem atribuir nomes aos campos)
- utilizar parênteses não é obrigatório, mas é considerado boa prática
- leituras: https://blog.betrybe.com/tecnologia/tuplas-em-python/ ,
            https://www.ime.usp.br/~kellyrb/mac0216_2020/mac0216_aula24.html
"""

# criaçãode uma tupla
cores = ('Azul', 'Verde', 'Amarelo', 'Violeta')

# criação de tupla de forma implícita, sem parenteses
pessoas = 'João', 'Maria'
print('tipo da variável pessoas: ', type(pessoas))

# tipo da variável cores
print('tipo da variável cores: ', type(cores))

# exibição da tupla
print('cores: ', cores)

# primeiro item da tupla
primeiroItem = cores[0]
print('primeiro item: ', primeiroItem)

'''
Se for criar uma tupla com apenas um item, é necessário colocar uma vírgula no final
ou o python vai entender que é uma string. Exemplo:
'''

formaIncorreta = ('Olá')
print('tipo da forma incorreta de criar tupla com um item: ', type(formaIncorreta)) # tipo string

formaCorreta = ('Olá',)
print('tipo correto de criar tupla com um item: ', type(formaCorreta))

# tentativa de alterar um item da tupla
# cores[0] = 'Preto'  lança erro TypeError: 'tuple' object does not support item assignment

# verificar se um item existe na tupla
verdeExisteEmCores = 'Verde' in cores
print('a palavra verde existe na tupla? ', verdeExisteEmCores)

pretoExisteEmCores = 'Preto' in cores
print('a palavra preto existe na tupla? ', pretoExisteEmCores)

# contar os elementos de uma tupla
totalPalavraVerde = cores.count('Verde')
print('total de palavra repetida Verde em cores: ', totalPalavraVerde)

# identificar índice de um elemento na tupla
print('Índice da cor verde: ', cores.index('Verde'))

'''
a consulta pelo index do elemento permite a pesquisa por pedaços da tupla, 
o que contribui para oferecer mais velocidade na busca por elementos em um 
grande volume de dados
'''

print('Busca por pedaços: ', cores.index('Verde', 0, len(cores)))





