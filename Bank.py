
import datetime

class NAWAF_Bank:
    naw=9
    def __init__(self):
        self.__account=0


    def set_deposit(self,amount):
        if amount>0 and type(amount)==type(0):
            self.__account +=amount
            print(datetime.datetime.today().strftime("{} riyals were deposited to the bank balance in one day %A ,"
                                                     " %m %B %Y,at %I:%M %p").format(amount) )
        else:
            print("invlid number")

    def set_Withdrawal(self,amount):
        if amount<=self.__account and type(amount)==type(0):
            self.__account -= amount
            print(datetime.datetime.today().strftime("{} riyals were deducted to the bank balance in one day %A ,"
                                                     " %m %B %Y,at %I:%M %p").format(amount))
        else:
               print("invlid number")

    def get_Balance_Inquiry(self):
        print(self.__account)

def get_Balanyce_Inquiry(self):
    print(self.__account)
nawaf=NAWAF_Bank()
nawaf.set_deposit(15000)
nawaf.set_Withdrawal(1000)
nawaf.get_Balance_Inquiry()

