import random
import matplotlib.pyplot as plt

#Aufgabe 22
def generate_datastream1(objekt_anzahl, datenpunkte_anzahl):
    objekte = list(range(objekt_anzahl))
    datenstrom = random.choices(objekte, k=datenpunkte_anzahl)
    return datenstrom

def generate_datastream2(objekt_anzahl, datenpunkte_anzahl):
    # die zahlen in der Liste können geändert werden, sind dann die Gewichte für die 60 Objekte
    gewichtung = [random.choice([1, 2, 5, 15, 50, 100, 130]) for _ in range(objekt_anzahl)]

    objekte = list(range(objekt_anzahl))

    # Erzeuge die Datenströme basierend auf der Gewichtung
    datenstrom = random.choices(objekte, weights=gewichtung, k=datenpunkte_anzahl)

    return datenstrom


def plot1(): #erstes Histogramm
    datastream = generate_datastream1(60, 10000)

    # Berechne die Anzahl der Datenpunkte pro Objekt
    objekt_häufigkeit = {}
    for objekt in datastream:
        if objekt not in objekt_häufigkeit:
            objekt_häufigkeit[objekt] = 0
        objekt_häufigkeit[objekt] += 1

    # Erstelle das Säulendiagram
    objekte = list(objekt_häufigkeit.keys())
    häufigkeiten = list(objekt_häufigkeit.values())

    plt.bar(objekte, häufigkeiten)
    plt.xlabel('Objekte')
    plt.ylabel('Anzahl der Datenpunkte')
    plt.title('Verteilung der Datenpunkte auf Objekte')
    plt.ylim(0, 800)
    plt.show()



def plot2(): #zweites Histogramm
    datastream = generate_datastream2(60, 10000)

    # Berechnet die Anzahl der Datenpunkte pro Objekt neu
    objekt_häufigkeit = {}
    for objekt in datastream:
        if objekt not in objekt_häufigkeit:
            objekt_häufigkeit[objekt] = 0
        objekt_häufigkeit[objekt] += 1

    # Erstelle das Säulendiagramm
    objekte = list(objekt_häufigkeit.keys())
    häufigkeiten = list(objekt_häufigkeit.values())
    
    #anpassen des Aussehens des Hisogramms
    plt.bar(objekte, häufigkeiten)
    plt.xlabel('Objekte')
    plt.ylabel('Anzahl der Datenpunkte')
    plt.title('Verteilung der Datenpunkte auf Objekte')

    plt.show()

plot1()
plot2()

# Aufgabe 23
import random

#Counter implementiere

def process_element_konstant(counters, element, index, fraction):
    if index % int(1/fraction) == 0:
        if element not in counters:
            counters[element] = index

def process_element_random(counters, element,index, fraction):
    if random.random() < fraction:
        if element not in counters:
            counters[element] = index

def estimate_second_moment23(counters): #ASM Algorithmus
    n = len(counters)
    if n == 0:
        return 0
    else:
        return sum((n - i) * (n - i) for i in counters.values()) / n #formel wie in VO Folien

# Initialisieren Sie die Zähler
counters = {}

stream = [1,1,1,2,3,4,5,6,7,7,7]
steam = [1,2,3,4,5,5,5,6,7,8,9]

#jedes Element im Datenstrom verarbeietn
# counter = Zähler pro Element, auswahl ist die auswahlrate
for i, e in enumerate(stream):
    # für index als auch element index i und element e
    process_element_konstant(counters, e, i, 0.5)

# Den zweiten Moment schätzen
second_moment = estimate_second_moment23(counters)

print("Estimated second moment (regular):", second_moment)

# Initialisieren Sie die Zähler erneut
counters = {}

for i, e in enumerate(stream):
    process_element_random(counters, e, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment23(counters)

print("Estimated second moment (random):", second_moment)

# Aufgabe 23 Zusatz
# man bräuchte zwei Werte. Das erste Auftreten des Elemnts und wie oft dieses seitdem
# wiedererschienen ist.

def process_element_zusatz_konstant(counters, element, index, fraction):
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


def estimate_second_moment23_zusatz(counters):
    n = sum(val[1] for val in counters.values())
    if n == 0:
        return 0
    else:
        return sum((n - val[0]) * (n - val[0]) * val[1] for val in counters.values()) / n

#den Zähler initialisieren
counters = {}

#wir verbarbeiten erneut jedes Element im Datenstrom mit 0.5 als fraction
for i, e in enumerate(stream):
    process_element_zusatz_konstant(counters, e, i, 0.5)

# Schätzen Sie den zweiten Moment
second_moment = estimate_second_moment23_zusatz(counters)

print("Estimated second moment (regular):", second_moment)



# Aufgabe 24
def true_second_moment(stream):
    counters = {}
    for element in stream:
        if element not in counters:
            counters[element] = 0
        counters[element] += 1
    return sum(val ** 2 for val in counters.values()) #n**2 + (n+1)**2+ ....

# Tests für den regular ablauf
def test_konstant():
    for fraction in [0.01, 0.05, 0.1, 0.5, 1.0]:
        print(f'\nFraction: {fraction}')#jede fraction wird einzeln betrachtet

        for datastream in [generate_datastream1, generate_datastream2]:# beide unsere Datenströme werden verarbietet
            stream = datastream(60, 10000) #bei beiden wird stream erstellt 

            counters = {}
            for i, element in enumerate(stream):
                process_element_zusatz_konstant(counters, element, i, fraction) # hier unterschiefd zu random

            second_moment_estimate = estimate_second_moment23_zusatz(counters)
            true_second_moment_value = true_second_moment(stream)

            print(f"Geschätzter zweiter Moment: {second_moment_estimate}")
            print(f"Wahrer zweiter Moment : {true_second_moment_value}")
            print(f"Anzahl der verschiedenen Objekte für die wir einen Zähler angelegt haben: {len(counters)}\n")

#Test für den random Ablauf
def test_random():
    for fraction in [0.01, 0.05, 0.1, 0.5, 1.0]:
        print(f'\nFraction: {fraction}')

        for datastream in [generate_datastream1, generate_datastream2]:
            stream = datastream(60, 10000)

            counters = {}
            for i, element in enumerate(stream):
                process_element_zusatz_random(counters, element, i, fraction)#hier unterschied zu konstant

            second_moment_estimate = estimate_second_moment23_zusatz(counters)
            true_second_moment_value = true_second_moment(stream)

            print(f"Geschätzter zweiter Moment: {second_moment_estimate}")
            print(f"Wahrer zweiter Moment : {true_second_moment_value}")
            print(f"Anzahl der verschiedenen Objekte für die wir einen Zähler angelegt haben: {len(counters)}\n")

print("test regular")
test_konstant()
print("test random")
test_random()
