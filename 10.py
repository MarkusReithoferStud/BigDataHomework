#Aufgabe 25
def merge_sort(lst):
    if len(lst) <= 1:  # Basisfall: Eine Liste mit 0 oder 1 Elementen ist bereits sortiert
        return lst
    # Teile die Liste in zwei Hälften
    #nehme unteres Element bei ungerade durch //
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    #print(left_half)
    #print(right_half)
    # Sortiere die beiden Hälften (rekursiv)
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    # Führe die beiden sortierten Hälften zusammen
    return merge(left_half, right_half)

def merge(left, right):
    mergedList = []
    while left and right:  # Solange beide Listen nicht leer sind
        if left[0] <= right[0]:  # Nimm das kleinere Element von beiden Listen
            mergedList.append(left.pop(0))
        else:
            mergedList.append(right.pop(0))
    # Füge die übrigen Elemente der nicht leeren Liste hinzu
    if left:
        mergedList.extend(left)
    if right:
        mergedList.extend(right)
    return mergedList



import random

# Radnom int liste mit 100000 Zahlen, da bei 1000000 das Program nicht durchläuft
random_numbers = [random.randint(1, 10) for _ in range(10)]

sorted_numbers = merge_sort(random_numbers)

# Überprüfen Sie, ob die Liste sortiert ist (die nächsten beiden Zahlen sollten identisch sein)
print(sorted_numbers)
print(sorted_numbers == sorted(random_numbers))
#print(random_numbers)


# Aufgabe 26

import random
# wiederverwnedung von dem sortieren
def merge_sort_online(X):
    buffer = [None]
    for x in X:
        sorted_element = [x]
        for level in range(len(buffer)):
            # wenn level von buffer leer ist -> True
            # Wenn das aktuelle Level im Puffer leer ist, speichern wir den bereits sortierten Wert in diesem Level.
            # Falls das letzte Element im Puffer nicht leer ist, fügen wir ein weiteres None Element am Ende hinzu.
            if not buffer[level]:
                buffer[level] = sorted_element
                # wenn None skip, wenn zahl add None oben drauf (Platzhalter)
                if buffer[-1]:
                    buffer.append(None)
                break
                # Wenn das aktuelle Level im Puffer nicht leer ist, führen wir eine Mischoperation durch, um die Werte
                # im aktuellen Level und den bereits sortierten Wert zusammenzuführen.
            buffer[level], sorted_element = None, merge(buffer[level], sorted_element)
        # Falls das letzte Element im Puffer nicht leer ist, fügen wir ein weiteres None Element am Ende hinzu.
        # Wir speichern das gemischte Element am letzten Platz im Puffer.
        if buffer[-1]:
            buffer.append(None)
        # zwischenzeitig das oberste Element ist die sortierte Liste
        buffer[-1] = sorted_element

    #Hier kombinieren wir alle gemischten Elemente im Puffer zu einer endgültig sortierten Liste.
    sorted_list = []
    for level in range(len(buffer)):
        #if true skip iteration
        if not buffer[level]: continue
        sorted_list = merge(buffer[level], sorted_list)
    return sorted_list


random_numbers2 = [random.randint(0, 10) for _ in range(5)]
sorted_numbers1 = merge_sort_online(random_numbers2)
print(sorted_numbers1)
