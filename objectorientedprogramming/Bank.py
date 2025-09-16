
# Bank (bank_name,person_name,account_number,balance) 
# (deposit(amount),
# withdraw(amount),
# bal_enq()
# )

class Bank:

    def set_customer_details(self,person_name,acc_no,bal):

        self.bank_name ="SBI"

        self.person_name = person_name

        self.acc_no = acc_no

        self.bal = bal


    def bal_enq(self):

        print(f"dear{self.bank_name} customer your acc{self.acc_no} avl bal is {self.bal}  ")


    def deposit(self,amount):

        self.bal += amount

        print(f"your {self.bank_name} acc {self.acc_no} has been credited with amount {amount} aval bal {self.bal}")

    def withdraw(self,amount):

        if self.bal < amount:

            print("transaction failed insuficcient bal")

        else:

            self.bal -= amount
            print(f"your {self.bank_name} acc {self.acc_no} has been debited with amount {amount} aval bal {self.bal}")



bank_instance1= Bank()

bank_instance1.set_customer_details("vipin",1234,2000)


bank_instance1.withdraw(25000)


bank_instance1.bal_enq()

# object oriented features

# Topic for tomorrow : looping (while,for,break,continue)

