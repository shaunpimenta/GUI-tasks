import pandas as pd
data = {'Name':['Tom1','nick1','krish1','jack1'], 'Age':[20,21,19,18]}

#create DataFrame
df = pd.DataFrame(data)
data1 = {'Name':['Tom1','nick1','krish1','jack1'], 'Age':[20,21,19,18]}
df1 = pd.DataFrame(data1)

frames = [df1,df]
#concat
result = pd.concat(frames)
print(result)

result = pd.concat([df1,df], axis = 1, join = 'inner')
print(result)

df1.merge(df, how = 'left', on = 'Name')