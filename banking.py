# declare constants
TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1 , 2, 3, 4, 5)

class BankAccount:
    accountBalance = 0
    transactions = []

# banking storage 
accountBalance = 0
transactions = []

# print menu to console providing options
def printMenu():
    print(f"\tEnter {WITHDRAW}: withdraw")
    print(f"\tEnter {DEPOSIT}: deposit")
    print(f"\tEnter {BALANCE}: check balance")
    print(f"\tEnter {SUMMARY}: summary of transactions")
    print(f"\tEnter {WITHDRAW_SUMMARY}: summary of withdraws")
    print(f"\tEnter {TERMINATE}: exit")

# manage withdrawal operation
def withdrawAmount():
    # accountBalance as global allowing modification/mutate
    global accountBalance
    withdraw = float(input('Enter amount to withdraw:'))
    if withdraw > accountBalance:
        print('Invalid amount')
    else:
        accountBalance -= withdraw
        transactions.append(('withdraw', withdraw))

# manage deposit operation
def depositAmount():
    # accountBalance as global allowing modification/mutate
    global accountBalance
    deposit = float(input('Enter amount to deposit:'))
    if deposit <= 0:
        print('Invalid amount')
    else:
        accountBalance += deposit
        transactions.append(('deposit', deposit))

# Display present balance
def checkBalance():
    print(f'Your present balance is: P {accountBalance}')
    transactions.append(('check-balance', accountBalance))

# Display list of transactions
def printTransactions(operations):
    # transform all transactions to print lines as formatted string
    lines = map(lambda trans: f'{trans[0]} = {trans[1]}', operations)
    counter = 1
    for line in lines:
        print(f'{counter}: {line}')
        counter += 1

# Display all transactions
def printSummary():
    printTransactions(transactions)

# Display only withdrawal transactions
def printWithdrawSummary():
    withdraws = filter(lambda trans: trans[0] == 'withdraw' , transactions )
    printTransactions(withdraws)

# entry point
def main():
    # initialize operation not(TERMINATE) allowing initial loop entry
    operation = BALANCE
    while operation != TERMINATE:
        printMenu()
        operation = int(input("Enter op code: "))
        if operation == WITHDRAW:
            withdrawAmount()
        elif operation == DEPOSIT:
            depositAmount()
        elif operation == BALANCE:
            checkBalance()
        elif operation == SUMMARY:
            printSummary()
        elif operation == WITHDRAW_SUMMARY:
            printWithdrawSummary()
        elif operation == TERMINATE:
            print('Good bye')
        else:
            print("Invalid operation")

# invoke entry point
main()