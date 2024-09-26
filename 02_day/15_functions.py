def greeting(name):
    print(f"Hi {name}!")


# built in functions
print(dir(__builtins__))
greeting("John")
name = "Gergő"
print(greeting(name))

print(type(None))


def summation(a, b):
    return a + b


summa = summation(1, 2)
print(summa)


def even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"


print(even_or_odd(2))
print(even_or_odd(3))


def calculate_gross_price(net_price, vat_rate=0.27):
    return net_price * (1 + vat_rate)


print(calculate_gross_price(1000, 0.05))
print(calculate_gross_price(3000))
print(calculate_gross_price(12000))


def add_item_to_basket(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


# print(add_item_to_basket("apple", ["banana", "orange"]))
print(add_item_to_basket("banana"))
print(add_item_to_basket("apple"))
print(add_item_to_basket("orange"))
