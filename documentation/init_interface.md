# Interfaces to __init__

## __init__(gType="add",mod=int, gSub)

creates an add group of modulus int
self.subgroup = False if gSub is empty
self.subgroup = True if gSub is not empty
self.i = 0
self.mod = mod
self.glist = range(0,mod) if gSub is empty
self.glist = gSub if gSub is not empty
self.o = order of the group
self.gType = gType
self.gdict = indexed dictionary of the group
self.sets = not defined

## __init__(gType="mult",mod=int, gSub)

creates a mult group of modulus int
self.subgroup = False if gSub is empty
self.subgroup = True if gSub is not empty
self.i = 1
self.mod = mod
self.glist = multiplication with modulus = mod if gSub is empty
self.glist = gSub if gSub is not empty
self.o = order of the group
self.gType = gType
self.gdict = indexed dictionary of the group
self.sets = not defined

## __init__(gType=list,mod=list, gSub)

creates a cross group of with types defined by gType and mods defined by mod
self.subgroup = False if gSub is empty
self.subgroup = True if gSub is not empty
self.i = list of 0s and 1s depending on elements in list gType
self.mod = mod
self.glist = cross group defined by gType and mod if gSub is empty
self.glist = gSub if gSub is not empty
self.o = order of the group
self.gType = list of types used to define the group
self.gdict = indexed dictionary of the group
self.sets = set of sets used to create the group






















