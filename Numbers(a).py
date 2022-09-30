def isPrime(num):
    flag = 0
    for e in range(2,num):
        if (num%e == 0):
            flag = 1
    if flag == 0:
        return True
    else:
        return False
n = int(input("Enter a integer: "))
list1 = [1]
for e in range (2,n+1):
    flag = 0
    if n%e == 0:
        if isPrime(e):
            list1.append(e)
print("The prime factors of "+str(n)+" are "+str(list1))