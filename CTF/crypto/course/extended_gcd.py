def extended_gcd(a,b):
    xa,ya = 1,0
    xb,yb = 0,1
    while b!=0:
        q = a // b
        r = a % b
        a = b
        b =r
        xr = xa -q * xb
        yr = ya - q * yb
        xa,ya = xb,yb
        xb,yb = xr,yr
    print("xa =: " , xa , " ya=: " , ya)

extended_gcd(32321,26513)