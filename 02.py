import pandas as pd

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


read_csv()
