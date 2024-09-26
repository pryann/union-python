# maximum kiválasztás
# A maximum kiválasztás algoritmusa egy olyan algoritmus, amely egy adott listából kiválasztja a legnagyobb elemet.
# Legalább egy elemet tartalmazó listát vár bemenetként, és a legnagyobb elemet adja vissza.
def get_max_value(numbers):
    # max_value = float("-inf")
    # for number in numbers:
    #     if number > max_value:
    #         max_value = number
    # return max_value
    max_value = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] > max_value:
            max_value = numbers[index]
    return max_value


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(get_max_value(numbers))
print(max(numbers))


def get_min_value(numbers):
    min_value = numbers[0]
    for index in range(1, len(numbers)):
        if numbers[index] < min_value:
            min_value = numbers[index]
    return min_value


print(get_min_value(numbers))
print(min(numbers))


def get_sum_value(numbers):
    summa = 0
    for number in numbers:
        summa += number
    return summa


def get_avg_values(numbers):
    return get_sum_value(numbers) / len(numbers)


def count_values(numbers, value):
    counter = 0
    for number in numbers:
        if number == value:
            counter += 1
    return counter


print(count_values(numbers, 5))
print(numbers.count(5))


def get_index(numbers, value):
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i


# None if not found
print(get_index(numbers, 5))
# ValueError if not found
print(numbers.index(5))


# Eldöntés
def is_contains(numbers, value):
    for number in numbers:
        if number == value:
            return True
    return False


print(is_contains(numbers, 5))
print(5 in numbers)


def linear_search(numbers, value):
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return -1


values = [-2, 45, 0, 11, -9]


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            print(i, j)
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


bubble_sort(values)
print(values)

values_2 = [1, 2, 3, 4, 6, 5]
bubble_sort(values_2)


def advanced_bubble_sort(numbers):
    numbers_copy = numbers[:]
    for i in range(len(numbers_copy)):
        swapped = False
        for j in range(len(numbers_copy) - i - 1):
            if numbers_copy[j] > numbers_copy[j + 1]:
                numbers_copy[j], numbers_copy[j + 1] = (
                    numbers_copy[j + 1],
                    numbers_copy[j],
                )
                swapped = True
        if not swapped:
            return numbers_copy


values_3 = [1, 2, 3, 4, 5, 6, 7]
print("ADVANCED")
print(advanced_bubble_sort(values_3))
