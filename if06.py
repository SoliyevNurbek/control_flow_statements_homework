def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    k=0
    k1=0
    if a<0:
        k=k+1
    else:
        k1=k1+1
    if b<0:
        k=k+1
    else:
        k1=k1+1
    if c<0:
        k=k+1
    else:
        k1=k1+1
    return str(k1)+" " +str(k)
print(main(-1,5,-8))