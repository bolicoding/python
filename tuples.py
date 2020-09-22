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
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

#post = post[:-1]

#post = post[1:]

post = list(post)
post.remove('published')
post = tuple(post)

print(post)