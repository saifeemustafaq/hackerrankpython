A = int(input())
setA = set(map(int,input().split()))
B = int(input())
setB = set(map(int,input().split()))
 
print(len(setA.symmetric_difference(setB)))
