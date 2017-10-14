from Crypto.PublicKey import RSA
from fractions import gcd

prime = []

for i in range(1,12):
    print('----------')
    pub1 = open('public{}.pub'.format(i+1) ).read()
    k1 = RSA.importKey(pub1);
    print(k1.exportKey())
    for j in range(i+1,13):
        pub2 = open('public{}.pub'.format(j) ).read()
        k2 = RSA.importKey(pub2);
        if(gcd(k1.n, k2.n)>1):
            prime.append(str(gcd(k1.n, k2.n)))
            print("k1:"+str(i)+", k2:"+str(j)+" matched!")
for j in range(len(prime)):
    print(prime[j])
    print('---------------------------------------------------------------------------------------------------')

'''
import math
key = []
for i in range(12):
    with open('public{}.txt'.format(i+1)) as f:
        key.append(int(f.read().replace('Modulus=',""), 16))

print('------------------------------------------------')
for i in range(12):
    print(key[i])
    print('------------------------------------------------')

raw_input()

for x in key:
	if not flag:
		break
	for y in key:
		if x==y:
			continue
		g=math.gcd(x,y)
		if g !=1 :
			print(x)
			print(y)
			print(g)
'''

