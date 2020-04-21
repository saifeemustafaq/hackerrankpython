def main(arr,setA,setB):
    count = 0
     
    for x in arr:
        if x in setA:
            count = count+1
    for x in arr:
        if x in setB:
            count = count-1
    print(count)


if __name__ == '__main__':
    n = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    setA = {int(x) for x in input().split()}
    setB = {int(x) for x in input().split()}
    main(arr,setA,setB)
