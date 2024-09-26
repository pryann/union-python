for i in range(10):
    print(i)

for i in range(10, 20, 2):
    print(i)

for i in range(10, -1, -1):
    print(i)


yearly_salary = [10000, 20000, 30000, 40000, 50000]
for salary in yearly_salary:
    print("salary:")
    print(salary)

print("END LOOP")
print(salary)

net_prices = [10000, 20000, 30000, 40000, 50000]
gross_prices = []
hungarian_vat_in_percent = 27

for net_price in net_prices:
    gross_prices.append(net_price * (1 + hungarian_vat_in_percent / 100))

print(gross_prices)

for i in range(len(net_prices)):
    print(f"{i}. {net_prices[i]}")

for index, value in enumerate(net_prices):
    print(f"{index}. {value}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
every_second_number = []
for i in range(1, len(numbers), 2):
    every_second_number.append(numbers[i])

print(every_second_number)
