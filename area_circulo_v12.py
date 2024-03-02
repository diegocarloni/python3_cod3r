from math import pi
import sys #importa o módulo sys, que é um módulo que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2: #se o tamanho da lista de argumentos for menor que 2 (ou seja, se não houver argumentos) 
        print('É necessário informar o raio do círculo.')
        print('Sintaxe: {} <raio>'.format(sys.argv[0][25:]))
    else:
        raio = sys.argv[1] #argumento 1 na linha de comando
        area = circulo(raio)
        print('Área do círculo: ', area)
