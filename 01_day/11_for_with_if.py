yearly_salaries = [10000, 20000, 30000, 40000, 50000]
high_salary_limit = 32000
sum_low_salaries = 0
sum_high_salaries = 0

for salary in yearly_salaries:
    if salary >= high_salary_limit:
        sum_high_salaries += salary
    else:
        sum_low_salaries += salary

print("Sum of low salaries:", sum_low_salaries)
print("Sum of high salaries:", sum_high_salaries)
