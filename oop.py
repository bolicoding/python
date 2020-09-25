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

class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total
    
    def __str__(self):
        return 'Invoice from {self.client} for {self.total}'
    
inv = Invoice('Google', 500)
print(str(inv))