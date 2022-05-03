'''1 số a có gcd(a,p) = 1 vs p là 1 số nguyên tố lẻ ta có:
    (a/p) đồng dư [a^((p-1)/2) ] mod p
'''

p = 29
for i in range(29):
    j = i*i % p
    if j == 14 or j== 6 or j==11:
        print(j) 
        print(i)
    
# ket qua ra : (i,j) = (6,8) (6,21) 
# ->> 8