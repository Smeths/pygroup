#An example of a class
from pure import *

class Group(object):

    def __init__(self, gtype   = None,
                       mod     = None,
                       sub     = [] ):

##########################################
#        Group Generation Methods        #
##########################################

# mult mod generator

        def multmodgen(m):
            mg = []
            for i in range(1,m):
                if gcd(i,m) == 1:
                    mg.append(i)
            return mg           

        if type(gtype) == str:
            if gtype == "add": 

##########################################
#        Single add mod group            #
##########################################

                self.i = 0
                self.mod = mod
                if sub == []:
                    self.glist = range(0,self.mod)
                else:
                    self.glist = sub

            if gtype == "mult":

##########################################
#        Single mult mod group           #
##########################################

                self.i = 1
                self.mod = mod
                if sub == []:
                    self.glist = multmodgen(mod)
                else:
                    self.glist = sub

##########################################
#        Cross product groups            #
##########################################

        elif type(gtype) == list:
            ident = []
            sets = []
            index = 0
# setting up sets for the cross product
            for gt in gtype:
                modi = mod[index]
                index = index + 1
                if gt == "add":
                    s = range(0,modi)
                    ident.append(0)
                elif gt == "mult":
                    s = multmodgen(modi)
                    ident.append(1)
                sets.append(s)
            self.i = ident
            self.sets = sets
            self.mod = mod
            if sub == []:
                gx = setCrossProd(self.sets)
                gs = []
                for x in gx:
                    if x not in gs:
                        gs.append(x)
                self.glist = gs
            else:
                self.glist = sub

# Group order and type

        self.o = len(self.glist)
        self.gtype = gtype

# Group dictionary

        count = 0
        self.gdict = {}
        for g in self.glist:
            self.gdict[count] = g
            count = count + 1
            
##########################################
#        Group Operator Methods          #
##########################################

    def op2(self,ga,gb,owType = None):
        if owType == None:
            useType = self.gtype
        else:
            useType = owType
# Addition modulus
        if useType == "add":
            ans = (ga + gb) % self.mod
# Multiplication modulus
        elif useType == "mult":
            ans = (ga*gb) % self.mod
# Addition vector modulus
        else:
            ans = []
            for i in range(0,len(ga)):
                if self.gtype[i] == "add":
                    ans.append((ga[i] + gb[i]) % self.mod[i])
                elif self.gtype[i] == "mult":
                    ans.append((ga[i]*gb[i]) % self.mod[i])
        return ans

    def op(self,ga,gb = None):
# if two elements are to be multiplied
        if gb is not None:
            return self.op2(ga,gb)
        else:
# if a list of elements are to be multiplied
            mult = ga[0]
            for i in range(1,len(ga)):
                mult = self.op2(mult,ga[i])
            return mult

##########################################
#        Group Element Order             #
##########################################

    def gorder(self,g,g_return = False):
# calculates the order of elem
        g_init = g
        if g_return:
            gs = [g]
        for i in range(0,self.o):
            if g == self.i:
                if g_return:
                    return gs
                else:
                    return i + 1
            else:
                g = self.op2(g,g_init)
                if g_return:
                    gs.append(g)

    def go(self,g=None):
# recording initial element and index
        if g == None:
            gos = []
            loop = self.glist
            for g in loop:
                gos.append(self.gorder(g))
            return gos
        elif type(g) == int:
            return self.gorder(g)
        elif type(g) == list and type(self.gtype) == str:
            gos = []
            loop = g
            for g in loop:
                gos.append(self.gorder(g))
            return gos
        elif type(g) == list and type(self.gtype) == list:
            if type(g[0]) == list:
                gos = []
                loop = g
                for g in loop:
                    gos.append(self.gorder(g))
                return gos
            elif type(g[0]) == int:
                return self.gorder(g)
                
##########################################
#      Cycling over an element           #
##########################################

    def gcycle(self,g=None):
# creates second interface to gorder with default of true for return elements
        return self.gorder(g,g_return = True)

##########################################
#        Group Element Power             #
##########################################

    def pow(self,g,power,owType = None):
# Calculating the power
        g_init = g
        for i in range(0,power-1):
            if owType == None:
                element = self.op2(g,g_init)
            else:
                element = self.op2(g,g_init,owType)
        return element

##########################################
#        Group Inverse Methods           #
##########################################

    def inv(self,g):
        if self.gtype == "add":
            ginv = (self.mod - g) % self.mod
        if self.gtype == "mult":
            power = self.mod
            ginv = self.pow(g,power)
        if type(self.gtype) == list:
            ginv = []
# setting up sets for the cross product
            for ind,gtype in enumerate(self.gtype):
                if gtype == "add":
                    ginv.append((self.mod[ind] - g[ind]) % self.mod[ind])
                elif gtype == "mult":
                    power = len(self.sets[ind]) - 1
                    storemod = self.mod
                    self.mod = self.mod[ind]
                    ginvc = self.pow(g[ind],power,"mult")
                    self.mod = storemod
                    ginv.append(ginvc)
        return ginv    

##########################################
#        Group Elements                  #
##########################################

    def g(self,ind=None):
        if ind==None:
            return self.glist 
        elif type(ind) is list:
            gs = set()
            for ind in index:
                gs.append(self.gdict[ind])
            return gs
        elif type(ind) is int:
            return self.gdict[ind]
        elif type(ind) == str:
            print("Group Type: ",self.gtype)
            print("Group Def: ",self.mod)
            for i in self.gdict:
                print("Element ",i," has value ", self.gdict[i])
            print("Group identity: ",self.i)
            print("Group order: ",self.o)

            print("")
        
##########################################
#        Sub Group                       #
##########################################

    def unique_list(self,glist):
        gs = []
        for x in glist:
            g = self.op(x)
            if g not in gs:
                gs.append(g)
        return gs 

    def sub(self,g):
        if type(g) == int:
            gs = self.gcycle(g)
        elif type(g) == list and type(self.gtype) == str:
            sets = []
            loop = g
            for g in loop:
                sets.append(self.gcycle(g))
            gx = setCrossProd(sets)
            gs = self.unique_list(gx)
        elif type(g) == list and type(self.gtype) == list:
            if type(g[0]) == int:
                gs = self.gcycle(g)
            elif type(g[0]) == list:
                sets = []
                loop = g
                for g in loop:
                    sets.append(self.gcycle(g))
                gx = setCrossProd(sets)
                gs = self.unique_list(gx)
        return Group(self.gtype,self.mod,gs)



                
            
    


