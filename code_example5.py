# Importing require modules
from groups import Group
from pure import setCrossProd

# Creating group and subgroup

print("Create (120,+)")
G = Group("add",120)
G.g("show")
GS = G.sub([15,30,60])

# print the sub group components

GSg = GS.g()
GS.g("show")
print("Inverse of element 15 = ",GS.inv(15))
print("Multiplication of 15 and 30 = ",GS.op(15,30))
print("15 to the power 3 = ",GS.pow(15,3))

GSgo = GS.go()
for g,go in zip(GSg,GSgo):
    print("Element: ",g," has order: ",go)



