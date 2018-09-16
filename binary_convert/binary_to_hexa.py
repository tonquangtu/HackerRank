# Convert binary number (passed as a string) and output expectation also as a string present hexa of this input
def get_bi_from_string(bi_s):
    bi = []
    for i in range(len(bi_s)):
        if bi_s[i] == '0':
            bi.append(0)
        else:
            bi.append(1)
    return bi


def bi_to_hexa(bi_s):
    if len(bi_s) < 1:
        return ''

    bi = get_bi_from_string(bi_s)
    hexa = ''
    for i in range(len(bi) - 1, -1, -4):
        number = bi[i]
        if i > 0:
            number += bi[i - 1] * 2
        if i > 1:
            number += bi[i - 2] * 2**2
        if i > 2:
            number += bi[i - 3] * 2**3
        hexa += get_hexa(number)

    return hexa[::-1]


def get_hexa(number):
    if 10 > number >= 0:
        return str(number)
    elif number == 10:
        return 'A'
    elif number == 11:
        return 'B'
    elif number == 12:
        return 'C'
    elif number == 13:
        return 'D'
    elif number == 14:
        return 'E'
    elif number == 15:
        return 'F'


def get_number_form_hexa(c):
    if c == 'F':
        return 15
    elif c == 'E':
        return 14
    elif c == 'D':
        return 13
    elif c == 'C':
        return 12
    elif c == 'B':
        return 11
    elif c == 'A':
        return 10
    else:
        return int(c)


#  Convert number to binary (the result will present by 4 binary character)
#  Number < 16
def number_to_bi_in_hex_format(number):
    bi = ''
    while number > 0:
        bi += str(number % 2)
        number = int(number / 2)

    num_zero_add = 4 - len(bi)
    for i in range(num_zero_add):
        bi += '0'

    return bi[::-1]


# Convert hexa to binary
def hexa_to_bi(hexa_s):
    if len(hexa_s) < 1:
        return ''
    bi = ''
    for i in range(len(hexa_s)):
        number = get_number_form_hexa(hexa_s[i])
        bi += number_to_bi_in_hex_format(number)

    return bi


# Test
bi_str = '11101010110010'
hexa_str = '3AB2'
hex_s = bi_to_hexa(bi_str)
bi_s = hexa_to_bi(hexa_str)
# print(hex_s)
print(bi_s)
