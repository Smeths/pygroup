# Import the class Group from the file groups.py

from groups import Group

# Create an instance of the group (5,+)x(9,x)

print("Create a group (5,+)x(9,x)")
G = Group(["add","mult"],[5,9])

# print the group components

Gg = G.g("show")
g3 = G.g(3)
print("Element 3 = ",G.g(3))
print("Inverse of element 3 = ",G.inv(g3))

g7 = G.g(7)
g6 = G.g(6)
print("Element 7 = ",g7)
print("Element 6 = ",g6)
print("Multiplication of element 7 and element 6 = ",G.op(g7,g6))
print("Element 7 to the power of 3 = ",G.pow(g7,3))

print("Group orders:")
Gg = G.g()
Ggo = G.go()
for (g,go) in zip(Gg,Ggo):
    print("Element ",g," has order ",go)
    









