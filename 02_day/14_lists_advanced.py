# slicing: str, list, tuple

yearly_salaries = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
print(yearly_salaries[0])
print("from the start to the 3. element", yearly_salaries[0:3])
print("from the start element to the 6. elemen, step:2", yearly_salaries[0:6:2])
print("from the 2. element to the end", yearly_salaries[2:])
print("from the start to the 2. element", yearly_salaries[:2])
print("every second element from the start", yearly_salaries[::2])
print("every second element from the end", yearly_salaries[::-2])
print("last element", yearly_salaries[-1])
yearly_salaries_copy = yearly_salaries[:]

updated_salary_values = [1111, 2222]
# yearly_salaries[2:6:2] = updated_salary_values
# print(yearly_salaries)
yearly_salaries[:: len(yearly_salaries) - 1] = updated_salary_values
print(yearly_salaries)

# comprehension
net_prices = [100, 200, 300, 400, 500]
gross_prices = []
hunragian_vat_rate = 0.27

for net_price in net_prices:
    gross_prices.append(net_price * (1 + hunragian_vat_rate))

gross_prices = [net_price * (1 + hunragian_vat_rate) for net_price in net_prices]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

marix = [[j for j in range(5)] for i in range(5)]
print(marix)
flatten_matrix = []
for row in marix:
    for item in row:
        flatten_matrix.append(item)

flatten_matrix = [item for row in marix for item in row]

# swap
a = 10
b = 20

# meeeh....
# tmp = a
# a = b
# b = tmp

a, b = b, a

# unpacking
first_name, last_name, age = "John", "Doe", 33
print(first_name, last_name, age)

abc = "abcdefg"
a, b, c, *others = abc
print(a, b, c, others)

user = ["John", "Doe", 33, "teacher", "Budapest"]

first_name, last_name, age, *_ = user
print(first_name, last_name, age, _)
