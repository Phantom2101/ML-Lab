import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=[1,2,3,4,5,]
print(type(a))
b=(1,'Affan',3200,32.00)
print(type(b))
c={1,'mango',2,52}
print(type(c))
d={'name':'Affan','marks':8.92}
print(type(d))
arr=np.array([1,2,3,4])
print(arr+2)
arr1=np.array([1,2,3,4])
arr2=np.array([48,99,87,666])
print(arr1+arr2)
print(arr[0:4])

s=pd.Series([1,2,3,4,5])
print(s)
data = {'A':[1,2,3],'B':[4,5,6]}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print(df['A'])

print(df[df['A']>1])

df['C'] = df['A']+df['B']
print(df['C'])

df=pd.DataFrame({'A':['foo','bar','foo'],'B':[1,2,3]})
grouped = df.groupby('A').sum()
print(grouped)
df.pivot_table(values='B',index='A',aggfunc='sum')
df=pd.DataFrame({'A':[1,2,None],'B':[4,None,6]})
print(df)
print(df.isnull())
df.fillna(0,inplace=True)
df.dropna(inplace=True)
df = pd.read_csv('C:\\Users\\HP\\Desktop\\python pgms\\Python codes\\Lab work\\data.csv')

df.to_csv('data',index=False)
print(df)

xpoints=np.array([0,6])
ypoints=np.array([0,10])
plt.plot(xpoints,ypoints)
plt.show()