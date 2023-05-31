import random
import matplotlib.pyplot as plt

#Aufgabe 22
def erzeuge_datenstrom1(objekt_anzahl, datenpunkte_anzahl):
    objekte = list(range(objekt_anzahl))
    datenstroeme = random.choices(objekte, k=datenpunkte_anzahl)
    return datenstroeme

def erzeuge_datenstroeme2(objekt_anzahl, datenpunkte_anzahl):
    # Definiere die Gewichtung für die Objekte
    gewichtung = [random.choice([1, 2, 5, 15, 50, 100, 130]) for _ in range(objekt_anzahl)]

    objekte = list(range(objekt_anzahl))

    # Erzeuge die Datenströme basierend auf der Gewichtung
    datenstroeme = random.choices(objekte, weights=gewichtung, k=datenpunkte_anzahl)

    return datenstroeme


def plot1():
    # Aufruf der Funktion mit den gewünschten Parametern
    datenstroeme = erzeuge_datenstrom1(60, 10000)

    # Berechne die Anzahl der Datenpunkte pro Objekt
    objekt_haeufigkeit = {}
    for objekt in datenstroeme:
        if objekt not in objekt_haeufigkeit:
            objekt_haeufigkeit[objekt] = 0
        objekt_haeufigkeit[objekt] += 1

    # Erstelle das Säulendiagramm
    objekte = list(objekt_haeufigkeit.keys())
    haeufigkeiten = list(objekt_haeufigkeit.values())

    plt.bar(objekte, haeufigkeiten)
    plt.xlabel('Objekte')
    plt.ylabel('Anzahl der Datenpunkte')
    plt.title('Verteilung der Datenpunkte auf Objekte')
    plt.ylim(0, 800)
    plt.show()



def plot2():
    # Aufruf der Funktion mit den gewünschten Parametern
    datenstroeme = erzeuge_datenstroeme2(60, 10000)

    # Berechne die Anzahl der Datenpunkte pro Objekt
    objekt_haeufigkeit = {}
    for objekt in datenstroeme:
        if objekt not in objekt_haeufigkeit:
            objekt_haeufigkeit[objekt] = 0
        objekt_haeufigkeit[objekt] += 1

    # Erstelle das Säulendiagramm
    objekte = list(objekt_haeufigkeit.keys())
    haeufigkeiten = list(objekt_haeufigkeit.values())

    plt.bar(objekte, haeufigkeiten)
    plt.xlabel('Objekte')
    plt.ylabel('Anzahl der Datenpunkte')
    plt.title('Verteilung der Datenpunkte auf Objekte')

    plt.show()

plot1()
plot2()

# Aufgabe 23
import random

def process_element_regular(counters, element, index, fraction):
    if index % int(1/fraction) == 0:
        if element not in counters:
            counters[element] = index

def process_element_random(counters, element,index, fraction):
    if random.random() < fraction:
        if element not in counters:
            counters[element] = index

def estimate_second_moment_efficient(counters):
    n = len(counters)
    if n == 0:
        return 0
    else:
        return sum((n - i) * (n - i) for i in counters.values()) / n

# Initialisieren Sie die Zähler
counters = {}

stream = [1,1,1,2,3,4,5,6,7,7,7]
steam = [1,2,3,4,5,5,5,6,7,8,9]

# Verarbeiten Sie jedes Element im Datenstrom
for i, element in enumerate(stream):
    process_element_regular(counters, element, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment_efficient(counters)

print("Estimated second moment (regular):", second_moment)

# Initialisieren Sie die Zähler erneut
counters = {}

for i, element in enumerate(stream):
    process_element_random(counters, element, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment_efficient(counters)

print("Estimated second moment (random):", second_moment)

# Aufgabe 23 Zusatz
# man bräuchte zwei Werte. Das erste Auftreten des Elemnts und wie oft dieses seitdem
# wiedererschienen ist.

def process_element_zusatz_regular(counters, element, index, fraction):
    if index % int(1 / fraction) == 0:
        if element not in counters:
            counters[element] = [index, 1]
        else:
            counters[element][1] += 1

def process_element_zusatz_random(counters, element, index, fraction):
    if random.random() < fraction:
        if element not in counters:
            counters[element] = [index, 1]
        else:
            counters[element][1] += 1


def estimate_second_moment(counters):
    n = sum(val[1] for val in counters.values())
    if n == 0:
        return 0
    else:
        return sum((n - val[0]) * (n - val[0]) * val[1] for val in counters.values()) / n

# Initialisieren Sie die Zähler
counters = {}

# Verarbeiten Sie jedes Element im Datenstrom
for i, element in enumerate(stream):
    process_element_zusatz_regular(counters, element, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment(counters)

print("Estimated second moment (regular):", second_moment)

# Initialisieren Sie die Zähler erneut
counters = {}

for i, element in enumerate(stream):
    process_element_zusatz_random(counters, element, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment(counters)

print("Estimated second moment (random):", second_moment)


# Aufgabe 24
def true_second_moment(stream):
    counters = {}
    for element in stream:
        if element not in counters:
            counters[element] = 0
        counters[element] += 1
    return sum(val ** 2 for val in counters.values())


def test_regular():
    for fraction in [0.01, 0.05, 0.1, 0.5, 1.0]:
        print(f'\nTesting for fraction: {fraction}')

        for erzeuge_datenstrom in [erzeuge_datenstrom1, erzeuge_datenstroeme2]:
            stream = erzeuge_datenstrom(60, 10000)

            counters = {}
            for i, element in enumerate(stream):
                process_element_zusatz_regular(counters, element, i, fraction)

            second_moment_estimate = estimate_second_moment(counters)
            true_second_moment_value = true_second_moment(stream)

            print(f"Estimated second moment: {second_moment_estimate}")
            print(f"True second moment: {true_second_moment_value}")
            print(f"Number of unique objects for which counters were created: {len(counters)}\n")


def test_random():
    for fraction in [0.01, 0.05, 0.1, 0.5, 1.0]:
        print(f'\nTesting for fraction: {fraction}')

        for erzeuge_datenstrom in [erzeuge_datenstrom1, erzeuge_datenstroeme2]:
            stream = erzeuge_datenstrom(60, 10000)

            counters = {}
            for i, element in enumerate(stream):
                process_element_zusatz_random(counters, element, i, fraction)

            second_moment_estimate = estimate_second_moment(counters)
            true_second_moment_value = true_second_moment(stream)

            print(f"Estimated second moment: {second_moment_estimate}")
            print(f"True second moment: {true_second_moment_value}")
            print(f"Number of unique objects for which counters were created: {len(counters)}\n")

print("test regular")
test_regular()
print("test random")
test_random()
