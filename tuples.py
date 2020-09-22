"""
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post)
print(post[-1])
print(post[-1][1])


post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])
"""
#post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

#post = post[:-1]

#post = post[1:]

#post = list(post)
#post.remove('published')
#post = tuple(post)

#print(post)

"""
priority_index = {
    (1, 'premier'): [1, 34, 12],
    (1, 'mvp'): [84, 22, 24],
    (2, 'standard'): [93, 81, 3]
}

print(list(priority_index.keys()))
"""

#positions = ['cb', 'lb', 'st', 'lw']
#players = ['Silva', 'Chilwell', 'Werner', 'Pulisic']

#scoreboard = zip(positions, players)

#print(list(scoreboard))

"""
tags = {
    'cb',
    'lw',
    'st',
    'lw'
}

#print(tags)

query_one = 'cb' in tags
query_two = 'rb' in tags
print(query_one)
"""

"""
tags_one = {
    'python',
    'coding',
    'tutor',
    'coding'
}

tags_two = {
    'ruby',
    'coding',
    'tutor',
    'development'
}
"""

#merged_tags = tags_one | tags_two

#print(merged_tags)

#exclusive_to_tag_one = tags_one - tags_two
#print(exclusive_to_tag_one)


#exclusive_to_tag_two = tags_two - tags_one
#print(exclusive_to_tag_two)

#universal_tags = tags_one & tags_two
#print(universal_tags)

