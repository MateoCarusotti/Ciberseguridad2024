import libnum

p = 1153324775179431312178120797679

q = 1259358348907893108175391571521

e = 65537

c = 1280743944712857143060627969938538851911171950125979945026152

n = p * q
phi_n = (p - 1) * (q - 1)

d = libnum.invmod(e, phi_n)


M = pow(c, d, n)

M = libnum.n2s(M)

print(f'Mensaje descifrado: {M}')
