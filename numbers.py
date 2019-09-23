# A simple first program in python

print('hello world!')

print('this is a basic program to start getting used to vim...')
print('and to git! It is mostly just me playing around.')
print('I will try to use command mode as much as possible, and not rely on scrolling.')

# I'll use comments from now on, because I do not want all of this printing to
# the command line. Now time to make a factorization function.


# Returns true iff m | n

def divides(m, n):
	q = float(n) / float(m)
	if q == round(q):
 		return True
	else:
		return False

# Returns the factors of n

def factorize(n):
	all_factors = []
	for i in range(2, n+1):
		if divides(i, n):
			all_factors.append(i)
	return all_factors

# Returns true iff n is prime

def prime(n):
	return len(factorize(n)) == 1

# Returns the highest k such that m^k | n

def find_order(m, n):
	k = 0
	while divides(m**(k+1), n):
		k += 1
	return k

# Returns the orders of the given factors

def find_orders(f, n):
	ords = []
	for factor in f:
		ords.append(find_order(factor, n))
	return ords

# Returns the prime factorization

def prime_factorize(n):
	facts = factorize(n)
	prime_facts = []
	for f in facts:
		if prime(f):
			prime_facts.append(f)
	pf_orders = find_orders(prime_facts, n)
	return prime_facts, pf_orders

# Prints the prime factorization

def print_prime_factorization(n):
	prime_facts, pf_orders = prime_factorize(n)
	facts_string = ''
	for fact, ord in zip(prime_facts, pf_orders):
		facts_string = facts_string + '(' + str(fact) + '^' + str(ord) + ')'
	return facts_string

# Gives all primes up to (not including) n

def first_n_primes(n):
	all_primes = []
	for i in range(n):
		if prime(i):
			all_primes.append(i)
	return all_primes

# Checks if the number is a perfect square

def is_square(n):
	factors, orders = prime_factorize(n)
	not_square = False
	for order in orders:
		if not divides(2, order):
			not_square = True
	return (not not_square) 

# Gives decompositions of n as a sum of two primes

def Goldbach_decompositions(n):
	candidates = first_n_primes(n)
	decompositions = []
	for i in range(len(candidates)):
		for j in range(i+1,len(candidates)):
			if candidates[i] + candidates[j] == n:
				decompositions.append([candidates[i], candidates[j]])
	return decompositions 

for i in range(101):
	print('Integer: '+str(i))
	print('Factors: '+str(factorize(i)))
	print('Orders:  '+str(find_orders(factorize(i), i)))
	print('Prime?:  '+str(prime(i)))
	print('Prime factorization:')
	print(print_prime_factorization(i))
	print('Is perfect square?')
	print(is_square(i))
	print('Goldbach decompositions:')
	print(Goldbach_decompositions(i))
	print('')

print('Primes up to 100:')
print(first_n_primes(100))

