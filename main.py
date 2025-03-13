from banking import BankAccount

# declare constants
TERMINATE, WITHDRAW, DEPOSIT, BALANCE, SUMMARY, WITHDRAW_SUMMARY = (0, 1 , 2, 3, 4, 5)


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
if __name__ == '__main__':
    main()