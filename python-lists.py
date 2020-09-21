"""
User Database Query
Mili
Ashley
Chelsey
"""

#users = ['Mili','Ashley','Chelsey']

#print(users)

#users.insert(0, 'Boli')

#print(users)

#users.append('Jr')

#print(users)

#print(users[2])

#users[4] = 'Gera'

#print(users)


#users = ['Mili','Ashley','Chelsey']
#print(users)

#users.remove('Mili')
#print(users)

#popped_user = users.pop()
#print(popped_user)
#print(users)

#del users[0]
#print(users)

#users = ['Mili','Ashley','Chelsey', 'Boli']

#ids = [1, 2, 3, 4]

#mixed_list = [42, 10.3, 'Gomes', users]

#print(mixed_list)

#user_list = mixed_list.pop()

#print(user_list)
#print(mixed_list)

#nested_list = [[123],[234],[345]]

#tags = ['python', 'development', 'tutorials', 'code']

#number_of_tags = len(tags)
#last_item = tags[-1]
#index_of_last_item = tags.index(last_item)

#print(number_of_tags)
#print(last_item)
#print(index_of_last_item)

#tags = ['python', 'development', 'tutorials', 'code']

#print(tags)

#tags.sort()

#print(tags)

#tags.sort(reverse=True)

#print(tags)

#totals = [234, 47, 4, 212]

#print(totals)

#totals.sort(reverse=True)

#print(totals#

#uri = 'https://www.google.com/search?q='
#tags = ['python', 'development', 'tutorial']
#formatted_tags = '+'.join(tags)
#query_uri = f'{uri}{formatted_tags}'

#print(query_uri)

#tags = ['python', 'development', 'tutorials', 'code']

#tag_range = tags[2:3]

#print(tag_range)
"""
tags = [
    'python',
    'development',
    'tutorials', 
    'code',
    'programming',
    'computer science'
]
"""
#tag_range = tags[:-1:2]
#tag_range = tags[::-1]

#print(tag_range)

"""
sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3
]

n_num = [1, 2, 3, 4, 5]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
    
print("Median is: " + str(median))


# Jordan Solution

import math

"""
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
"""
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)
"""

tags = ['hi', 'hello', 'hey', 'bonjour', 'hola']

# no
# tags[-1] = 'programming'

# tags.extend(['programming'])

new_tags = tags + ['ni hao']

print(new_tags)
print(tags)