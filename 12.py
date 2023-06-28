def quicksort(X, check=False):
    if len(X) <= 1:
        return X
    else:
        pivot = X[len(X) // 2]  # Pivot ist das mittlere Element
        lesserPart = [x for x in X if x < pivot]    # Elemente kleiner als Pivot
        equalPart = [x for x in X if x == pivot]    # Elemente gleich dem Pivot / Problem extra durchlauf für == Elemente
        greaterPart = [x for x in X if x > pivot]   # Elemente größer als Pivot

        if check:
            if len(lesserPart) == 0:
                print("Leere Liste kleiner als Pivot")
            if len(greaterPart) == 0:
                print("Leere Liste größer als Pivot")

        return quicksort(lesserPart, check) + equalPart + quicksort(greaterPart, check)   # Sortierte Teile zusammenfügen

# Implementierung testen
import random
testList = [random.randint(0, 100000) for _ in range(10000)] # Liste mit 10.000 Zufallszahlen
sortedList = ["Testing"]
#sortedList = quicksort(testList)

print(f'Liste ist sortiert: {sortedList == sorted(testList)}')
print(testList)
print(sortedList)
print("-"*30)

# Aufgabe 30
worstCaseList = [1,2,3,4,10,4,5,6,7] # [1,2,3,4,5,6,7,8], [
print(worstCaseList)
print(quicksort(worstCaseList, True))
print("-"*30)

# Eigener Zusatz: lange liste wo Größtes element hinzugefügt wird als pivot
'''
BadList = [random.randint(0, 10000) for _ in range(10000)]
index = len(BadList)//2
print(BadList)
BadList.insert(index, 10001)
print("-"*30)
print(quicksort(BadList, True))
'''


def median_of_three(A):
    mid_index = len(A) // 2
    if (A[0] - A[-1]) * (A[mid_index] - A[0]) >= 0:
        return A[0]
    elif (A[-1] - A[0]) * (A[mid_index] - A[-1]) >= 0:
        return A[-1]
    return A[mid_index]

def quicksort2(A):
    if len(A) <= 1:
        return A
    else:
        pivot = median_of_three(A)
        lesserPart = [x for x in A if x < pivot]
        equalPart = [x for x in A if x == pivot]
        greaterPart = [x for x in A if x > pivot]
        return quicksort2(lesserPart) + equalPart + quicksort2(greaterPart)





# Vergleich der Laufzeit des alten und des neuen Quicksort-Algorithmus
import random
import time

# Erzeugen einer Liste mit 10.000 Zufallszahlen
A = [random.randint(0, 100000) for _ in range(10000)]

A_copy = A.copy()

# Laufzeit des alten Quicksort-Algorithmus
start = time.time()
quicksort(A)
end = time.time()
print('Alte Quicksort-Laufzeit: ', end - start)

# Laufzeit des neuen Quicksort-Algorithmus
start = time.time()
quicksort2(A_copy)
end = time.time()
print('Neue Quicksort-Laufzeit: ', end - start)

