#Tipos básicos
print(False) #False
print(True) #True
print(1.2 + 1) #2.2
print('Aqui eu falo minha lingua!') #Aqui eu falo minha lingua!
print("Também funciona") #Também funciona
print('Você é ' + 3 * 'muito ' + 'legal!') #Você é muito muito muito legal!
#print(3 + '3') -> ambiguidade entre soma e concatenação, TypeError: unsupported operand type(s) for +: 'int' and 'str'
print([1, 2, 3]) #[1, 2, 3] -> lista
print({'nome': 'Diego', 'idade': 31}) #{'nome': 'Diego', 'idade': 31} -> dicionario
print(None) #None


#Variáveis
"""'a' é o identificador, '=' é o simbolo de atribuicao e '10' é o valor.
Podemos ler como: O identificador da variável 'a'(nome) recebe (=) o valor"""
a = 10  
b = 5.2

print(a + b) #15.2

a = 'Agora sou uma string!' #a variavel 'a' recebe um novo valor, agora uma string
print(a) #Agora sou uma string!
print(b) #5.2

#Comentários
#linha a linha
#Minhas variaveis
salario = 3450.45 
despesas = 2456.2

#comentar varias linhas com """ """ ou ''' '''
"""
A ideia é calcular 
quando vai sobrar no 
final do mes!
"""

'''
A ideia é calcular 
quando vai sobrar no 
final do mes!
'''

print(salario - despesas) #994.25

#print('Fim')  

print('Fim de verdade') #Comentário aqui também vale!

print('Agora sim o fim de verdade')


