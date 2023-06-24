#write a python class bankaccount with attributes like account_number,balance,date_of_opening and customer_name,and methods like deposit,withdraw,and check_balance.
class BankAccount:
    account_number=int(input("Acc no:"))
    balance=float(input("Balance:"))
    date_of_opening=str(input("Date of opening:"))
    customer_name=str(input("Customer name:"))
    deposit=float(input("Deposit:"))
    withdraw=float(input("Withdraw:"))
    Bal=deposit+balance
    check_balance=(deposit+balance)-withdraw
obj1=BankAccount
print("Account number:",obj1.account_number)
print("Balance:",obj1.balance)
print("Date of opening:",obj1.date_of_opening)
print("Customer name:",obj1.customer_name)
if (obj1.balance>=obj1.withdraw):
    print("Available balance:",obj1.check_balance)
else:
    print("Insufficient balance!!,Available Balance=",obj1.Bal)
