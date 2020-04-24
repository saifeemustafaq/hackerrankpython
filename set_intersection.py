A = int(input())
setA = set(map(int,input().split()))
B = int(input())
setB = set(map(int,input().split()))

count = len(setA.intersection(setB))

print(count)