#Operadores Aritmeticos
print(2 + 3) #5
print(4 - 7) #-3
print(2 * 5.3) #10.6
print(9.4 / 3) #3.1333333333333333
print(9.4 // 3) #3.0
print(2 ** 8) #256
print(10 % 3) #1

a = 12 
b = a
print(a + b) #24


#Desafio 1
# Minhas variáveis
salario = 3450.45
despesas = 2456.2

# Resposta do desafio
percentual_comprometido = despesas / salario * 100 
percentual_comprometido #71.24765708418891


#Operadores Relacionais
3 > 4 #False
4 >= 3 #True
1 < 2 #True
3 <= 1 #False
3 != 2 #True
3 == 3 #True
2 == '2' #False

#Operadores de Atribuição
a = 3 #a recebe 3
a = a + 7 #a recebe a + 7
print(a) #10

#Operadores unarios
#atribuicao aditiva
# a = 5 substituindo o valor que era 10 por 5, numa nova atribuição
a += 5 # a = a + 5 (acrescentando o valor 5 na variavel 10, que passará a ser 15)
print(a) #15

#atribuicao subtrativa
a -= 3 #(subtraindo o valor 3 na variavel 15, que passará a ser 12)
print(a) #12

#atribuicao multiplicativa
a *= 2
print(a) #24

#divisiva
a /= 4
print(a) #6.0

#modular (resto da divisao)
a %= 4
print(a) #2.0

#exponencial
a **= 8
print(a) #256.0

#divisiva, retornando apenas o inteiro
a //= 256
print(a) #1.0


#Operadores Lógicos
True or False #True
# V ou F = V

7 != 3 and 2 > 3 #False
#V e F = F

# Tabela verdade do AND
True and True # True
True and False # False
False and True # False
False and False # False
True and True and False and True and True and True #False

# Tabela verdade do OR
True or True #True
True or False #True
False or True #True
False or False #False
False or False or True or False or False or False #True

# Tabela verdade do XOR (ou exclusivo) 
True != True #False
True != False #True
False != True #True
False != False #False

# Operador de Negação (unário)
not True #False
not False #True

not 0 #True
not 1 #False - qualquer numero diferente de zero é verdadeiro, logo, not True é False
not not -1 #True
not not True #True

# Cuidado! Operadores bit-a-bit
True & False 
False | True
True ^ False

# AND Bit-a-bit
# 3 = 11 em binario
# 2 = 10 em binario
# _ = 10, logo 2 em binario
3 & 2 #resultado é 2

# OR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 11
3 | 2 #resultado é 3

# XOR Bit-a-bit
# 3 = 11
# 2 = 10
# _ = 01
3 ^ 2 #resultado é 1

# Um pouco de realidade
saldo = 1000
salario = 4000
despesas = 3900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario 

meta = saldo_positivo and despesas_controladas 
meta #True


# Desafio Operadores Lógicos

# Os Trabalhos
trabalho_terca = True
trabalho_quinta = False

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa
"""
tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta #xor
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudável={}"
     .format(tv_50, tv_32, sorvete, mais_saudavel))

# "{}, {} = {}".format(1, False, 'resultado')

#Operadores ternarios
esta_chovendo = False

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))

#Mais operadores
# Operador de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
2 in lista
'Ana' not in lista

# Operador de Identidade
x = 3
y = x
z = 3
x is y
y is z
x is not z

lista_a = [1, 2, 3] 
lista_b = lista_a 
lista_c = [1, 2, 3]

lista_a is lista_b
lista_b is lista_c
lista_a is not lista_c

#Builtins
# type()
type(1)
__builtins__.type('Fala Galera!')
__builtins__.print(10 / 3)

# __builtins__.help(__builtins__.dir)

# a = 7
# import math
# dir()
# dir(__builtins__)


nome = 'João da Silva'
type(nome) #str
__builtin__.len(nome) #13

dir() #variaveis disponiveis

#Conversão de Tipos
2 + 3 #5
'2' + '3' #'23'
# 2 + '3' #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(2 + '3') #TypeError: unsupported operand type(s) for +: 'int' and 'str'

a = 2
b = '3'

print(type(a)) #int
print(type(b)) #str

print(a + int(b)) #5
print(str(a) + b) #23

type(str(a)) #str

# print(2 + int('3.4'))

#Coerção Automática
10 / 2 #5.0
type(10 / 2) #float
10 / 3 #3.3333333333333335
10 // 3 #3
type(10 // 3) #int
10 // 3.3 #3.0
type(10 // 3.3) #float
10 / 2.5 #4.0
2 + True #3
2 + False #2
type(1 + 2) #int
type(1 + 2.5) #float

#Numeros_01

dir(int) #metodos disponiveis para o tipo int
dir(float) #metodos disponiveis para o tipo float

a = 5
b = 2.5
a / b #2.0
a + b #7.5
a * b #12.5

type(a) #int
type(b) #float
type(a - b) #float

b.is_integer() #False
5.0.is_integer() #True
int.__add__(2, 3) #5
2 + 3 #5

(-2).__abs__() #2
abs(-2) #2

(-3.6).__abs__() #3.6
abs(-3.6) #3.6

#Numeros_02

1.1 + 2.2 #3.3000000000000003

from decimal import Decimal, getcontext
Decimal(1) / Decimal(7) #Decimal('0.1428571428571428571428571429')

getcontext().prec = 4 #precisao de 4 casas decimais
Decimal(1) / Decimal(7) #Decimal('0.1429')
Decimal.max(Decimal(1), Decimal(7)) #Decimal('7')
dir(Decimal) #metodos disponiveis para o tipo Decimal

1.1 + 2.2 #3.3000000000000003
getcontext().prec = 10 #precisao de 10 casas decimais
Decimal(1.1) + Decimal(2.2) #Decimal('3.3000000000')

import decimal #importando o modulo decimal
dir(decimal) #metodos disponiveis para o modulo decimal
dir() #variaveis disponiveis

#String_01

dir(str) #metodos disponiveis para o tipo string
nome = 'Saulo Pedro'
nome #Saulo Pedro
nome[0] #S

# nome[0] = 'P'  >> imutável, TypeError: 'str' object does not support item assignment

'marca d\'água' #marca d'água
"Dias D'Avila" == 'Dias D\'Avila' #True
texto = 'Texto entre apostrófos pode ter "aspas"' #Texto entre apostrófos pode ter "aspas"
texto = "Texto entre apostrófos pode ter 'aspas'" #Texto entre apostrófos pode ter 'aspas'

doc = """Texto com múltiplas
... linhas""" #atribuindo um texto com múltiplas linhas a variavel
doc #Texto com múltiplas\n... linhas
print('Texto com múltiplas\n... linhas') #Texto com múltiplas\n... linhas
print(doc) #Texto com múltiplas\n... linhas

doc = '''Também é possível
... com 3 aspas simples''' #atribuindo um texto com múltiplas linhas a variavel
doc #Também é possível\n... com 3 aspas simples

#String_02

nome = 'Ana Paula'
nome[0] #A
nome[6] #u
nome[-3] #u
nome[4:] #inclui a posição 4 e vai até o final -> Paula
nome[-5:] #Paula, pega os 5 ultimos caracteres
nome[:3] #da posição 0 até a 3, excluindo a 3 -> Ana
nome[2:5] #da posição 2 até a 5, incluindo a posicao 2 excluindo a 5 -> a P

numeros = '1234567890'
numeros
numeros[::] #todos os elementos
numeros[::2] #pulando de 2 em 2 a partir da posição 0
numeros[1::2] #pulando de 2 em 2 a partir da posição 1
numeros[::-1] #inverte a string
numero

nome[::-1] #inverte a string, Ana Paula -> alauP anA

#String_03

frase = 'Python é uma linguagem excelente' #False, pois é case sensitive
'py' in frase #True
'ing' in frase #True
'py' not in frase #False
len(frase) #tamanho da string, 32 caracteres
frase.lower() #tudo minusculo, python é uma linguagem excelente
'py' in frase.lower() #True
frase
frase = frase.upper() #tudo maiusculo
frase

frase = frase.upper()
frase.split() #quebra a string em uma lista de strings, separando pelo espaço
frase.split('E') #quebra a string em uma lista de strings, separando pelo E
frase.split('E', 1) #quebra a string em uma lista de strings, separando pelo E, mas apenas 1 vez

dir(str)
help(str.center)

#String_04, metodos magicos

a = '123'
b = ' de Oliveira 4'
a + b #concatenação, '123 de Oliveira 4'
a.__add__(b) #concatenação, '123 de Oliveira 4'
str.__add__(a, b) #concatenação, '123 de Oliveira 4'
len(a) #3
a.__len__() #3
'1' in a #True
a.__contains__('1') #True

dir(str) #metodos disponiveis para a string

#Lista_01

lista = [] #lista vazia, usar par de colchetes
type(lista) #list
dir(lista) #metodos disponiveis para a lista
help(list) #ajuda para a lista, multavel, ordenada, heterogenea e indexada
len(lista) #0
lista.append(1) #adiciona um elemento na lista
lista.append(5) #adiciona um elemento na lista
lista #lista com 1 e 5 -> [1, 5]
len(lista) #2
nova_lista = [1, 5, 'Ana', 'Bia']
nova_lista # -> [1, 5, 'Ana', 'Bia']
nova_lista.remove(5) #remove o item 5 da lista e nao o indice 5
nova_lista # -> [1, 'Ana', 'Bia']
nova_lista.reverse() #inverte a ordem da lista -> ['Bia', 'Ana', 1]
nova_lista # -> ['Bia', 'Ana', 1], nesse caso, no caso o reverse é um metodo que altera a nova_lista, pela lista ser mutavel

#Lista_02

lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
lista.index('Guilherme') #indice 3
lista[2] #Rebeca
1 in lista #True
'Rebeca' in lista #True
'Pedro' not in lista #True
lista[0] = 2 #substitui o valor 1 por 2, é mutavel
lista[0] #2
lista[4] #3.1415
lista[-1] #3.1415
lista[-5] #2
lista[-2] #Guilherme
lista[-3] #Rebeca
lista[-4] #5

#Lista_03
lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
lista[1:3] #pega os elementos da posição 1 até a 3, excluindo a 3 -> ['Lia', 'Rui'] 
lista[1:-1] #pega os elementos da posição 1 até o penultimo, ou seja, não considera o ultimo elemento, indice -1 -> ['Lia', 'Rui', 'Paulo']
lista[1:] #pega os elementos da posição 1 até o final -> ['Lia', 'Rui', 'Paulo', 'Dani']
lista[:-1] #pega os elementos da posição 0 até o penultimo, ou seja, não considera o ultimo elemento, indice -1 -> ['Ana', 'Lia', 'Rui', 'Paulo']
lista[:] #pega todos os elementos da lista
lista[::2] #pega todos os elementos da lista, pulando de 2 em 2 -> ['Ana', 'Rui', 'Dani']
lista[::-1] #inverte a lista -> ['Dani', 'Paulo', 'Rui', 'Lia', 'Ana']
del lista[2] #deleta o elemento da posição 2 -> ['Ana', 'Lia', 'Paulo', 'Dani']
del lista[1:] #deleta os elementos da posição 1 até o final -> ['Ana']

#Tupla_01
tupla = tuple() #tupla vazia, usar par de parenteses 
tupla = () #tupla vazia, usar par de parenteses
type(tupla) #tuple
dir(tupla) #metodos disponiveis para a tupla
help(tuple) #ajuda para a tupla, imutavel, ordenada, heterogenea e indexada

tupla = ('um') #não é uma tupla
tupla = ('um',) #é uma tupla, com um elemento
tupla = ('um', 'dois', 'três') #é uma tupla, com 3 elementos
type(tupla) #tuple
tupla[0] #um
tupla[0] = 'novo' #TypeError: 'tuple' object does not support item assignment, é imutavel

cores = ('verde', 'amarelo', 'azul', 'branco')
cores[0] #verde
cores[-1] #branco
cores[1:] #('amarelo', 'azul', 'branco') -> pega os elementos da posição 1 até o final
cores.index('amarelo') #1
cores.count('azul') #1, conta quantas vezes o elemento aparece na tupla
cores.append('roxo') #AttributeError: 'tuple' object has no attribute 'append', não é mutavel

len(cores) #4

#Dicionario_01, chave e valor
dicio = {} #dicionario vazio, usar chaves
pessoa = {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
type(pessoa) #dict
dir(dict) #metodos disponiveis para o dicionario
help(dict) #ajuda para o dicionario, mutavel, desordenado, heterogeneo e indexado
len(pessoa) #3, quantidade de elementos no dicionario

pessoa # {'nome': 'Prof(a). Ana', 'idade': 38, 'cursos': ['Inglês', 'Português']}
pessoa['nome'] #Prof(a). Ana
pessoa['idade'] #38
pessoa['cursos'] #['Inglês', 'Português']
pessoa['cursos'][1] #Português
pessoa.keys() #dict_keys(['nome', 'idade', 'cursos'])
pessoa.values() #dict_values(['Prof(a). Ana', 38, ['Inglês', 'Português']])
pessoa.items() #dict_items([('nome', 'Prof(a). Ana'), ('idade', 38), ('cursos', ['Inglês', 'Português'])]), retorna chave e valor
pessoa.get('idade') #38
pessoa.get('tags') #None
pessoa.get('tags', []) #[], retorna uma lista vazia

#Dicionario_02
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
pessoa['idade'] = 44 #altera o valor da chave idade
pessoa['cursos'].append('Angular') #adiciona um elemento a lista de cursos
pessoa # {'nome': 'Prof. Alberto', 'idade': 44, 'cursos': ['React', 'Python', 'Angular']}
pessoa.pop('idade') #44, remove a chave idade do dicionario e retorna o valor da chave retirada
pessoa # {'nome': 'Prof. Alberto', 'cursos': ['React', 'Python', 'Angular']}
pessoa.update({'idade': 40, 'sexo': 'M'}) #adiciona as chaves idade e sexo ao dicionario
pessoa # {'nome': 'Prof. Alberto', 'cursos': ['React', 'Python', 'Angular'], 'idade': 40, 'sexo': 'M'}
del pessoa['cursos'] #remove a chave cursos do dicionario e seu(s) respectivo(s) valor(es)
pessoa # {'nome': 'Prof. Alberto', 'idade': 40, 'sexo': 'M'}
pessoa.clear() #limpa o dicionario
pessoa # {}, dicionario vazio

#Conjunto_01 - set, não aceita repetição, não é indexado, não é ordenado
a = {1, 2, 3} #conjunto, par de chaves
type(a) #set
a[0] #TypeError: 'set' object is not subscriptable, não é indexado
a = set('coddddd3r') #conjunto, não aceita repetição
print(a) #{'c', 'r', '3', 'd', 'o'} -> não é ordenado e nao garante a ordem
print('3' in a) #True
print('4' not in a) #True
{1, 2, 3} == {3, 2, 1, 3} #True, não é ordenado e não aceita repetição

c1 = {1, 2}
c2 = {2, 3}
c1.union(c2) # {1, 2, 3}, une os conjuntos
c1.intersection(c2) # {2}, interseção entre os conjuntos
c1.update(c2) # {1, 2, 3}, atualiza o conjunto c1 com a união de c1 e c2
c1 # {1, 2, 3}
c2 <= c1 #True, c2 é subconjunto de c1, c2 está contido em c1
c1 >= c2 #True, c1 é superconjunto de c2, c1 contém c2

{1, 2, 3} - {2} # {1, 3}, diferença entre os conjuntos
c1 - c2 # {1}, diferença entre os conjuntos
c1 -= {2} # {1}, remove o elemento 2 do conjunto c1
c1 # {1}

#interpolacao
 nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome, idade)) #Nome: Ana Idade: 30 -> interpolacao com %
print('Nome: {0} Idade: {1}'.format(nome, idade)) #Nome: Ana Idade: 30 -> interpolacao com format
print(f'Nome: {nome} Idade: {idade}') #Nome: Ana Idade: 30 -> interpolacao f-string

from string import Template #importando a classe Template do modulo string
s = Template('Nome: $n Idade: $i') #criando um template
print(s.substitute(n=nome, i=idade)) #Nome: Ana Idade: 30 -> interpolacao com Template
