from math import pi
import sys #importa o módulo sys, que é um módulo que fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
import errno #importa o módulo errno, que fornece um número de erro simbólico. O módulo errno define várias constantes, como EPERM, EPIPE, etc. que representam códigos de erro que podem ser retornados por várias funções do sistema operacional.


def ajuda():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][25:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2: #se o tamanho da lista de argumentos for menor que 2 (ou seja, se não houver argumentos) 
        ajuda()
        #sys.exit(1) #termina o programa com erro 1
        sys.exit(errno.EPERM) #termina o programa com erro EPERM, que é um código de erro que representa a operação não permitida. Mesmo que o erro seja diferente, o programa termina com erro 1
    elif not sys.argv[1].isnumeric(): #se o argumento 1 não for numérico
        ajuda()
        print('O raio deve ser um valor numérico inteiro.')
        sys.exit(errno.EINVAL) #termina o programa com erro EINVAL, que é um código de erro que representa um argumento inválido
    else:
        raio = sys.argv[1] #argumento 1 na linha de comando
        area = circulo(raio)
        print('Área do círculo: ', area)
