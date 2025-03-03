
class Reserve_bank:
    def __init__(self):
        self.reserve_balance = 100000
        self.acc1_no = 100

class Tamil_nadu(Reserve_bank):
    def __init__(self):
        super().__init__()
        self.tamil_balance = 10000
        self.acc2_no = 10

class SBI(Tamil_nadu):
    def __init__(self):
        super().__init__()
        self.account = {}
        self.balance = {}
        self.acc_no = 1

    def accnt_opening(self):
        n = input("Enter your name: ")
        m = input("Enter your mail id: ")
        self.account[self.acc_no] = [n, m]
        self.balance[self.acc_no] = 0
        print(f"Your account number is {self.acc_no}")
        self.acc_no += 1
        self.acc1_no += 1  
        self.acc2_no += 1  

    def Close_account(self):
        n = int(input("Enter your account number: "))
        if n in self.account:
            self.account.pop(n)
            self.balance.pop(n)
            print("Account Closed")
        else:
            print("Invalid bank account number")

    def deposit_money(self):
        m = int(input("Enter your account number: "))
        if m in self.balance:
            q = int(input("Enter the amount to be deposited: "))
            self.balance[m] += q
            self.tamil_balance += q
            self.reserve_balance += q
            print(f"The balance in your account is {self.balance[m]}")
        else:
            print("Invalid bank account")

    def withdraw_money(self):
        acc = int(input("Enter your account number: "))
        if acc in self.balance:
            withdraw = int(input("Enter the amount to be withdrawn: "))
            if withdraw <= self.balance[acc]:
                self.balance[acc] -= withdraw
                self.tamil_balance -= withdraw
                print(f"The balance in your account is {self.balance[acc]}")
            else:
                print("Insufficient funds")
        else:
            print("Invalid account number")

    def print_data(self):
        b = int(input("Enter your account number: "))
        if b in self.account:
            if b in self.balance:
                data = self.account.get(b)
                print(f"Your name is {data[0]}")
                print(f"Your mail id is {data[1]}")
                print(f"The balance in your account is {self.balance[b]}")
        else:
            print("Invalid account number")

    def acc_details(self):
        print("Account Details:")
        for acc_no, (name, email) in self.account.items():
            print(f"Account Number: {acc_no}, Name: {name}, Email: {email}, Balance: {self.balance[acc_no]}")

    def Create_files(self):
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project.txt", "w") as a:
            a.write(str(self.account))
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project1.txt", "w") as b:
            b.write(str(self.balance))
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project2.txt", "w") as c:
            c.write(str(self.acc_no))
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project3.txt", "w") as d:
            d.write(str(self.reserve_balance))
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project4.txt", "w") as e:
            e.write(str(self.acc1_no))

        with open("/Users/kamal/Desktop/Pythonfiles/Python_project5.txt", "w") as f:
            f.write(str(self.acc2_no))

        with open("/Users/kamal/Desktop/Pythonfiles/Python_project6.txt", "w") as g:
            g.write(str(self.tamil_balance))
        
        

    def add_data(self):
        
        with open("/Users/kamal/Desktop/Pythonfiles/Python_project.txt", "r") as a:
            with open("/Users/kamal/Desktop/Pythonfiles/Python_project1.txt", "r") as b:
                 with open("/Users/kamal/Desktop/Pythonfiles/Python_project2.txt", "r") as c:
                     with open("/Users/kamal/Desktop/Pythonfiles/Python_project3.txt", "r") as d:
                         with open("/Users/kamal/Desktop/Pythonfiles/Python_project4.txt", "r") as e:
                             with open("/Users/kamal/Desktop/Pythonfiles/Python_project5.txt", "r") as f:
                                 with open("/Users/kamal/Desktop/Pythonfiles/Python_project6.txt", "r") as g:
                                     X = a.read()
                                     Y = b.read()
                                     Z = c.read()
                                     Q =d.read()
                                     W =e.read()
                                     E =f.read()
                                     F =g.read()
                                     if len(X) > 0:
                                         self.account = eval(X)
                                         self.balance = eval(Y)
                                         self.acc_no=eval(Z)
                                         self.reserve_balance=eval(Q)
                                         self.acc1_no=eval(W)
                                         self.acc_no2=eval(E)
                                         self.tamil_balance=eval(F)
                                         
                                     else:
                                         pass


X = SBI()
X.add_data()
X.accnt_opening()
X.accnt_opening()
X.deposit_money()
X.deposit_money()
X.withdraw_money()
X.withdraw_money()
X.print_data()
X.acc_details()
X.Create_files()
