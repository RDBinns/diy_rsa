# Key generation

def isPrime(num):
	for i in range(2,num):
		if (num % i) == 0:
			prime = False
		else:
			prime = True
	return prime

def find_nearest_prime(num):
	while num < 100000:
		if isPrime(num):
			return num
		else:
			num += 1

# let's split the coprime function into smaller functions to simply get factors

def get_factors(num):
	factors = []
	for i in range(2,num):
		if ((num % i) == 0):
			factors.append(i)
	return factors

# this function tests whether two numbers are coprime - i.e. if they have any common factors other than one and themselves.
# seems to be working now, having separately defined the get_factors function

def isCoprime(num1,num2):
	num1_factors = get_factors(num1)
	num2_factors = get_factors(num2)
	if set(num1_factors).isdisjoint(set(num2_factors)):
		# print('no common factors - they coprime!')
		return True
	else:
		# print('there are common factors, not coprime')
		return False

# check through candidate numbers that satisfy the conditions for the private key e. 

def find_e(n,phi_n):
	candidates = []
	for i in range(3,n):
		if isPrime(i):
			if((isCoprime(i,n)) and (isCoprime(i,phi_n))):
				candidates.append(i)
	return candidates

# find d (the private key part 1)
def find_d(prime1,n):
	for i in range(prime1,n):
		if (((i*e) % phi_n) == 1):
			print(i)
			return i

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

# at this point we have a long list of candidates for e. let's let the user select one by entering a random number

choice_e = input("to choose a particular e, pick a random number between 1 and %s: " % len(e))

e = e[int(choice_e)]

# find d

d = find_d(prime1,n)

# let's put those keys into a nice dictionary

# Example keypair:

name = input('Please enter a name for this keypair (e.g. reuben_keypair): ')

public_key = {'e':e, 'n':n}
private_key = {'d':d, 'n':n}

print("Saving key pair %s_.txt to working directory. Put it somewhere safe!" % name)

key_file = open("%s.txt" % name, "w")
key_file.write("%s, %s" % (public_key, private_key))
key_file.close()

# Encryption and decryption

def encrypt(pt):
	print('encrypting message ... ')
	return (pt ** public_key['e']) % public_key['n']

def decrypt(ct):
	return (ct ** private_key['d'] % public_key['n'])