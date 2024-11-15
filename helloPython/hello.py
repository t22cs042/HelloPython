import math
print("Hello, Python world!")

"""
a = 10
b = 0.00000001
c = 'string'
print(a,b,c)
for x in {1,2,3,5}:
    print(x)

if 0 < x < 10:
    print('0<x<10')
else:
    print('p = ', p)
    p += 1
    
p=0
while p<10:
    print('p = ',p)
    p += 1
    
n = 10
for i in range(n):
    
    print(i)
    i+=1
    
print(math.pi)

def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(20))
    """
    
def quick_sort(data):
    
    if len(data) <= 1:
        return data
    
    pivot = data.pop(0)
    
    left = [i for i in data if i <= pivot]
    right = [i for i in data if i > pivot]
    
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right

DATA = [6, 15, 4, 2, 8, 5,11, 9, 7, 13 ]
print (quick_sort(DATA))
print (quick_sort(DATA))
print (quick_sort(DATA))
print (quick_sort(DATA))
print (quick_sort(DATA))
print (quick_sort(DATA))
#github
#print(f"{DATA} → {quick_sort(DATA)}")
    
    