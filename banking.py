# declare constants
TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1 , 2, 3, 4, 5)

class BankAccount:
    def __init__(self, accountName):
        self.name = accountName

    accountBalance = 0
    transactions = []

    # manage deposit operation
    def depositAmount(self):
        deposit = float(input('Enter amount to deposit:'))
        if deposit <= 0:
            print('Invalid amount')
        else:
            self.accountBalance += deposit
            self.transactions.append(('deposit', deposit))
    
    # manage withdrawal operation
    def withdrawAmount(self):
        withdraw = float(input('Enter amount to withdraw:'))
        if withdraw > self.accountBalance:
            print('Invalid amount')
        else:
            self.accountBalance -= withdraw
            self.transactions.append(('withdraw', withdraw))

    # Display present balance
    def checkBalance(self):
        print(f'Your present balance is: P {self.accountBalance}')
        self.transactions.append(('check-balance', self.accountBalance))

    # Display list of transactions
    def printTransactions(self, operations):
        # transform all transactions to print lines as formatted string
        lines = map(lambda trans: f'{trans[0]} = {trans[1]}', operations)
        counter = 1
        for line in lines:
            print(f'{counter}: {line}')
            counter += 1

    # Display all transactions
    def printSummary(self):
        self.printTransactions(self.transactions)

    # Display only withdrawal transactions
    def printWithdrawSummary(self):
        withdraws = filter(
            lambda trans: trans[0] == 'withdraw' , 
            self.transactions 
        )
        self.printTransactions(withdraws)

# print menu to console providing options
def printMenu():
    print(f"\tEnter {WITHDRAW}: withdraw")
    print(f"\tEnter {DEPOSIT}: deposit")
    print(f"\tEnter {BALANCE}: check balance")
    print(f"\tEnter {SUMMARY}: summary of transactions")
    print(f"\tEnter {WITHDRAW_SUMMARY}: summary of withdraws")
    print(f"\tEnter {TERMINATE}: exit")

# entry point
def main():
    # initialize operation not(TERMINATE) allowing initial loop entry
    account = BankAccount("Luffy")
    operation = BALANCE
    while operation != TERMINATE:
        printMenu()
        operation = int(input("Enter op code: "))
        if operation == WITHDRAW:
            account.withdrawAmount()
        elif operation == DEPOSIT:
            account.depositAmount()
        elif operation == BALANCE:
            account.checkBalance()
        elif operation == SUMMARY:
            account.printSummary()
        elif operation == WITHDRAW_SUMMARY:
            account.printWithdrawSummary()
        elif operation == TERMINATE:
            print('Good bye')
        else:
            print("Invalid operation")

# invoke entry point
main()