s = {-12,-1,1,2,4,5,7}
def even(x):
    """Check if a number is even."""
    return x % 2 == 0
even(3)

all(even(x)
     for x in s
     if x > 4)

def odd(x):
    """Check if a number is odd."""
    return x % 2 != 0

all(odd(x)
    for x in s 
    if x > 4)