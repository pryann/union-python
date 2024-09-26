rgb_color = (255, 255, 255)
print(type(rgb_color))
print(rgb_color[0])
# IMMUTABLE
# rgb_color[0] = 0

# fmt: off
# number
# nums = (1)
nums = (1,)
print(type(nums))
# fmt: on
# unpacking
user = ("John", "Doe", 33, "teacher", "Budapest")
first_name, last_name, age, *details = user
print(first_name, last_name, age, details)

# slicing
print(user[0:3])

# no comprehension, generator expression works with tuple function
numbers = [1, 2, 3, 4, 5]
squared_numbers = tuple(number**2 for number in numbers)
print(squared_numbers)

# bad practice, use list if you want to mutate it
numbers = (1, 2, 3)
numbers_list = list(numbers)
numbers_list.append(4)
numbers = tuple(numbers_list)


def user_factory(first_name, last_name, age):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    age = int(age)
    # tuple
    return first_name, last_name, age


user = user_factory("john", "doe", "33")
print(user, type(user))
