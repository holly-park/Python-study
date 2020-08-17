import simplemodule

print(simplemodule.add(1,2,3,4,5))
print(simplemodule.evenAdd(1,3,5,2,4,6))
print(simplemodule.isEven(5))


import simplemodule as simp
print(simp.add(1,2,3,4,5))
print(simp.evenAdd(1,3,5,2,4,6))
print(simp.isEven(5))


from simplemodule import *
print(add(1,2,3,4,5))
print(evenAdd(1,3,5,2,4,6))
print(isEven(5))