def rotLeft(a, d):
    # Write your code here
    n = len(a)
    d = d % n  # In case d is greater than n
    return a[d:] + a[:d]
rotLeft([1, 2, 3, 4, 5], 2)
print(rotLeft([1, 2, 3, 4, 5], 2))

def rotRight(a, d):
    n = len(a)
    d = d % n  # In case d is greater than n
    return a[-d:] + a[:-d]
rotRight([1, 2, 3, 4, 5], 2)
print(rotRight([1, 2, 3, 4, 5], 2))

