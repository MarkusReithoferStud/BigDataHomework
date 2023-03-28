import sys
import random

# Aufgabe 06a
def find_counterexamplesys():
    tests = 1000000
    max_val = sys.float_info.max
    print(max_val)
    min_val = sys.float_info.min
    print(min_val)
    counter = 0

    for i in range(tests):
        a = random.uniform(min_val, max_val)
        b = random.uniform(min_val, max_val)
        c = random.uniform(min_val, max_val)
#würde code gerne so ändern, dass die for schleife c immer größer macht und 
#so lange durchgeht bis c sozusagen großgenug ist um ein ergbnis zuerzeugen, dass unterschiedlich groß ist
# weil so dreimal ranodm ist es nicht systematisch
        erg1 = (a + b) + c
        erg2 = a + (b + c)
        counter += 1
        print(counter)

        if erg1 != erg2:
            print("Gegenbeispiel gefunden:\n")
            print(f"( {a} + {b} ) + {c} = {erg1}\n")
            
            print(f"{a} + ( {b} + {c} ) = {erg2}")
            return
        
    print("Kein Gegenbeispiel gefunden.")

find_counterexamplesys()

#print(pi)
#print(e)

erg1 = (1e-308 + 1e308) + 1
erg2 = 1e-308 + (1e308 + 1)
print(1e-35 + 1e35)
print(erg1)
print(erg2)

## versteh nicht warum er mir da immer noch float true ausgibt

print(erg1 == erg2)