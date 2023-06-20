def sift(H, l, r, v):
    i = 2*l + 1  # Index des ersten Kindes berechnen
    while i < r:  # Absink-Schleife (solange im Heap)
        if i + 1 < r and H[i + 1] > H[i]:  # wenn das zweite Kind größer ist,
            i = i + 1  # zum zweiten Kind gehen
        if v >= H[i]:  # wenn das Absink-Element größer oder gleich dem ausgewählten Kind ist,
            break  # abbrechen
        H[l] = H[i]  # das Kind im Heap aufsteigen lassen
        l = i  # zum aufgestiegenen Kind gehen
        i = 2*i + 1  # Index des ersten Kindes berechnen
    H[l] = v  # das Absink-Element speichern

def build_max_heap(H):
    n = len(H)
    for i in reversed(range(n//2)):
        sift(H, i, n, H[i])

import random

# Erstelle eine Liste mit 10.000 zufälligen Elementen
numbers = [random.randint(0, 10000) for _ in range(10000)]

# Baue den Max-Heap
build_max_heap(numbers)
print(numbers)
# Prüfe, ob der erstellte Heap die Max-Heap-Eigenschaft erfüllt
for i in range(len(numbers)//2):
    if numbers[i] < numbers[2*i+1] or (2*i+2 < len(numbers) and numbers[i] < numbers[2*i+2]):
        print("Max-Heap-Eigenschaft verletzt an Index", i)

def heap_sort(H):
    n = len(H)

    # Erstelle Max-Heap
    build_max_heap(H)

    # Sortiere die Elemente
    for i in reversed(range(n)):
        # Tausche das größte Element (Wurzel des Heaps) mit dem letzten Element des Heaps
        H[0], H[i] = H[i], H[0]

        # Lasse das neue Wurzelelement im verbleibenden Heap absinken
        sift(H, 0, i, H[0])

# Erstelle eine Liste mit 10.000 zufälligen Elementen
numbers = [random.randint(0, 10000) for _ in range(10000)]

# Sortiere die Liste mit Heapsort
heap_sort(numbers)

# Überprüfe, ob die Liste sortiert ist
for i in range(1, len(numbers)):
    if numbers[i-1] > numbers[i]:
        print("Liste nicht sortiert an Index", i)
print(numbers)
