#Aufgabe 13
# Die Ansätze unten aufgelistet sind die optimal Ansätze für die jeweilige Aufgabe, z.b der naive Approach
# Dazu kommen ist unsere Funktion von mv_recursive die durch rekursives aufrufen von sich selbst den mean
# und die varianz berechnen
# ein anderer Ansatz ergab bei uns immer einen Rekursion Error wegen python rekursion limit

def mv_recursive(X, leftCut=0, RightCut=0):
    if RightCut == 0:
        RightCut = len(X)    # if no right border, get length
    n = RightCut - leftCut                # n is the length of a part right - left
    if n <= 1:  #if list contains only one element, return element as mean and var = 0
        return X[leftCut], 0

    if n <= 2:                  # solve for 2 elements when recursion hits n <=2
        leftEle = X[leftCut]
        rightEle = X[RightCut-1]
        meanEle = (leftEle+rightEle)/n
        sumSqEle = (leftEle-rightEle)**2/n
        return meanEle, sumSqEle

    midEle = (leftCut + RightCut) // 2   # compute index of middle element
    meanLeft, sQLeft = mv_recursive(X, leftCut, midEle)   # recursive call function for left part meanLeft = meanEle sQLeft = sumSqEle
    meanRigth, sQRight = mv_recursive(X, midEle, RightCut)   # recursive call function for right part meanRigth = meanEle sQRight = sumSqEle
    nleft = midEle - leftCut    # count of elements between lft and midEle
    nright = RightCut - midEle    # count of elements between midEle and rgt

    #calc mean
    mu = (nleft/n) * meanLeft + (nright/n) * meanRigth   # mu = mean of both parts, weighted by nleft/nright proportion
    #calc sigma
    sigma = ((nleft-1)/(n-1))*sQLeft + ((nright-1)/(n-1))*sQRight + (nleft/n)*(nright/(n-1)) * (meanLeft-meanRigth)**2
    return mu, sigma

#Aufgabe 14
# Für einen Online Approach brauchen wir eine Art Buffer der mitzählt auf welchem Level wir uns befinden
# in diesem Buffer sieht man sich immer nur zwei elemente an für die die Varianz und der Mean berechnet werden
#
def mv_online (X):
    buffer = []
    counter = 0
    buffer.append((None, None))
    var = 0
    for x in X:
        buffer.append((None, None))
        print(buffer[counter][0])
        if buffer[0][0] == None:
            buffer[0][0] = x
            #buffer[counter][1] = var
        elif buffer[0][0] != None:
            mean = (buffer[0][0] + x)/2
            counter += 1
            if buffer[0+counter][0] == None:
                buffer[0+counter][0] = mean
                buffer[0] = (None, None)
            elif buffer[0+counter][0] != None:
                buffer[counter+1][0] = (buffer[counter-1][0] + buffer[counter][0])/2
                buffer[counter-1][0] = (None, None)
                buffer[counter][0] = (None, None)

    return buffer


def mean_naive (X):
    s = 0                       # initialize (partial) sum
    i = 0                       # and element counter
    for x in X:                 # traverse the stream elements
        s += x                  # add current element to sum
        i += 1                  # count the current element
    if i < 1: return 0          # safeguard: need at least one element
    return s / i                # compute and return the mean value

def mean_improved (X):
    mu = 0                      # initialize (partial) mean
    i  = 0                      # and element counter
    for x in X:                 # traverse the stream elements
        i  += 1                 # count the current element
        mu += (x -mu) /i        # update the (partial) mean
    return mu                   # return the computed mean

def mean_kahan2 (X):
    mu = 0                      # initialize (partial) mean,
    c  = 0                      # correction value,
    i  = 0                      # and element counter
    for x in X:                 # traverse the sequence
        i += 1                  # count the processed element
        y = (x -mu) /i -c       # compute corrected term
        t = mu +y               # and add it to the sum
        c = (t -mu) -y          # compute new correction
        mu = t                  # set new mean value
    return mu                   # return computed mean

from random import seed, randrange

seed(7)                         # init. pseudo-random number generator
r = 6; n = 10**r                # (decimal logarithm of) number of values
Y = [randrange(0, 2**52) for i in range(n)]
X = [float(y) for y in Y]       # convert to floating point numbers
Z = [int(x)   for x in X]       # convert back to integer (sanity check)
print('ok' if Y == Z else 'fail') # check whether result equals original
t = '%d' % sum(Y)               # print exact mean from integer sum
print('naive:     %.6f'  % mean_naive(X))
print('improved:  %.6f'  % mean_improved(X))
print('kahan2:    %.6f'  % mean_kahan2(X))
print('exact:     %s.%s' % (t[:-r],t[-r:]))
print(f'{"recursive"}  {mv_recursive(X)[0]}')


