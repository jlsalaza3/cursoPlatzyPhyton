class BanckAccount:
    def __init__(self, account_holder, balance):
        self.account_holder=account_holder
        self.balance=balance
        self.is_Active=True
    def deposit(self, amount):
        if self.is_Active:
            self.balance += amount
            print(f"Se ha depositado: {amount}. Saldo Actual= {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    def withdraw(self, amount):
        if self.is_Active:
            if amount<=self.balance:
                self.balance-=amount
                print(f"Se ha retirado: {amount} y el nuevo saldo es: {self.balance}")
    def deactivate_account(self):
        self.is_Active=False
        print(f"La cuenta ha sido desactivada")
    def activate_account(self):
        self.is_Active=True
        print(f"La cuenta ha sido activada")
account1=BanckAccount("Ana",500)
account2=BanckAccount("Pedro",1000)

#llamada a los métodos:
account1.deposit(200)
account2.deposit(100)
account1.deactivate_account()
account1.deposit(50)
account1.activate_account()
account1.deposit(50)