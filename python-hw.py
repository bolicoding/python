def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum((1, 2, 3)))
    
def character_change(str):
    char = str[0]
    str = str.replace(char, '$')
    str = char + str[1:]
    
    return str
print(character_change('restart'))