"""
class Invoice:
    
    def greeting(self):
        return 'Hi there'
    
    
inv_one = Invoice()
print(inv_one.greeting())

inv_two = Invoice()
print(inv_two.greeting())
"""

"""
class Invoice:
    
    def __init__(self, client, total):
        self.client = client 
        self.total = total
        
    def formatter(self):
        return f'{self.client} owes: ${self.total}'
    
    
google = Invoice('Google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())
"""
"""
class Invoice:
    
    def __init__(self, client, total):
        self.client = client 
        self.total = total
        
    def formatter(self):
        return f'{self.client} owes: ${self.total}'
    
    
google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)
"""
"""
class Invoice:
    
    def __init__(self, client, total):
        self._client = client 
        self._total = total
        
    def formatter(self):
        return f'{self._client} owes: ${self._total}'
    
    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client):
        self._client = client
    
    @property
    def total(self):
        return self._total 
       
google = Invoice('Google', 100)
print(google.client)

google.client = 'Yahoo'

print(google.client)
"""
"""
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def __str__(self):
        return 'Invoice from {self.client} for {self.total}'
    
inv = Invoice('Google', 500)
print(str(inv))
"""
"""
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def __str__(self):
        return 'Invoice from {self.client} for {self.total}'
    
    def __repr__(self):
        return f'Invoice <value: client: {self,client}, total: {self.total}>'
    
inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))
"""

class Lineup:
    def __init__(self, players):
        self.players = players
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < (len(self.players) - 1):
            player = self.players[self.n]
            self.n += 1
            return player
        elif self.n == (len(self.players) - 1):
            player = self.players[self.n]
            self.n = 0
            return player
chelsea = [
    'Havertz',
    'Werner',
    'Chilwell',
    'Mount',
    'Zouma',
    'Silva',
    'Pulisic',
    'James',
    'Ziyech'
]

chelsea_lineup = Lineup(chelsea)
process = iter(chelsea_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
