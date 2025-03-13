from functools import reduce
class BankAccount:
    def __init__(self, accountName):
        self.name = accountName

    __transactions = []

    @property
    def computedBalance(self):
        def reducer(total, trans):
            operation, amount = trans
            if operation == 'deposit':
                return total + amount
            elif operation == 'withdraw':
                return total + amount
            else:
                return total
        accountBalance = reduce(reducer, self.__transactions, 0)
        return accountBalance
    
    # manage deposit operation
    def depositAmount(self):
        deposit = float(input('Enter amount to deposit:'))
        if deposit <= 0:
            print('Invalid amount')
        else:
            self.__transactions.append(('deposit', deposit))
    
    # manage withdrawal operation
    def withdrawAmount(self):
        withdraw = float(input('Enter amount to withdraw:'))
        accountBalance = self.computedBalance
        if withdraw > accountBalance:
            print('Invalid amount')
        else:
            self.__transactions.append(('withdraw', withdraw))

    # Display present balance
    def checkBalance(self):
        accountBalance = self.computedBalance
        print(f'Your present balance is: P {accountBalance}')
        self.__transactions.append(('check-balance', accountBalance))

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
        self.printTransactions(self.__transactions)

    # Display only withdrawal transactions
    def printWithdrawSummary(self):
        withdraws = filter(
            lambda trans: trans[0] == 'withdraw' , 
            self.__transactions 
        )
        self.printTransactions(withdraws)
