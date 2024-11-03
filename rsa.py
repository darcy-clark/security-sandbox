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
p = 41
q = 61

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

cipher = m**e % (p * q)

print('Cipher: ' + str(cipher))

d = eea(sigma, e)
if d < 0:
    d = d + sigma

print('Computed d: ' + str(d))

retrieved = cipher**d % (p * q)
print('Retrieved message: ' + str(retrieved))
