def main(number,arr,loop):
    num = number
    ar = set(arr)
    command = loop
    #print(ar)
    

    for x in range(command):
        temp = [x for x in input().split()]
        if temp[0] == 'pop':
            ar.pop()
        if temp[0] == 'remove':
            #print(temp[1])
            r = int(temp[1])
            #print(r)
            ar.remove(r)
        if temp[0] == 'discard':
            r = int(temp[1])
            ar.discard(r)
    return sum(ar)


if __name__ == '__main__':
    n = int(input())
    m = set(map(int,input().split()))
    o = int(input())
    print(main(n,m,o))
