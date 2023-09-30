def main(a,b,c):
    """
    Find number of negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    k=0
    if a<0:
        k=k+1
    if b<0:
        k=k+1
    if c<0:
        k=k+1
    return k
print(main(-1,-2,-8))