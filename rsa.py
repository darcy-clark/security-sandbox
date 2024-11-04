def eea(sigma, e):
    r_prev = sigma
    r_curr = e

    s_prev = 1
    s_curr = 0

    t_prev = 0
    t_curr = 1

    q = 0
    while r_curr != 0:
        q = r_prev // r_curr

        temp = r_curr
        r_curr = r_prev - (q * r_curr)
        r_prev = temp

        temp = s_curr
        s_curr = s_prev - (q * s_curr)
        s_prev = temp

        temp = t_curr
        t_curr = t_prev - (q * t_curr)
        t_prev = temp

    return t_prev

# Equivalent to pow() with the modulo argument. I just wanted to implement it myself to get a hang of modular math again
def l2r_binary(b, e, m):
    e_str = str(bin(e))
    e_str = e_str[2:]
    e_str = e_str[::-1] # Reverse string so we can start at LSB

    result = 1
    b_inter = b % m
    i = 0
    for char in e_str:
        current = int(char)
        if current == 1:
            result = (result * b_inter) % m
        b_inter = b_inter**2 % m
        i = i + 1

    return result

message = input('Enter message: ')
m = 0

iteration = 0
for char in message:
    print('ASCII for "' + char + '": ' + str(ord(char)))
    m = m + ((256**iteration) * ord(char))
    iteration = iteration + 1

print('m=' + str(m))

# Size of our n value (p*q) limits the possible size of our message. n must be larger than m, otherwise
# the lowest congruent value will not be our original message
p = 7907
q = 7919

print('Using p=' + str(p) + ' and q=' + str(q))
print('n: ' + str(p * q))

sigma_num = (p - 1)*(q - 1)

b = p - 1
a = q - 1

while b != 0:
    temp = b
    b = a % b
    a = temp

print('GCD: ' + str(a))

sigma = sigma_num // a

print('Sigma: ' + str(sigma))

e = 7
d = eea(sigma, e)
if d < 0:
    d = d + sigma
print('Computed d: ' + str(d))

# pow() with the modulo argument works perfectly here, but I wanted to implement the modular exponentiation method
cipher = l2r_binary(m, e, p * q)
print('Cipher: ' + str(cipher))
retrieved = l2r_binary(cipher, d, p * q)
print('Retrieved message: ' + str(retrieved))
