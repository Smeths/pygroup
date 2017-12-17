# Import the class Group from the file groups.py

from groups import Group

# Create an instance of the group (32,x)

G = Group("mult",32)
G.g("show")
Gg = G.g()
Ggo = G.go()
print("(32,x) sorted element orders = ",sorted(Ggo),"\n")

# Creating candidate groups

G1 = Group("add",16)
G2 = Group(["add","add"],[8,2])
G3 = Group(["add","add","add"],[4,2,2])
G4 = Group(["add","add","add","add"],[2,2,2,2])

print("Candidate groups:")

G1go = G1.go()
print("(16,+) sorted element orders = ",sorted(G1go))
G2go = G2.go()
print("(8,+)x(2,+) sorted element orders = ",sorted(G2go))
G3go = G3.go()
print("(4,+)x(2,+)x(2,+) sorted element orders = ",sorted(G3go))
G4go = G4.go()
print("(2,+)x(2,+)x(2,+)x(2,+) sorted element orders = ",sorted(G4go),"\n")

print("Conclusion:")
print("(32,x) is therefore isomorphic to (8,+)x(2,+)")













