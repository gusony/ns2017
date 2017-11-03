from Crypto.PublicKey import RSA
from fractions import gcd
import sys
import base64

pub = []

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y
        
for i in range(0,13):
    pub.append ( RSA.importKey(open('./publicKeys/public{}.pub'.format(i) ).read()))
    
for i in range(1,13):
    for j in range(i+1,13):
        if(gcd(pub[i].n, pub[j].n)!=1):
            common_gcd = gcd(pub[i].n, pub[j].n)
            
            anotherP1 = pub[i].n / common_gcd
            anotherP2 = pub[j].n / common_gcd

            phi1 = (anotherP1-1) *  (common_gcd-1)
            phi2 = (anotherP2-1) *  (common_gcd-1)
            
            d1 = egcd( pub[i].e, phi1)[1] % phi1
            d2 = egcd( pub[j].e, phi2)[1] % phi2
            
            private_key1 = RSA.construct((pub[i].n,pub[i].e,d1))
            private_key2 = RSA.construct((pub[j].n,pub[j].e,d2))
            f = open('./publicKeys/private' + str(i) + '.pem','wb')
            f.write(private_key1.exportKey('PEM'))
            f.close()
            f = open('./publicKeys/private' + str(j) + '.pem','wb')
            f.write(private_key2.exportKey('PEM'))
            f.close()
            
            
            