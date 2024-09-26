# index is a string, tuple, etc.., ordered, mutable, no duplicates
user = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 33,
}

print(user, type(user))
print(user["first_name"])

user["first_name"] = "Jane"
print(user)

user["job"] = "teacher"
print(user)

user.pop("job")
print(user)

user.update({"first_name": "John", "job": "teacher", "city": "Budapest"})
print(user)

for item in user.items():
    print(item[0], item[1])

for i, v in user.items():
    print(i, v)

# NOT A LIST!!!
print(type(user.values()))


# unpacking
# keys
first_name, last_name, age, *_ = user
# values
first_name, last_name, age, *_ = user.values()
print(first_name, last_name, age)

# comprehension
cart_net_prices = {"VGA": 100, "CPU": 200, "RAM": 300}
cart_gross_prices = {key: value * 1.27 for key, value in cart_net_prices.items()}
print(cart_gross_prices)
