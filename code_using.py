class Bank:
    def __init__(self,n,m,acc,p,ad):
        self.name=n
        self.__balance=0
        self.account=acc
        self.__mobile=m
        self.__pin=p
        self._address=ad

    def __verify(self,num):
        if self.__pin==num:
            return True
        return False
    def checkbalance(self):
        password=input("bhayya pin enter karo::")
        if self.__verify(password):
            print("Available balance:",self.__balance)
        else:
            print(f"endhi babu mosam cheyyali ani chustunava:: ")
    def depoist(self):
        dep=int(input("Endhi Anna Entha Depoist cheyyali: "))
        print("Anna dabbulu ",dep, "vachayiiii pandaga ,motham dabbulu  :",self.__balance+dep)
    def withdraw(self):
        password=input("bhayya pin enter karo::")
        amount=int(input("entha kavali chinna:"))
        if self.__verify(password):
            if amount<=self.__balance:
                print("thisukooo thisukooo",self.__balance-amount)
            else:
                print("hey cheat dabbulu lev babu")
        else:
            print("endhi babu mosam cheyyali ani chustunava:")
    def changepin(self):
        kotha=input("pin nacha ledha sare kotha pin enter cheyyy!:")
        if self.__verify(kotha):
            print("kothapettu bro malli idhe endhuku")
        else:
            self.__pin=koth
            print("your new pin is:",self.__pin)
    def showaddress(self):
        print(self._address)
b=Bank("dj",900,362500,2005,"vadarevu")
b.checkbalance()
