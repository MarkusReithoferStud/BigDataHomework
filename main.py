def depths(s):
    #remove whitespaces
    s = "".join(s.split())
    ret = []
    balance = 0
    depth = 1
    counter = 0
    if s[0] == ")":
        return None
    s += " "
    #run through all elements and also check the i+1 element for comparison
    for i in range(len(s)-1):
        current_element = s[i]
        next_element = s[i+1]
        if current_element == "(":
            balance += 1
        if current_element == ")":
            balance -= 1
        if current_element == "(" and next_element == "(" and counter < len(s):
            depth += 1
        if balance == 0:
            ret.append(depth)
            depth = 1
        counter += 1
    if balance != 0:
        return None
    return ret

print(depths("(()(())) (( )) ()((()()()))"))
print(depths("()(())() (()(())((()))"))
print(depths("(((((((()))))))) ()(( )) ((( )()()))"))
print(depths(") ( ) ("))
print("-------------------")

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
    #This if check is here to check if the first element of the list is also the minimum element of the list
    #if not, then the list will be split and added together as a list which starts in that way
    if X[0] > min(X):
        lowIndex = X.index(min(X))
        firstList = X[:lowIndex]
        secondList = X[lowIndex:]
        X = secondList + firstList
        #print(X)

    #this part is here to check how many changes the list has e.g 1,2,3,2,1,2,3 woudl have 2 changes
    #1,2,3,4,3,2,1 would have 1 change
    #is the change counter greater than 1, the given sequence is not bitonic
    counter = 0
    pre = X[0]
    # % operator is used to check whether the sequence is declining or ascending
    for i in X:
        if counter % 2 == 0:
            if i < pre:
                counter += 1
                pre = i
            if i >= pre:
                pre = i
        if counter % 2 == 1:
            if i > pre:
                counter += 1
                pre = i
            if i < pre:
                pre = i

    return True if counter <= 1 else False



print(is_bitonic([1,2,3,4,5,6] ))
print(is_bitonic([4,3,2,1,2,3]))
print(is_bitonic([4,3,2,1,2,3,2,1]))
print(is_bitonic([4,2,2,1,3,4,4,5]))
print(is_bitonic([1,2,3,4,0,2]))
