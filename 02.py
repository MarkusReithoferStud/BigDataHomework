import pandas as pd
import math

def read_csv():
    df = pd.read_csv("wine.tsv", delimiter="\t")
    #print(df.head())
    #df1 = the dataset from colum 1-13, so without the last column which contains letters#
    df1 = df.iloc[:, 0:13]
    mean = df1.mean()
    std = df1.std()
    #print(mean)
    df_stats = pd.concat([mean, std], axis=1)
    df_stats.columns = ['mean', 'std']
    print(df_stats)

    df2 = df.iloc[: , 13:14]
    #print(df2)
    test = df2['class'].value_counts().rename_axis('class').reset_index(name='frq')
    #print(test)
    c = test.sort_values(by='class')
    print(c)

## RENAME ABOVE CODE AND FINETUNE OUTCOME


def rowRead():
    #data collection
    with open('wine.tsv', 'r') as data:
        header = data.readline().strip().split('\t')
        squareList = ([0] * (len(header)-1))
        t = ([0] * (len(header)-1))
        t.append([0,0,0])
        #print(t)
        rowcount = 0
        for row in data:
            line = row.strip().split('\t')
            counter = 0
            rowcount += 1
            for i in line:
                try:
                    t[counter] += float(i)
                    squareList[counter] += float(i)*float(i)
                    counter += 1
                    #print(t)
                except:
                    if i == 'A':
                        t[-1][0] += 1
                    if i == 'B':
                        t[-1][1] += 1
                    if i == 'C':
                        t[-1][2] += 1


        index = 0
        #caclculation
        print("column".ljust(10), "mean".rjust(10), "std".rjust(10))
        for i in t:
            try:
                columnHeader = header[index]
                meanHeader = str(round(t[index] / rowcount, 4))
                secondpart = t[index]/rowcount * t[index]/rowcount
                firstpart= squareList[index]/rowcount
                stdev = str(round(math.sqrt(firstpart-secondpart),4 ))
                print(columnHeader.ljust(10), meanHeader.rjust(10), stdev.rjust(10))
                index +=1
            except:

                print('\n'"class".ljust(10), "frq".rjust(0))
                print("A", str(i[0]).rjust(11))
                print("B", str(i[1]).rjust(11))
                print("C", str(i[2]).rjust(11))


rowRead()
#https://stackoverflow.com/questions/1174984/how-to-efficiently-calculate-a-running-standard-deviation
