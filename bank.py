"""
Python Bank ATM
- use of methods
- The user needs to be able to make a deposit
- The user needs to be able to pull money out
- The user needs to be able to pay a bill
- The program needs to track the money in the bank
- The user needs to be able to look up their balance
- The program needs to keep running until the user decides to quit the program.
"""

class Bank: 
  def __init__(self, balance):
    self.balance = balance
         
  def deposit(self):
    amount = input('Amount: ')
    self.balance +=  int(amount)
    print('New Balance: ', self.balance)
          
  def withdrawal(self):
    withdrawal = input('Amount to withdrawal: ')
    self.balance -= int(withdrawal)
    print('New Balance: ', self.balance)
  
  def pay_bill(self):
    
  
  
  def get_balance(self):
      pass

def game():
  playing = True 
  while playing == True:
    playing = False
    quit_game = input('Continue playing? Yes or No? ')
    if quit_game.lower() == 'yes':
      playing = True
    else:
      playing = False
      
game()

#user_one = Bank(300)
#user_one.deposit()