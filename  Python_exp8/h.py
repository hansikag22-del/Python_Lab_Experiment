"""
arr=[]
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(3)
print(set(arr))


arr=set()
arr.add(1)
arr.append(1)
arr.remove()
"""
n=int(input("Enter a number: "))
for i in range (n):
    print("*" * (i+1))

n=int(input("Enter a number: "))
for i in range(1,n+1):
    print("*" * i)