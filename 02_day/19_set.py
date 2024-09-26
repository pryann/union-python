# Mutale, not indexable, unordered, unique elements
numbers = {1, 2, 3, 4, 5}
print(numbers, type(numbers))

numbers.add(6)
print(numbers)

numbers.update([7, 8, 9])
print(numbers)

# KeyError if not found
numbers.remove(9)
print(numbers)

# no error if not found
numbers.discard(10)
print(numbers)


def error_handling():
    try:
        numbers.remove(10)
    except Exception as e:
        print("KeyError", e)


error_handling()
print("END  ")

numbers.pop()
print(numbers)

int_numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    1,
    2,
    3,
    4,
    4,
    5,
    6,
    7,
]

int_numbers_uniq = []
for number in int_numbers:
    if number not in int_numbers_uniq:
        int_numbers_uniq.append(number)

int_numbers_uniq = list(set(int_numbers))
