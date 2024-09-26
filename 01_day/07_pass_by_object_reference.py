# IMMUTABLE OBJECTS
age = 20
age_copy = age

print(id(age))
print(id(age_copy))

age = 21
print(id(age))
print(id(age_copy))

print(age)
print(age_copy)

# MUTABLE OBJECTS
# list
yearly_salary = [10000, 20000, 30000]
yearly_salary_copy = yearly_salary
print(id(yearly_salary))
print(id(yearly_salary_copy))

yearly_salary.append(40000)
print(id(yearly_salary))
print(id(yearly_salary_copy))
print(yearly_salary)
print(yearly_salary_copy)

yearly_salary = [10000, 20000, 30000]
print(id(yearly_salary))
print(id(yearly_salary_copy))
print(yearly_salary)
print(yearly_salary_copy)


ys = [10000, 20000, 30000]
ysc = ys.copy()
print(id(ys))
print(id(ysc))
