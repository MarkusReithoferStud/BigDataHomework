import random

#Aufgabe 15
print("Aufgabe 15")
def boyerMoore(X):
    counter = 0
    candidate = None
    length = 0

    for x in X:
        if x == candidate:
            counter += 1
        elif candidate == None:
            candidate = x
            counter = 1
        else:
            counter -= 1
            if counter == 0:
                candidate = None
        length += 1
    counter = 0
    for x in X:
        if x == candidate:
            counter += 1

    if counter > length/2:
        return candidate, counter

    return None, counter

# Beispiel for keine majority
print(boyerMoore([5,3,5,4,5,6,9,9,7]))

#TestCase
print("TestCase:")

startValue = 1      # Range für die testumgebung mit start und end value bestimmt
endValue = 10
length = 10         # wie lang sollte der Stream sein?
iterations = 0
while True:
    lst = [random.randrange(startValue, endValue, 1) for _ in range(length)]
    can, counter = boyerMoore(lst)
    iterations += 1
    if can != None:
        print(lst)
        print(f'How many iterations: {iterations}')
        print(f'Candidate: {boyerMoore(lst)[0]}, counter: {boyerMoore(lst)[1]}')
        break
print("-"*30)


#Aufgabe 16
print("Aufgabe 16")
def boyerMoore2(X):
    counter = 0
    candidate = None
    length = 0

    for x in X:
        if x == candidate:
            counter += 1
        elif candidate == None:
            candidate = x
            counter = 1
        else:
            counter -= 1
            if counter == 0:
                candidate = x  # current element ist neuer candidate
                counter = 1    # counter wird auf 1 gesetzt für neuen candidate
        length += 1
    counter = 0
    for x in X:
        if x == candidate:
            counter += 1

    if counter >= length/2:     # > auf >= geändert
        return candidate, counter

    return None, counter

# für diese Beispiel funktioniert die Änderung so, dass der candidate direkt mit dem neuen element überschrieben wird
# dies funktioniert wenn der candidate als letzte stelle des Streams ist, da beim letzten durchlauf das letzte element
# als neues Element aufgenommen wird.
X = [2,1,3,1,4,1,5,1,6,1]
print(X)
print(boyerMoore(X))
print(boyerMoore2(X))
print("------")

# Für dieses Beispiel funktioniert der Algorithmus nicht, da der candidate nicht als letztes Element steht
# Wenn der candidate nicht das letzte Element ist, müsste man den Algorithmus nicht bis 0 counten lassen
# sondern bis ins negative, da bei z.b 6 Elementen, davon 3 1er bei der 0 als counter der candidate verschwindet.
# müsste man also bis ins negative zählen um so den candidate auch bei so einer zahlenfolge aufrecht zu erhalten.
# jedoch funktioniert dies dann wiederum nicht für den anderen Fall wenn der candidate am ende steht.
Y = [1,1,1,2,3,4]
print(Y)
print(boyerMoore(Y))
print(boyerMoore2(Y))
print("-"*30)


#Aufgabe 17
print("Aufgabe 17")
def misraGries(X, k):
    candidate = {}      # dict inizierien
    for x in X:         # durch Liste gehen
        if x in candidate:      # checken ob Element in dict ist
            candidate[x] = candidate[x] + 1     # wenn ja dann + 1 value
        elif len(candidate) < k - 1:            # sonst wenn länge von dict < k-1
            candidate[x] = 1                    # dict eintrag von element mit value 1 erstellen
        else:                                   # sonst durch dict gehen
            for y in candidate:                 # und alle values um 1 decrementieren
                candidate[y] = candidate[y] - 1
            candidate = {key: value for key, value in candidate.items() if value != 0}  # da man ein dict nicht während
            # dem durchlauf verändern kann, erstellen wir ein neues dict, welches nur key value pairs hat die als value
            # > 0 sind

    for y in candidate: # setzte für übrigen key value pairs den counter neu auf 0
        candidate[y] = 0
    for x in X:         # gehe durch die Liste neu durch
        if x in candidate:      # check ob schon in dict ist
            candidate[x] = candidate[x] + 1 # erhöhren die value
    lst = list(zip(candidate.keys(), candidate.values()))
    candidateList = []
    for i in lst:
        if i[1] > len(X)/k:
            candidateList.append(i[0])
    if candidateList:
        return candidateList

# 1 element kommt n/k mal vor
print(misraGries([9,3,9,4,9,6,9,9,7,9,4,9], 4))
# 2 elemente kommen n/k mal vor
print(misraGries([9,3,9,4,9,6,9,9,7,9,4,9,4,4], 4))
# kein element kommt n/k mal vor
print(misraGries([9,3,2,4,9,6,8,3,7,9,4,2], 4))
print("------")
# Testumgebung für Aufgabe 17
startValue = 1      # Range für die testumgebung mit start und end value bestimmt
endValue = 12
length = 12         # wie lang sollte der Stream sein?
iterations = 0
k = 8
while True:
    lst = [random.randrange(startValue, endValue, 1) for _ in range(length)]
    can, counter = boyerMoore(lst)
    iterations += 1
    if can != None:
        print(lst)
        print(f'How many iterations: {iterations}')
        print(f'Candidate Elements are: {misraGries((lst), k)}')
        break

# wir haben beobachtet, dass wenn man die spanne aus start und end-wert vergößert der Algorithmus länger braucht um
# unter anderem ein candiadte elemnt zu finden
# k ist unser testanspruch den wir mit 4 festgelegt haben
# da k im Nenner steht ist die Hürde für Elemente entweder größer oder kleiner um als candidat valide zu sein
