def full_string (str):
  if len(str) < 2:
    return ''
  
  return str [0:2] + str[-2:]

print(full_string('flame'))
print(full_string('W'))
print(full_string('xbox'))