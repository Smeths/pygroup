SG = G.Sub(g)

    def Sub(self,g):
        if type(g) == int:
            gs = gcycle(g)
        elif type(g) == list and type(self.gType) == str:
            sets = []
            loop = g
            for g in loop:
                sets.append(gcycle(g))
            gx = setCrossProduct(sets)
            gs = []
            for x in gx:
                gs.append(op(x))
            gs = set(tuple(x) for x in gs)
        elif type(g) == list and type(self.gType) == list:
            if type(g[0]) == int:
                gs = gcycle(g)
            elif type(g[0]) == list:
                sets = []
                loop = g
                for g in loop:
                    sets.append(gcycle(g))
                gx = setCrossProduct(sets)
                gs = []
                for x in gx:
                    gs.append(op(x))
                gs = set(tuple(x) for x in gs)
        return Group(self.gType,self.mod,gs)

I think the identity should be the last element in gs, check this is always true
                
            
            
        

1) gcycle all elements
2) setcross all gcycles

create object of class G with:

1) list of elements
2) mod defined as self.mod
3) gType defined as self.gType

set self.i (should be able to obtain from the list of elements)
set self.mod
set self.gType
set self.gList and self.gDict





