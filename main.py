def depths(s):
    stack = []
    ret= []
    depth = 0

    for i in s:
        if i == "(":
            stack.append(i)

        if i == ")":
            stack.pop()
            depth += 1

        if len(stack) == 0 and depth != 0:
            ret.append(depth)
            depth = 0

    return ret

print(depths("(((((((()))))))) ()(( )) ((( )()()))" ))

import time


def cshift (X, k):
    # Check that k meets the condition
    n = len(X)
    if 0 <= k < n:
        # create two copies of the list X with the
        firstList = X[k:]
        secondList = X[:k]
        # add both lists together to create one list where the values are shifted based on k
        shiftedList = firstList + secondList
    else:
        # if no requirements are met, return an Expectopn
        return Exception("The Input does not meet the requirements")

    return shiftedList

    '''
     Wie häangt die Laufzeit Ihrer Funktion vom Wert von k ab?
    Wie hängt sie von der Läange n der Sequenz X ab?
    (Hinweis: Ist die Laufzeit unabhäangig von k und/oder n? Ist sie proportional zu k
    und/oder n? Ist sie eine Funktion von k und/oder n? Seien Sie sehr vorsichtig
    bei der Bestimmung der Abhäangigkeit von n.)

    -> Die Laufzeit von der Funktion ist abhängig von der Länge von X. Die Slice Operationen
    werden jeweils nur einmal ausgeführt egal wie groß oder klein k ist und erstellen dabei eine
    Kopie. 
    Die Funktion ist unabhängig von k, da k nur als parameter gilt mit dem die Liste
    verschoben wird. Jedoch ist sie abhängig von n bzw der länge von X.
    Die Funktion ist proportional zur Länge von X.
    
    Anderer Ansatz mit Rekursion k mal eine funktion aufrufen die die eingabeliste um 1 verschiebt.
    dies wäre dann von n und k abhängig
    '''

print(cshift([1, 2, 3, 4, 5], 2))
print("-------------")
def is_bitonic (X):
    if X[0] > min(X):
        lowIndex = X.index(min(X))
        firstList = X[:lowIndex]
        secondList = X[lowIndex:]
        X = secondList + firstList
        print(X)


    pre = X[0]
    for i in X:
        pass




#print(is_bitonic([1,2,3,4,5,6] ))
#print(is_bitonic([4,3,2,1,2,3]))
print(is_bitonic([4,3,2,1,2,3,2,1]))
#print(is_bitonic([4,2,2,1,3,4,4,5]))
