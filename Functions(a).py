import random
len_dict = int(input("Enter the number of elements in dictionary: "))
n = int(input("Enter the max number: "))
dict1 = {}
for e in range(len_dict):
    key = random.randint(1,n)
    if key in dict1:
        key = random.randint(1,n)
    #print(e,key)
    dict1[key] = key*key
print(dict1)