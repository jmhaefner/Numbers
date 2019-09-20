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

def order(m, n):
	k = 0
	while divides(m**(k+1), n):
		k += 1
	return k

# Returns the orders of the given factors

def orders(f, n):
	ords = []
	for factor in f:
		ords.append(order(factor, n))
	return ords

# Returns the prime factorization

def prime_factorize(n):
	facts = factorize(n)
	prime_facts = []
	for f in facts:
		if prime(f):
			prime_facts.append(f)
	pf_orders = orders(prime_facts, n)
	return prime_facts, pf_orders

# Prints the prime factorization

def print_prime_factorization(n):
	prime_facts, pf_orders = prime_factorize(n)
	facts_string = ''
	for fact, ord in zip(prime_facts, pf_orders):
		facts_string = facts_string + '(' + str(fact) + '^' + str(ord) + ')'
	return facts_string


for i in range(101):
	print('Integer: '+str(i))
	print('Factors: '+str(factorize(i)))
	print('Orders:  '+str(orders(factorize(i), i)))
	print('Prime?:  '+str(prime(i)))
	print('Prime factorization:')
	print(print_prime_factorization(i))
	print('')