print("-"*30)

from random import seed, randrange

def var_kahan1 (X):
    n  = 0                      # initialize element counter,
    s  = q  = 0                 # sum of values and sum of squares,
    cs = cq = 0                 # and correction values
    for x in X:                 # traverse the stream elements
        n += 1                  # count the current element
        y  = x -cs              # compute corrected term
        t  = s +y               # and add it to the sum
        cs = (t -s) -y          # compute new correction
        s  = t                  # set the new sum
        y  = x*x -cq            # compute corrected term
        t  = q +y               # and add it to the sum
        cq = (t -q) -y          # compute new correction
        q = t                   # set the new sum
    if n < 2: return 0          # safeguard: need at least two elements
    return (q-s*s/n) /(n-1)     # compute and return the variance

def var_kahan2 (X):
    n  = 0                      # counter for the elements
    mu = delta = 0              # mean and sum of squared deviations
    cm = cd    = 0              # correction variables for mean and delta
    for x in X:                 # traverse the stream elements
        n    += 1               # count the current element
        d     = x -mu           # compute deviation from old mean
        y     = d /n -cm        # compute corrected term
        t     = mu +y           # and add it to the sum (mean)
        cm    = (t -mu) -y      # compute new correction (mean)
        mu    = t               # set new (partial) mean value
        y     = d *(x -mu) -cd  # compute corrected term
        t     = delta +y        # and add it to the sum (squared deviations)
        cd    = (t -delta) -y   # compute new correction (squared deviations)
        delta = t               # set new (partial) sum of squared deviations
    if n < 2: return 0          # safeguard: need at least two elements
    return delta /(n-1)         # compute and return the variance

def var_improved2 (X):
    n  = 0                      # initialize element counter,
    mu = delta = 0              # and (partial) mean and delta
    for x in X:                 # traverse the stream elements
        n     += 1              # count the current element
        d      = x -mu          # compute deviation from current mean
        mu    += d /n           # update partial mean
        delta += (n-1)/n *d*d   # and partial delta
    if n < 2: return 0          # safeguard: need at least two elements
    return delta /(n-1)         # compute and return the variance

def var_improved1 (X):
    n  = 0                      # initialize element counter,
    mu = delta = 0              # and (partial) mean and delta
    for x in X:                 # traverse the stream elements
        n     += 1              # count the current element
        d      = x -mu          # compute deviation from current mean
        mu    += d /n           # update partial mean
        delta += d *(x -mu)     # and    partial delta
    if n < 2: return 0          # safeguard: need at least two elements
    return delta /(n-1)         # compute and return the variance

def var_naive (X):
    n = 0                       # initialize element counter,
    s = q = 0                   # sum of values and sum of squares
    for x in X:                 # traverse the stream elements
        n += 1                  # count the current element
        s += x                  # add element to sum of values
        q += x*x                # add square  to sum of squares
    if n < 2: return 0          # safeguard: need at least two elements
    return (q-s*s/n) /(n-1)     # compute and return the variance

def var_trivial (X):
    n  = len(X)                 # get number of elements (for convenience)
    if n < 2: return 0          # safeguard: need at least two elements
    mu = sum(X) /n              # compute the mean value, and then the variance
    return sum([(x-mu)**2 for x in X]) /(n-1)

seed(7)                     # init. pseudo-random number generator
r = 6; n = 10**r            # (logarithm of) number of values
Z = [randrange(0, 2**26) for i in range(n)]
s = sum(Z)                  # exact computation: use integers
q = sum([z*z for z in Z])   # except for one final division
# For a list of integer numbers, both s and q are integer numbers.
# The number n of elements is clearly also an integer number.
# Hence numerator and denominator in the above expression are computed
# as integers. Only the final division yields a floating point number.
X = [float(x) for x in Z]   # turn into floating-point numbers
print('trivial:   %.6f' % var_trivial(X))
print('naive:     %.6f' % var_naive(X))
print('improved1: %.6f' % var_improved1(X))
print('improved2: %.6f' % var_improved2(X))
print('kahan1:    %.6f' % var_kahan1(X))
print('kahan2:    %.6f' % var_kahan2(X))
print('exact:     %.6f' % ((n*q - s*s) / (n*(n-1))))
print(f'{"recursive"}  {mv_recursive(X)[1]}')

