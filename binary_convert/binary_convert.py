

# Input a number and the algorithm convert this number to binary presentation
def binary_convert(number):
    result = []
    while number > 0:
        result.append(number % 2)
        number = int(number / 2)

    result.reverse()
    return result

# Test binary convert
n = 1020
binary = binary_convert(n)
print(binary)
