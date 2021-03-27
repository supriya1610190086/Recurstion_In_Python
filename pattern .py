def p(n):
    if n==1:
        return 1
    return p(n-1)+1
i=1
while i<=10:
    print(p(i))
    i=i+1