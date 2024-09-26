yearly_salary = 100000
high_salary_limit = 100000

if yearly_salary >= high_salary_limit:
    print("High salary")
else:
    print("Low salary")


grade = input("Enter your grade: ")
if grade == "1":
    print("Elégtelen")
elif grade == "2":
    print("Elégséges")
elif grade == "3":
    print("Közepes")
elif grade == "4":
    print("Jó")
elif grade == "5":
    print("Jeles")
else:
    print("Ez nem osztályzat")
