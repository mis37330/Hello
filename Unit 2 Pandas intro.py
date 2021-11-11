import pandas as pd
from pandas import Series, DataFrame
my_obj = pd.Series([2, 5, 8, 3, 1, 0], name='MY FIRST PANDA OBJECT!!')
data = {'student':['Jane', 'Delilah', 'Kyle', 'Sam', 'Elaine', 'Arthur', 'Thomas'], 'grade':[107, 56, 76, 85, 99, 100, 98], 'age':[13, 13, 13, 13, 13, 14, 13]}
df = pd.DataFrame(data)


df2 = pd.DataFrame(data, columns=['grade', 'age', 'student'])
    

df2['height'] = pd.Series([70, 71, 72], index = [1, 4, 6])

A = df2.grade >= 90

A

df2.loc[df2.grade <90]

df2.loc[df2.student == 'Arthur', 'grade'] = 30

df2
