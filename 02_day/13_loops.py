# fmt: off
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# fmt: on
print(matrix)

for row in matrix:
    for item in row:
        print(item)

matrix = []
for divide in range(5):
    row = []
    for j in range(5):
        row.append(j)
    matrix.append(row)
print(matrix)

#  print([list(range(5))] * 5)

for divide in range(5):
    print(divide)

# equivalent to the above
divide = 0
while divide < 5:
    print(divide)
    divide += 1

# while True:
#     grade = input("Enter your grade: ")
#     if grade.isdigit() and 0 < int(grade) < 6:
#         print("Grade is valid")
#         break
#     print("Grade is invalid")

# strandard solution
# number = 5
# divide = 2
# is_prime = True
# while divide <= number // 2:
#     if number % divide == 0:
#         is_prime = False
#         break
#     divide += 1


# print("Prime" if is_prime else "Not prime")

number = 5
divide = 2
while divide <= number // 2:
    if number % divide == 0:
        print(f"{number} is not prime")
        break
    divide += 1
else:
    print(f"{number} is prime")


for i in range(50):
    if i % 15 != 0:
        print(i)
