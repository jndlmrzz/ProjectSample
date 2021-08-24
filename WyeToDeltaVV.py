def parallelAdd(*args):
    sum = 0
    for arg in args:
        sum += 1/arg
    return 1/sum
def deltaToWye(ra, rb, rc):
    deltaToWye(15, 10, 25)
    denominator = ra + rb + rc
    r1  = (rb * rc) / denominator
    r2  = (rc * ra) / denominator
    r3  = (ra * rb) / denominator
    
    return [r1, r2, r3]
# Sample Git
# Sample Git but outside local

def wyeToDelta(r1, r2, r3):
    numerator = (r1 * r2) + (r2 * r3) + (r3 * r1)
    ra = numerator / r1
    rb = numerator / r2
    rc = numerator / r3
    
    return [ra, rb, rc]
