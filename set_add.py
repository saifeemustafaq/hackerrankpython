def main(number):
    num = number
    tot = set()
    for x in range(num):
        temp = input()
        tot.add(temp)
     
    return len(tot)


if __name__ == '__main__':
    n = int(input())
    print(main(n))
