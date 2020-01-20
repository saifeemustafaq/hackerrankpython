n = 20
b = 0
c = 0

for x in range(3,20):
    if(x%3==0 and x<20):
        b = b+x
    if(x%5==0 and x<20):
        c = c+x
d = c+b
print(d)
