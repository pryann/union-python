standard_hungarian_tax_rate_in_percent = 27
print(standard_hungarian_tax_rate_in_percent)

# standard_hungarian_tax_rate_in_percent = standard_hungarian_tax_rate_in_percent + 1
standard_hungarian_tax_rate_in_percent += 1
print(standard_hungarian_tax_rate_in_percent)

# compound operators can be used with any aritmetic operator
standard_hungarian_tax_rate_in_percent **= 3
print(standard_hungarian_tax_rate_in_percent)

a = 1000
b = 1000
print(id(a))
print(id(b))
b = 1001
print(id(b))
