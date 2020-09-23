"""
nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()
"""
numbers = [1,2,3,4,5,6]
results = []

for number in numbers:
    print(number + 1)
    results.append(number + 1)
    
print(results)