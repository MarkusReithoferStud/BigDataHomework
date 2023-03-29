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

    i = 0 
    z = 0
    mu = 0
    for x in X:
        i += 1
        z += x
        mu = (z/i)
    return mu
    
def mean_improved (X):
    i = 0
    meanOld = 0
    #we look for the meanOld and meanNew according to the formula
    #wenn in der liste kleine auf große Zahlen vorkommen, kann es zu Rundungsfehlern kommen durch die Rechenoperatoren
    #man müsste die Annordnung #ndern.
    for x in X:
        meanNew = (x+(i+1)*meanOld-meanOld)/(i+1)
        meanOld = meanNew
        i+=1
        mu = meanNew
    return meanNew

print(mean_improved([1,2,3,4,5]))

import random

def Testumgebung():
    X = [1]
    diff = 0.0
    while not diff != 0:
        diff = abs(mean_naive(X) - mean_improved(X))
        print(mean_naive(X))
        print(mean_improved(X))
        X.append(random.randint(1,2))
        print(sum(X)/len(X))
    return diff

print(Testumgebung())

