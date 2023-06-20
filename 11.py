import time
import random
import math

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


def merge (lft, rgt, out=[]):
    '''Merge two input lists.
    lft: first  input list (must be sorted)
    rgt: second input list (must be sorted)
    out: list into which the result is to be stored (is created if not given)'''
    nl = len(lft)               # get number of elements in input lists
    nr = len(rgt)               # and create output list if necessary
    if len(out) < nl+nr: out = [None] *(nl+nr)
    o = l = r = 0               # initialize list indices (output, left, right)
    while l < nl and r < nr:    # while neither input list is empty
        if lft[l] < rgt[r]:     # if next element in left  list is smaller
            out[o] = lft[l]; l += 1 # move it to the output list
        else:                   # if next element in right list is smaller
            out[o] = rgt[r]; r += 1 # move it to the output list
        o += 1                  # one element moved to the output list
    if l < nl: out[o:] = lft[l:]# append remainder of left  list
    else:      out[o:] = rgt[r:]# append remainder of right list
    return out                  # return the result of the merging


def mergesort1 (X):
    '''Sort a list with Mergesort. Sorting is "in place" (i.e. changes the list)
    X: list to sort (containing any comparable items)
    returns the sorted list for convenience (despite "in place" sorting)'''
    n = len(X)                  # get the number of list elements
    if n <  2: return X         # less than two elements need no sorting
    if n <= 2:                  # if there are only two list elements
        if X[0] > X[1]: X[0],X[1] = X[1],X[0]
        return X                # optimize with a conditional swap
    mid = n // 2                # split into roughly equal halves
    lft = mergesort1(X[:mid])   # recursively sort the left  half
    rgt = mergesort1(X[mid:])   # recursively sort the right half
    return merge(lft, rgt, X)   # merge sorted sublist and return result


# Definieren Sie hier Ihre heap_sort Funktion

# Definieren Sie hier Ihre mergesort1 Funktion

def time_test(sort_func, n, iterations=5):
    total_time = 0
    for _ in range(iterations):
        numbers = [random.randint(0, 10000) for _ in range(n)]
        start_time = time.time()
        sort_func(numbers)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / iterations

ks = list(range(14, 21))
ns = [2**k for k in ks]
results = []

for n in ns:
    merge_time = time_test(mergesort1, n)
    merge_time_ratio = merge_time / (n * math.log2(n))
    heap_time = time_test(heap_sort, n)
    heap_time_ratio = heap_time / (n * math.log2(n))
    results.append((n, merge_time, merge_time_ratio, heap_time, heap_time_ratio))

# Print results
print("n\tMergesort Time\tMergesort Time Ratio\tHeapsort Time\tHeapsort Time Ratio")
for n, merge_time, merge_time_ratio, heap_time, heap_time_ratio in results:
    print(f"{n}\t{merge_time}\t{merge_time_ratio}\t{heap_time}\t{heap_time_ratio}")
