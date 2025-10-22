def distance(a,b):
    # return and calculate the distance formula
    a = tuple(a)
    b = tuple(b)


    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


print (distance((1,2),(4,6)))

