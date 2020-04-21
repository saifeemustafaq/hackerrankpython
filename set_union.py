def main(setA,setB):
    setC = setA.union(setB)
    print(len(setC))

if __name__ == '__main__':
    A = int(input())
    setA = set(map(int,input().split()))
    B = int(input())
    setB = set(map(int,input().split()))
    main(setA,setB)
