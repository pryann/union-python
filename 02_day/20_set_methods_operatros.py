x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

print(x1.union(x2))
print(x1.intersection(x2))
print(x1.difference(x2))
print(x1.symmetric_difference(x2))
print(x1.issubset({"a", "b", "c", "d"}))
print(x1.issuperset({"a", "b"}))
print(x1.isdisjoint(x2))

print("union", x1 | x2)
print("intersection", x1 & x2)
print("difference", x1 - x2)
print("symmetric_difference", x1 ^ x2)
print("issubset", x1 <= {"a", "b", "c", "d"})
print("issuperset", x1 >= {"a", "b"})
