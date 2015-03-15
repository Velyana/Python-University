def find_digits(number):
	l = []
	number_string = str(number)
	for ch in number_string:
		l.append(int(ch))
	return l

def is_happy(number):
	new_number = 0	
	visited = []	
	while new_number != 1 or not(new_number in visited):
		new_number = 0
		for i in find_digits(number):
			new_number += i**2	
		if new_number == 1:
			return True
		elif new_number in visited:
			return False
		else:
			visited.append(new_number)
			number = new_number
			
def is_prime(number):
	if number < 2:
		return False
	for i in range(2, number):
		if number%i == 0:
			return False
	return True

def happy_primes(iterable):
	happy_prime_list = []
	for number in iterable:
		if is_happy(number) and is_prime(number):
			happy_prime_list.append(number)
	return happy_prime_list


