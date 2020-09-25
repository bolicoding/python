"""
class InfiniteLineup:
    def __init__(self, players):
        self.players = players

    def lineup(self):
        lineup_max = len(self.players)
        idx = 0

        while True:
            if idx < lineup_max:
                yield self.players[idx]
            else:
                idx = 0
                yield self.players[idx]

            idx += 1

    def __repr__(self):
        return f'InfiniteLineup({self.players})'

    def __str__(self):
        return f"InfiniteLineup with the players: {', '.join(self.players)}"


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros)
astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(full_lineup))

print(str(full_lineup))
"""
"""
class Website:
    def __init__(self, title):
        self.title = title
        
ws = Website('My Website Title')
print(ws.__dict__)

ws_two = Website('Second Title')
print(ws_two.__dict__)
"""
"""
class User:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        
    def greeting(self):
        return f'Hi {self.first_name} {self.last_name}'
    
class AdminUser(User):
    def active_users(self):
        return '500'
    
ashley = AdminUser('ashley@devcamp.com', 'Ashley', 'Orozco')

chelsey = User('chels@devcamp.com', 'Chelsey', 'Orozco')

print(ashley.active_users())
print(ashley.greeting())
"""

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):             
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'


class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [Div('Some content'),
        Heading('My Amazing Heading'),
        Div('Another div')
        ]

for tag in tags:
  print(str(tag) + ': ' + tag.render())