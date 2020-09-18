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

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)