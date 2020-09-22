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

positions = ['cb', 'lb', 'st', 'lw']
players = ['Silva', 'Chilwell', 'Werner', 'Pulisic']

scoreboard = zip(positions, players)

print(list(scoreboard))