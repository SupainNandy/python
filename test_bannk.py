from bank import Bank

sbi = Bank()

hdfc = Bank()

Punb = Bank()

print(sbi.sno)
print(hdfc.sno)
print(Punb.sno)

print(Bank.get_counter())

Bank.set_counter(100)

print(Bank.get_counter())

