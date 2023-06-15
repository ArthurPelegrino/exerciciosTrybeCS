# 1 - OK
# 0 - Instabilidades
import random

valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
# resultado = 3

valores_coletados1 = [0, 1, 0, 1, 0, 1, 0]
# resultado = 4


def check_stability(binary_list):  # [1, 1, 1, 1, 0, 0, 1, 1]
    working_time = 0
    maximum_working_time = 0
    for w in range(0, len(binary_list) - 1):
        if binary_list[w] == 1:
            if binary_list[w] == binary_list[w + 1]:
                if working_time == 0:
                    working_time += 2
                else:
                    working_time += 1
                if maximum_working_time < working_time:
                    maximum_working_time == working_time
        if binary_list[w] == 0:
            if binary_list[w] == binary_list[w + 1]:
                maximum_working_time = working_time
                working_time = 0
            else:
                working_time += 1
    return maximum_working_time


# print(check_stability(valores_coletados1))


def sort_cards_randonly(cards):
    mid = len(cards) // 2
    first_half = cards[:mid]
    second_half = cards[mid:]
    random.shuffle(first_half)
    random.shuffle(second_half)
    first_half.extend(second_half)
    return first_half


# sort_cards_randonly([1, 4, 4, 7, 6, 6])


def find_combinations(numbers):  # [ 5, 2, 8 ,4 ,6 ]
    number_of_combinations = 0  # [ 5, 2, 8 ,4 ,6 ]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                number_of_combinations += 1
    return number_of_combinations


print(find_combinations([5, 2, 8, 4, 5, 6]))
