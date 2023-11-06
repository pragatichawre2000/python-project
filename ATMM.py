# CORRERCT CODE
class Atm:
    #constructor
    def __init__(self):
        self.pin =''
        self.balance = 0
        self.menu()
        
     
    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        """)

        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
             self.change_pin()
             #change pin
        elif user_input  == '3':
            #check balance
             self.check_balance()
        elif user_input == '4':
             #withdraw
             self.withdraw()
             
        else:
            exit()

    def create_pin(self):
        user_pin = input('enter your pin :') 
        self.pin = user_pin

        user_balance = int(input('enter balance:'))
        self.balance = user_balance

        print('pin created succeefully')
        self.menu()

    def change_pin(self):
        old_pin =input('enter old pin:')
        
        if old_pin == self.pin:
            #let him change the pin
            new_pin= input('enter new pin:')
            self.pin =  new_pin
            print('pin change successful')
            self.menu()
        else:
            print('Incorrect pin')
            self.menu()

    def check_balance(self):
        user_pin = input('enter your pin:')
        if user_pin == self.pin:
            print("your balance is ", self.balance)
            self.menu
        else:
            print('nhi hai')
            self.menu
    
    def withdraw (self):
        user_pin  = input('enter the pin:')
        if user_pin == self.pin:
          #allow to withdraw
            amount = int(input('enter the amount'))
            if amount<= self.balance:
                self.balance = self.balance - amount
                print('withdrawl successful.balance is',self.balance) 

            else:
                print("No,you cannot withdraw")
        else:
            print('Wrong password')
            self.menu()

obj=Atm()


