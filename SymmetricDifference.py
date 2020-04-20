def sym(b,d):
    z = sorted(b^d)
    print(*z, sep = '\n')

if __name__=='__main__':
    a = int(input())
    b = {int(x) for x in input().split()}
    c = int(input())
    d = {int(x) for x in input().split()}
    sym(b,d)

