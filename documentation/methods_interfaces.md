# Interfaces to methods

## possible inputs:

element = any element of the group (always g in the code)
list of elements = any list of elements in the group (always gs in the code)
index = index of an element as defined by gdict or glist (always ind in the code)
list of indexes = any list of element indexes as defined by gdict or glist (always inds in the code)
assorted logicals to control behaviour

## op2:

op2(element,element,owType = None)

returns: element*element according to self.gType

op2(element,element,owType = Defined)

returns: element*element according to owType (for a simple add or mult group)
returns: element*element according to self.gType (for a cross product group)

## gorder:

gorder(element,elem_return=True)

returns: {element^1, element^2, element^3,...,identity}

gorder(element,elem_return=False)

returns: the order of the element

## go:

go()

returns: returns the order of every element of the group

go(element=integer) - needs to this whether element is an integer or whether element is a list

returns: returns the order of the element

go(list of elements)

returns: returns the order of each element in the list

## op:

op(list of elements)

returns: all of the elements multiplied together

op(element, element)

returns: multiplies two elements together

## pow:

pow(element,power,owType=None)

returns: element to the power of power using multiplication defined by gType

pow(element,power,owType=Defined)

returns: element to the power of power using multiplication defined by owType

## gcycle:

gcycle(element)

returns: gorder(element,elem_return=True)

## g:

g()

returns: list of all elements in the group for add and mult groups
returns: a dictionary of elements for cross groups

g(index)

returns: the element with given index

g(list of indexes)

returns: list of all elements for all indexes in the list for add and mult groups
returns: a dictionary of elements for all indexes in the list for cross groups









