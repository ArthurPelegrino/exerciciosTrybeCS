# 🚀 Exercício 1:
# Crie um algoritmo não recursivo para contar quantos números
# pares existem em uma sequência numérica (1 a n).


def non_recursive_counter(n):
    x = 1
    divisible_by_zero = 0
    while x <= n:
        if x % 2 == 0:
            x += 1
            divisible_by_zero += 1
        else:
            x += 1
    print(divisible_by_zero)
    return divisible_by_zero


# non_recursive_counter(10)

# 🚀 Exercício 2:
# Transforme o algoritmo criado acima em recursivo.


def recursive_counter(n):
    if n < 2:
        return 0
    elif n % 2 == 0:
        return 1 + recursive_counter(n - 1)
    else:
        return recursive_counter(n - 1)


# print(recursive_counter(10))

# 🚀 Exercício 3:
# Crie um algoritmo recursivo que encontre, em uma lista,
# o maior número inteiro.


def recursive_find_bigger_number(recieved_list):
    if len(recieved_list) == 1:
        return recieved_list[0]
    else:
        if recieved_list[0] <= recieved_list[1]:
            recieved_list.pop(0)
        else:
            recieved_list.pop(1)
    return recursive_find_bigger_number(recieved_list)


# print(recursive_find_bigger_number([1, 3, 4, 5, 7, 9, 123123]))
