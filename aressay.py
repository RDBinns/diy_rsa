public_keypair = {'e':5, 'n':14}
private_keypair = {'d':11, 'n':14}

# Key generation

def isPrime(num):
	prime = True
	for i in range(2,num):
		if (num % i) == 0:
			prime = False
	return prime

def find_nearest_prime(num):
	while num < 100000:
		if isPrime(num):
			return num
		else:
			num += 1

# this function tests whether two numbers are coprime - i.e. if they have any common factors other than one and themselves.

def check_coprime(num1,num2):
	are_coprime = False
	num1_factors = []
	for i in range(3,num1):
		if ((num1 % i) == 0):
			num1_factors.append(i)
	# print(num1_factors)
	num2_factors = []
	for i in range(3,num2):
		if ((num2 % i) == 0):
			num2_factors.append(i)	
	# print(num2_factors)
	if set(num1_factors).isdisjoint(set(num2_factors)):
		# print('no common factors - they coprime!')
		are_coprime = True
	else:
		# print('there are common factors, not coprime')
		are_coprime = False
	return are_coprime

# check through candidate numbers that satisfy the conditions for the private key e. 
# Order matters! (num1 = n, num2 = Φ(N))

def find_e(n,phi_n):
	candidates = []
	for i in range(2,n):
		if isPrime(i):
			if((check_coprime(i,n)) and (check_coprime(i,phi_n))):
				candidates.append(i)
	return candidates

# find d (the secret key part 1)
def find_d(prime1,n):
	for i in range(prime1,n):
		if ((i*e) == (phi_n % 1)):
			return d

# pick two large prime numbers:

# ==== first prime number

print("let's generate the first of two prime numbers.")

user_entropy = input("please generate some entropy by typing lots of random characters: ")
entropy = 0
for letter in user_entropy:
	entropy = entropy + ord(letter)

print(entropy)

# use entropy value to select a prime number

prime1 = find_nearest_prime(entropy)
print("the first prime number is: %s" % prime1)

# ===== second prime number

print("let's generate the second of two prime numbers.")

user_entropy = input("please generate some entropy by typing lots of random characters: ")
entropy = 0
for letter in user_entropy:
	entropy = entropy + ord(letter)

print(entropy)

# use entropy value to select a prime number

prime2 = find_nearest_prime(entropy)
print("the second prime number is: %s" % prime2)


# ==== generate N (second part of public and private keypairs)

n = prime1*prime2

print("N will be %s" % n)

# calculate Φ(N) = (p-1) (q-1)

phi_n = ((prime1-1)*(prime2-1))

# choose E

print("Searching for e ... please wait")

e = find_e(n,phi_n)


# find d

d_candidates = []




# # Encryption and decryption

# def encrypt(pt):
# 	return (pt ** public_keypair['e']) % public_keypair['n']

# def decrypt(ct):
# 	return (ct ** private_keypair['d'] % public_keypair['n'])

# # def encrypt_message(message):
# # 	cyphertext = []
# # 	for i in message:
# # 		cyphertext.append(encrypt(ord(i)))
# # 	return cyphertext

# # def decrypt_message(cyphertext):
# # 	decrypted_plaintext = ''
# # 	for i in cyphertext:
# # 		decrypted_plaintext = decrypted_plaintext + chr(decrypt(i))
# # 	return decrypted_plaintext

# user_message = input("what is your secret message?: ")

# print('encrypting message ....')

# cyphertext = encrypt(int(user_message))

