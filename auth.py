import random
import validation
import database
from getpass import getpass


# initialization function
def init():
    isValidOptionsSelected = False
    print('Welcome to Bank Ruby')

    haveAccount = int(input('Do you have an account with us: (1) Yes (2) No (3) Exit \n'))

    if(haveAccount == 1):
        login()

    elif(haveAccount == 2):
        register()

    elif(haveAccount == 3):
        print('Thank you for banking with us')
        exit()

    else:
        print('You have selected invalid option')
        init()


# login function
def login():
    print('********** Login **********')

    accountNumberFromUser = input('Enter your account number: \n')

    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:

        password = input('Enter password: ')
        # password = getpass('Enter password: ')

        user = database.authenticateUser(accountNumberFromUser, password)

        if user:
            bankOperation(user)

        # for accountNumber, userDetails in database.items():
        #     if accountNumber == int(accountNumberFromUser):
        #         if userDetails[3] == password:
        #             bankOperation(userDetails)

        print('Invalid account or password')
        login()

    else:
        print('Account Number invalid: check that you have up to 10 digits and only integers')
        init()


# register function
def register():

    print('******* Register ********')

    email = input('Email address: ')
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    password = input('Create password: ')

    # password: str = getpass('Create password: ')

    accountNumber = generateAccountNumber()

    # using database module to create new user record

    isUserCreated = database.create(
        accountNumber, firstName, lastName, email, password)

    if isUserCreated:
        print('Your account has been created')

        print('== ==== ====== ==== ===')
        print('Your account number is : %d' %accountNumber)

        print('Make sure you keep it safe')
        print('== ==== ====== ==== ===')

        login()

    else:
        print('Something went wrong, please try again')
        register()


# bank operation
def bankOperation(user):
    print('Welcome %s %s' % (user[0], user[1]))

    selectedOption = int(input('What would you like to do today: (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n'))

    if selectedOption == 1:
        depositOperation()

    elif selectedOption == 2:
        withdrawalOperation()

    elif selectedOption == 3:
        logout()

    elif selectedOption == 4:
        exit()

    else:
        print('Invalid option selected')
        bankOperation(user)


def withdrawalOperation():
    print('Withdrawal')
    # get current balance
    # getCurrentBalance(userDetails, balance)
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdrawn amount form current balance
    # display current balance


def depositOperation():
    print('Deposit Operations')
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance

    userSelection = int(input('Do you want to perform another operation: (1) Yes (2) No \n'))

    if userSelection == 1:
        bankOperation()
    elif userSelection == 2:
        logout()
    else:
        print('You have selected a wrong option')


# generate account number
def generateAccountNumber():
    # Generating Account Number
    return random.randrange(0000000000, 9999999999)


def getCurrentBalance(userDetails, balance):
    return userDetails[4] == balance


def logout():
    # clear all session
    print('Thank you for banking with us')
    userSelection = int(input('*** Will you to login again: (1) Yes (2) No ***\n'))

    if userSelection == 1:
        login()
    elif userSelection == 2:
        exit()
    else:
        print('You have selected a wrong option')


# Actual Banking System
init()