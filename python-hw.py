"""
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
"""

"""
phonebook = {
    'Juan': '808-555-5555',
    'Ash': '801-333-3333',
    'Chels': '385-444-4444'
}

 #phonebook['Mili'] = '801-222-2222'

#phonebook['Juan'] = '801-555-5555'
# grab_contact = phonebook.get('Ash', 'Number not available')

del phonebook['Juan']

print(phonebook)
"""


"""
users = [
   {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
]

print(users)
"""

#user = {
 # 'username': 'boli',
  #'email': 'b@gmail.com',
  #'phone': '555-555-5555'
#}

#for key, value in user.items():
 #print('Key =>', key)
 #print('Value =>', value)
  
#for key in user.keys():
 #print('Key =>', key)
  
#for value in user.values():
 #print('Value =>', value)
 
 #for num in range(6, 16):
    #print(num)
    
#for num in range(10, 31, 2):
    #print(num)
    
    

"""
fav_cereals = ['frosted flakes','shredded wheat',  'honey bunches']

for cereal in fav_cereals:
  if cereal == 'shredded wheat':
    print(f'{cereal} is Gross!')
    break
  print(cereal + " is delicious")
  """

"""
dog_house = ['hndrx', 'joey', 'luna', 'rosco']
  
#while dog_house:
  #print(dog_house.pop(0)) 
  
i = 0
while i < len(dog_house):
  print(dog_house[i])
  i = i + 1
"""

#<h1>Hi</h1>
#def heading_generator(title, heading_type):
 # return(f'<h{heading_type}>{title}</h{heading_type}>')
    
#print(heading_generator('Hi', 1))

"""
answer = False

if answer == False:
  answer = True 
  
print(answer)
"""
"""
def watermelon_party():
  
  watermelon: 36
  
  if watermelon > 50:
    print(True)
  else:
    print(False)
    
watermelon_party()
"""


"""
def kid():
  
  age = 15
  
  if age == 15:
    print(f'Can get a permit, but not a liscense')
  elif age < 15:
    print(f'Can\'t get anything')
  else:
    print(f'Can get license')
    
kid()
"""
"""
def age_verification(age):
  if age < 25:
    print(f'You cannot rent a car')
  else:
    print(f'you can rent whatever you want')   
    
age_verification(23)
"""
"""
def age_verification(age):
  print('Can\'t rent car' if age < 25 else 'can rent car')
  

age_verification(10)
age_verification(2)
"""

"""
sentence = 'Python is best!'
word = 'the'

if word in sentence:
  print('The word is in the sentence')
else: 
  print('The word is not in the sentence')
  
nums = [1, 2, 3, 4]
num = 6

if num in nums:
  print('The number was found')
else:
  print('The number was not found')
"""

"""
a = 200
b = 33
c = 500 

if a >= 200 and b == 33:
  print('both are True')
  
if c == 500 or b > 55:
  print('at least one is True')
"""

"""
def greeting():
  print('Hello')
  
greeting()
"""

"""
def greeting(name):
  print(f'Hello, {name}')
  
greeting('boli')
"""

"""
def sum_two_numbers(num1, num2):
  print(num1 + num2)
  
sum_two_numbers(3, 5)
"""

"""
def sum_two_numbers(num1, num2):
  return num1 + num2

result = sum_two_numbers(4, 17)

print(result)
"""

"""
def greeting(first, last):
  def full_name():
    return f'{first} {last}'
  
  print(f'Hi {full_name()}')
  
greeting('Ashley', 'Orozco')
"""

"""
full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))
"""

"""
sum_of_numbers = lambda num1, num2: num1 + num2


def adding_nums(num1, num2):
      print(num1 + num2)

adding_nums(sum_of_numbers(67, 234)):
"""




