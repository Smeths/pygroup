# Importing require modules
from groups import Group

# Creating group and subgroup

print("Create (6,+)x(9,x) group")
G = Group(["add","mult"],[6,9])
G.g("show")

print("Print order of [0,1] is: ", G.go([0,1]))

print("Create sub group with elements 2 and 22")
g2 = G.g(2)
g22 = G.g(22)
GS = G.sub([g2,g22])
GSg = GS.g("show")

g2 = GS.g(2)
print("Element 2 = ",g2)
print("Inverse of element 2 = ",GS.inv(g2))
g4 = GS.g(4)
g5 = GS.g(5)
print("Element 4 = ",g4)
print("Element 5 = ",g5)
print("Multiplication of element 4 and element 5 = ",GS.op(g4,g5))
print("Element 4 to the power of 3 = ",GS.pow(g4,3))

print("Group orders:")
GSg = GS.g()
GSgo = GS.go()
print(GSgo)
for (g,go) in zip(GSg,GSgo):
    print("Element ",g," has order ",go)















