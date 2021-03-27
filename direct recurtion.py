def demo(number):
    if number==1:
        return 1
    return 2*demo(number-1)
i=1
while i<10:
    print(demo(i))
    i=i+1