import re


def validate_phone_re(number):
    pattern = r'^(02|032|052)?[5-9]\d{4,6}$'
    return bool(re.search(pattern, number))

def matcher(regex, string):
	match = re.search(regex, string)
	if match is None: return string
	start, end = match.span()
	return string[:start] + '(' + string[start:end] + ')' + string[end:]


def main():
	print(matcher('o+', 'Goooooogle'))
	print(matcher('o*', 'Goooooogle'))
	print(matcher('[hH]o+', 'Hohohohohoo'))
	print(matcher('([hH]o)+', 'Hohohohohohooo'))
	print(matcher('([hH]o){2,3}?', 'Hohohohohohooo'))
	print(matcher('day|nice', 'A nice dance-day.'))
	print(matcher('da(y|n)ce', 'A nice dance-day.'))

if __name__ == '__main__':
	main()
