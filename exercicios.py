import random

# Exercício 1
# Dado um array de números de tamanho n, escreva um
# algoritmo que retorna true se há no array um número
# duplicado e false caso contrário. Analise a solução
# abaixo e diga qual é a ordem de complexidade desse
# algoritmo para o melhor caso, pior caso e caso médio.


def contains_duplicate(numbers):
    numbers.sort()
    previous_number = "not a number"
    for number in numbers:
        if previous_number == number:
            return True
        previous_number = number

    return False


# Resposta: Algoritimo O(n log n)

# 🚀 Exercício 2
# Utilize o módulo random da linguagem Python para gerar um array
# com 100 números. Cada um deve ser a média de n números gerados
# aleatoriamente. Qual é a ordem de complexidade de tempo e de espaço
# deste programa?


def generateNumbers():
    my_range = 100
    number_array = []
    my_total = 0
    x = 0
    while x < my_range:
        random_number = round(random.randrange(1, 1001))
        x += 1
        final_number = random_number / x
        number_array.append(final_number)
        my_total += random_number

    print(number_array)


# Resposta: Complexidade de tempo O(n)
# e de espaço O(1) pois possuímos


generateNumbers()
