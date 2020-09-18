#calculation = 8 + 2 * 5 - (9+2) ** 2

#print(calculation)
from functools import reduce

def manual_exponent(base_num, pow_num):
    result = 1
    for num in range(pow_num):
        result = result * base_num
    return result

print(manual_exponent(2, 3))