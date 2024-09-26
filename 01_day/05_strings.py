first_name = "Ahmed"
last_name = "Ali"

# Concatenation, old school way
full_name = first_name + " " + last_name
print(full_name)

first_name = "O'Connor"
# cite = ""cite""
cite = '"cite"'

# better way, but not the best
full_name = "Fullname: {0} {1}. {2}. My name is {0}".format(first_name, last_name, cite)
print(full_name)

# modern way
age = 40
me = f"Fullname: {first_name} {last_name}. Age: {age-10}"
print(me)

print("Hi" * 5)

print("First line\nSecond line\nThird line")
# print("First line\\nSecond line\\nThird line")
print(r"First line\n\tSecond line\nThird line")

# TODO: Add more examples

# documenation string
"""This is a long string
It can span multiple lines"""

print("string".count("s"))
