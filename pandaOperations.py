import pandas as pd
dict1 = {"name": ['mansi', 'mj', 'abc', 'aceeg'],
         "marks": [100,99,47,57]}
df = pd.DataFrame(dict1)
# print(df)

df.to_csv('data.csv', index=False) #make an excel file with our data and index show nahi krega
xy= pd.read_csv('data.csv')
# print(xy)

l=xy['marks'][0]= 40
print(l)
print(xy)
