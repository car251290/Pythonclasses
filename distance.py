def distance(a,b):
    # return and calculate the distance formula
    a = tuple(a)
    b = tuple(b)


    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


print (distance((1,2),(4,6)))

def test_distance():
    assert distance((0,0),(3,4)) == 5.0
    assert distance((1,1),(4,5)) == 5.0
    assert distance((-1,-1),(2,3)) == 5.0
    assert distance((2,3),(2,3)) == 0.0
    assert distance((0,0),(0,0)) == 0.0
    assert distance((1.5,2.5),(4.5,6.5)) == 5.0

test_distance()