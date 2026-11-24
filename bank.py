class Bank:
    #Static Variable or Class Veriable
    __counter =  0
    def __init__(self):
        #private attributes
        self.__balance = 0
        self.__pin = "" 
        # while True:            
        # self.manu()
        self.sno = Bank.__counter
        Bank.__counter += 1 
           

    def manu(self):
        user_input = input("""\
How do you like to proceed ?
    1) Enter 1 to create pin.
    2) Enter 2 to deposit
    3) Enter 3 to withdraw
    4) Enter 4 check balance
    5) Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()          
        elif user_input == "4":
            self.check_balance()     
        elif user_input == "5":
            print("exit")

    #Static method
    @staticmethod
    def get_counter():
        return  Bank.__counter

    def set_counter(new):
        if type(new) == int:
            Bank.__counter = new
        else:
            print("Not allowed")

    def get_pin(self):
            print(self.__pin)


    def set_pin(self,new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("pin changed successfuly...")
        else:
            print("Invalid data type")

    # ----------------- pin -----------------
    def create_pin(self):
        self.__pin = input("Enter your pin: ")
        print("Pin created successfully")

    # ----------------- deposit -----------------
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid Pin")

    # ----------------- withdraw -----------------
    def withdraw(self):
        temp = input("Enter your pin : ")
        if temp == self.__pin:
            amount = int(input("Enter amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Operation Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Invalid Pin")

    # ----------------- check balance -----------------
    def check_balance(self):
        temp = input("Enter Your Pin: ")
        if temp == self.__pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid Pin")


