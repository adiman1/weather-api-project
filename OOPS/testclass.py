class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0
        self.menu()

    def menu(self):
        menu_choice = int(input(""" Hello, How may we help you
    1. Create Pin 
    2. Deposit Money
    3. Withdraw Money
    4. Check Balance                                       
    """))
        if menu_choice == 1:
            self.create_pin()
        elif menu_choice == 2:
            self.deposit()
        elif menu_choice == 3:
            self.withdraw()
        elif menu_choice == 4:
            self.check_balance()
        else:
            print('Exited')

    def create_pin(self):
        self.__pin = input('Enter your pin:')
        print('PIN Successfully created')
        self.menu()

    def deposit(self):
        pin = input('Enter your PIN')
        if pin == self.__pin:
            deposit = int(input('Enter deposit amount'))
            self.__balance = self.__balance + deposit
            print('Amount successfully deposited')
        else:
            print('Wrong PIN')
        self.menu()

    def withdraw(self):
        pin = input('Enter your PIN')
        if pin == self.__pin:
            withdraw = int(input('Enter deposit amount'))
            self.__balance = self.__balance - withdraw
            print('Amount successfully withdrawn')
        else:
            print('Wrong PIN')
        self.menu()

    def check_balance(self):
        pin = input('Enter your PIN')
        if pin == self.__pin:
            print(f'your balance is {self.__balance}')
        else:
            print('Wrong PIN')
        self.menu()