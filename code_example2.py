# Import the class Group from the file groups.py

from groups import Group

# Create an instance of the group (10,+)

print("Creating a group (10,+)")
G = Group("add",10)

# print the group components

G.g("show")
print("Inverse of element 3 = ",G.inv(3))
print("Multiplication of 7 and 6 = ",G.op(7,6))
print("7 to the power 3 = ",G.pow(7,3))

Gg = G.g()
Ggo = G.go()
GgoDict = dict(zip(Gg, Ggo))
for g in GgoDict:
    print("Element: ",g," has order: ",GgoDict[g])

# Create an instance of the group (15,x)

print("\nCreating a group (15,x)")
H = Group("mult",15)

# print the group components

Hh = H.g("show")
print("Inverse of element 2 = ",H.inv(2))
print("Multiplication of 2 and 10 = ",H.op(2,10))
print("2 to the power 10 = ",H.pow(2,10))
print("Group orders:")

Hh = H.g()
Hho = H.go()
HhoDict = dict(zip(Hh, Hho))
for h in HhoDict:
    print("Element: ",h," has order: ",HhoDict[h])








