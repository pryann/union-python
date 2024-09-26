# can contains any type of data
# can contains duplicate data
# mutable
# indexed
# yearly_salaries = [10000, 20000, 30000, 40000, 50000, 50000, True, None, [1, 2, 3]]
yearly_salaries = [10000, 20000, 30000, 40000, 50000]
print(yearly_salaries)

name = "Gergely"
print(name[0])
# TypeError
# name[0] = "g"

print(yearly_salaries[0])
print(yearly_salaries[1])
yearly_salaries[0] = 15000
print(yearly_salaries)

# operators
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)
print(1 in [1, 2, 3])

# delete
del yearly_salaries[0]
print(yearly_salaries)
# remove
yearly_salaries.remove(20000)
print(yearly_salaries)
print("pop return value", yearly_salaries.pop())
print(yearly_salaries)
# add
yearly_salaries.append(60000)
print(yearly_salaries)
# same as + operator
yearly_salaries.extend([70000, 80000])
print(yearly_salaries)
yearly_salaries.insert(0, 90000)
print(yearly_salaries)
yearly_salaries.sort(reverse=True)
print(yearly_salaries)

names = ["Gergely", "Ahmed", "Ali", "Mohamed"]
print("|".join(names))

yearly_salaries = [10000, 20000, 30000, 40000, 50000]
# extend with: [60000, 70000, 80000]
# insert 90000 at the beginning
# remove the second element
# sort by descending order

yearly_salaries.extend([60000, 70000, 80000])
yearly_salaries.insert(0, 90000)
yearly_salaries.pop(1)
yearly_salaries.sort(reverse=True)

