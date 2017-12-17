# Importing require modules
from groups import Group
from pure import setCrossProd

# Creating group and subgroup

print("Create (64,x)")
G = Group("mult",64)
G.g("show")
GS = G.sub([7,17])
GS.g("show")

# print the sub group components
print("Inverse of element 25 = ",GS.inv(25))
print("Multiplication of 7 and 25 = ",GS.op(7,25))
print("18 to the power 3 = ",GS.pow(15,3))

GSg = GS.g()
GSgo = GS.go()
for g,go in zip(GSg,GSgo):
    print("Element: ",g," has order: ",go)



