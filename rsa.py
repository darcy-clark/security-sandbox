print('Hello World!')

message = input('Enter message: ')
m = 0

iteration = 0
for char in message:
    print('ASCII for "' + char + '": ' + str(ord(char)))
    if iteration > 0:
        m = 256**iteration + ord(char)
    else:
        m = ord(char)
    iteration = iteration + 1

print('m=' + str(m))

p = 11
q = 13

print('Using p=' + str(p) + ' and q=' + str(q))

sigma_num = (p - 1)*(q - 1)

b = p - 1
a = q - 1

while b != 0:
    temp = b
    b = a % b
    a = temp

print('GCD is ' + str(a))

sigma = sigma_num // a

print('Sigma is ' + str(sigma))

e = 7

cipher = m**e % (p * q)

print('Cipher is: ' + str(cipher))

d = 43 # temporarily hardcoded until I get the EEA

retrieved = cipher**d % (p * q)
print('Retrieved message is: ' + str(retrieved))
