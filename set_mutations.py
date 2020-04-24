A = int(input())
setA = set(map(int,input().split()))
n = int(input())

for x in range(n):
    temp = [y for y in input().split()]
    temp_set = set(map(int,input().split()))

    if temp[0] == 'intersection_update':
        setA.intersection_update(temp_set)
        #print(setA)
        
    elif temp[0] == 'update':
        setA.update(temp_set)
        #print(setA)
        
    elif temp[0] == 'symmetric_difference_update':
        setA.symmetric_difference_update(temp_set)
        #print(setA)
        
    elif temp[0] == 'difference_update':
        setA.difference_update(temp_set)
        #print(setA)


print(sum(setA))
