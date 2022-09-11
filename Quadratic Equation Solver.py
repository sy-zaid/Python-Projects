def quadratic(a,b,c):
    import math
    res1 = (-1*b + math.sqrt((b**2)-4*a*c))/2*a
    res2 = (-1*b - math.sqrt((b**2)-4*a*c))/2*a
    print('Either',res1,'or,',res2)

quadratic(1,3,1)
