def is_narcissistic(number, base=10):
    result = 0
    count_digits = 0
    for i in number:
        count_digits += 1
    for i in number:
        if i.isdigit():
            result += int(i)**count_digits
        else:
            result += (ord(i) - 55)**count_digits
    return result == int(number, base)
    
def main():
    print(is_narcissistic('0'))
    print(is_narcissistic('10'))
    print(is_narcissistic('223', 4))
    print(is_narcissistic('115132219018763992565095597973971522401'))
if __name__ == '__main__':
    main()