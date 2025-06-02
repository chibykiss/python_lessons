from bank_accounts import *

vibe = BankAccount(1000,'Vibe')
# vibe.getBalance()
# vibe.deposit(500)

mercy = BankAccount(2000,'Mercy')
mercy.getBalance()
mercy.withdraw(500)

vibe.transfer(2000,mercy)

james = InterestRewardsAcct(1000,'James')
james.getBalance()
james.deposit(100)

james.transfer(100, vibe)

bond = SavingsAcct(1000,'Bond')
bond.getBalance()
#bond.deposit(100)
bond.withdraw(1000)