def average(array):
    array = set(array)
    a = sum(array)/len(array)
    return a

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
