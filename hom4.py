import re


# class PrivacyFilter():
#	def __init__(self, text):
#		self.text = text

# 	preserve_phone_country_code = False
# 	preserve_email_hostname = False
# 	partially_preserve_email_username = False

# 	def filtered(self):
#		for word in self.text:
#			if is_email(word):
#				re.sub(word, '[EMAIL]', self.text)
#			elif is_phone(word):
# 				re.sub(word, '[PHONE]', self.text)
#		
#		if preserve_phone_country_code:
#			?re.sub('', '[FILTERED]', )
#		if partially_preseve_email_username:
#			preserve_email_hostaname = True
#		re.sub()



# class Validations():
# 	def is_email(value):


# 	def is_phone(value):
# 		valid_local_phone = r'^(0)?[1-9]\d{6,11}'
# 		valid_international_phone = r'^(\b00\b|+)\d{1,3}\d{6,11}'
# 		return bool(re.search(valid_local_phone, value))
			  #and bool(re.search(valid_international_phone, value))

# 	def is_hostname(value):

# 	def is_ip_address(value):

	def is_number(value):
		valid_number = r'^-?(0|([1-9]([(\.,])?\d+))'
		match = re.search(valid_number, value)
		if match is None:
			return False
		start, end = match.span()
		return value[start:end] == value

	def is_integer(value):
		valid_integer = r'^-?(0|([1-9]\d+))'
		match = re.search(valid_integer, value)
		if match is None:
			return False
		start, end = match.span()
		return value[start:end] == value

	def is_ip_address(value):
		valid_ip = r'\b(25[0-5]|2[0-4][0-9]|[01]?\[0-9][0-9]?)\.(25[0-5]|\
			2[0-4][0-9]|[01]?\[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|\
			[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
		return bool(re.search(valid_ip, value))

# 	def is_date(value):

# 	def is_time(value):

# 	def is_datetime(value):

#?
#0,...XXX
# def is_number(value):
# 	valid_number = r'^-?(0|([1-9]([(\.,])?\d+))'
# 	match = re.search(valid_number, value)
# 	if match is None:
# 		return False
# 	start, end = match.span()
# 	return value[start:end] == value

# def is_integer(value):
# 	valid_integer = r'^-?(0|([1-9]\d+))'
# 	match = re.search(valid_integer, value)
# 	if match is None:
# 		return False
# 	start, end = match.span()
# 	return value[start:end] == value

# def is_ip_address(value):
# 	valid_ip = r'\b(25[0-5]|2[0-4][0-9]|[01]?\[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?\[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
# 	return bool(re.search(valid_ip, value))

# 	#return re.match(r'(([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$', value) != None

# def is_date(value):
# 	valid_date = r'\d{4}-?[1,12]{2}-?[1,31]{2}'
# 	return bool(re.search(valid_date, value))



# def is_email(value):
# 	valid_email = r'\w?(\w_+.-)\d{0,200}   '
# 	return bool(re.search(valid_email, value))
# def is_hostname(value):
# 	valid_hostname = r''
# 	return bool(re.search(valid_hostname, value))
# def is_phone(value):
# 	valid_local_phone = r'^(0)?[1-9]\d{6,11}  [^-()]'
# 	valid_international_phone = r'^(\b00\b|+)\d{1,3}\d{6,11}'
# 	return bool(re.search(valid_local_phone, value))
# 			  #and bool(re.search(valid_international_phone, value))


#re.sub('ROAD$', 'RD.', s) ;  re.sub(r'\bROAD\b', 'RD.', s)
