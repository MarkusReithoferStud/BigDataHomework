def mv_recursive(X, lft=0, rgt=None):
    if rgt is None:
        rgt = len(X)    # if no right border, get length
    n = rgt - lft                # n is the length of a part right - left
    if n <= 1:  #if list contains only one element, return element as mean and var = 0
        return X[lft], 0

    if n <= 2:                  # solve for 2 elements when recursion hits n <=2
        leftEle = X[lft]
        rightEle = X[rgt-1]
        meanEle = (leftEle+rightEle)/n
        sumSqEle = (leftEle-rightEle)**2/n
        return meanEle, sumSqEle

    midEle = (lft + rgt) // 2   # compute index of middle element
    meanLeft, sl = mv_recursive(X, lft, midEle)   # recursive call function for left part ml = meanEle sl = sumSqEle
    meanRigth, sr = mv_recursive(X, midEle, rgt)   # recursive call function for right part ml = meanEle sl = sumSqEle
    nleft = midEle - lft    # count of elements between lft and midEle
    nright = rgt - midEle    # count of elements between midEle and rgt
    #calc mean
    mu = (nleft/n) * meanLeft + (nright/n) * meanRigth   # mu = mean of both parts, weighted by nleft/nright proportion
    #calc sigma
    sigma = ((nleft-1)/(n-1))*sl + ((nright-1)/(n-1))*sr + (nleft/n)*(nright/(n-1)) * (meanLeft-meanRigth)**2
    return mu, sigma

print(mv_recursive([1,2,3,4]))
