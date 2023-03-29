import sys
import random

def find_counterexamplesys():

    # Aufgabe 06a

    # Systematischer Approach. Die Zahlen sind von uns so festgelegt da es anders nicht
    # funktioniert. Ist dies der richtige Weg? Funktioniert nur mit spezifischen start zahlen.
    a = 0.1
    b = 0.0
    c = 0.0

    while True:
        z = (a + b) + c
        y = a + (b + c)
        if z != y:
            print(y, z)
            break
        a += 0.1
        if z != y:
            print(y, z)
            break
        b += 0.1
        if z != y:
            print(y, z)
            break
        c += 0.1
        if z != y:
            print(y, z)
            break
    print(a, b, c)
    print("----------------------------")
    # Aufgabe 06b
    # Bei diesen Zahlen ist das Ergebnis nicht gleich.
    # Dies würde Punkt zwei beantworten.
    a = 0.4
    b = 0.1
    c = 0.2
    z = (a + b) + c
    y = a + (b + c)
    print(z, y)
    if z == y:
        print("Das Ergebnis ist gleich")
    else:
        print("Das Ergebnis ist nicht gleich")

find_counterexamplesys()

def mean_naive (X):
    sum = 0
    for i in X:
        pass
