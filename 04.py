## Using the optimal solutions for comparing so we get the right values
#Aufgabenblatt 4

#Aufgabe 9:
print("Aufgabe 9")
def mean_naive1 (X):
    s = 0; i = 0                # initialize (partial) sum and counter
    for x in X:                 # traverse the stream elements
        s += x                  # add current element to sum
        i += 1                  # count the current element
    if i < 1: return 0          # safeguard: need at least one element
    return s / i                # compute and return the mean value

def mean_improved2 (X):
    mu = 0; i = 0               # initialize (partial) mean and counter
    for x in X:                 # traverse the stream elements
        i  += 1                 # count the current element
        mu += (x-mu) /i         # update the (partial) mean
    return mu                   # return the computed mean

def kahanMean(X):
    z = 0   # actual sum
    c = 0   # correction variable
    counter = 0

    for x in X:         # traverse the elements / data points
        y = x - c       # incorporate correction into value
        t = z + y       # compute the next sum
        c = (t-z)-y     # (t − z) is the actual increase
        z = t           # c is the difference between
        counter += 1
    return z/counter    # the correct and the actual increase

print(mean_naive1([1,2,3,4,5]))
print(mean_improved2([1,2,3,4,5]))
print(kahanMean([1,2,3,4,5]))

from random import seed, randrange

seed(7)                         # init. pseudo-random number generator
r = 6; n = 10**r                # (decimal logarithm of) the number of values
Y = [randrange(0, 2**52) for i in range(n)]
X = [float(y) for y in Y]       # convert to floating point numbers
Z = [int(x)   for x in X]       # convert back to integer (sanity check)
print('ok' if Y == Z else 'fail') # check whether result equals original
t = '%d' % sum(Y)               # print exact mean from integer sum
exact = [t[:-r], t[-r:]]
print('exact:     %s.%s' % (t[:-r], t[-r:]))
print('kahan:     %.18g' % kahanMean(X))
print('naive1:    %.18g' % mean_naive1(X))
print('improved2: %.18g' % mean_improved2(X))
exa = 2249725209498336.658365
print(exa - kahanMean(X))
print(exa - mean_naive1(X))
print(exa - mean_improved2(X))
#Zeigt die verschiedenen abweichungen, jedoch ist auch dies durch die berechnung
#nicht ganz genau aber es gibt einen guten einblick wie groß die differenz ist.
print("-"*30)
# Wie man erkennt anhand der print ausgabe ist der improved2 und und naive1 ansatz
#am weitesten vom exact weg, nicht nur bei der nachkommastelle sondern auch bei der Ganzzahl.
#kahans approach ist sehr knapp an der exact variante dran, bei diesem beispiel nur um 0.158
#unterscheiden sich die zwei

#Aufgabe 10
print("Aufgabe 10")
import math

def var_naive(X):
    i = 0
    z = 0
    z2 = 0
    q = 0
    q2 = 0
    for x in X:
        z2 = z + x
        q2 = q+x*x
        i += 1
