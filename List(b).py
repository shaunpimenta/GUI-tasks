n = int(input("Enter the number of words: "))
print("Now enter the list of words: ")
list1 = []
for e in range(n):
    list1.append(input())
max = 0
word = list1[max]
for e in list1:
    if len(e)>max:
        max = len(e)
        word = e
print("Length of the largest word: "+word+" is "+str(max))