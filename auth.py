import random

#account database dictionary
database = {
    3455667788: ['Sanmi', 'Idowu', 'sanmi@gmail.com', 'password1', 200]
}

balance = {
    3455667788: [234]
}

#initialization function
def init():

    isValidOptionsSelected = False
    print('Welcome to Bank Ruby')

    haveAccount = int(input('Do you have an account with us: (1. Yes 2. No) \n'))

    try:
        if(haveAccount == 1):
            login()

        elif(haveAccount == 2):
            register()

    except ValueError:
        print('You have selected invalid option')
        init()


#login function
def login():
    print('********** Login **********')

    accountNumberFromUser = input('Enter your account number: ')

    isValidAccountNumber = accountNumberValidation(accountNumberFromUser)

    if isValidAccountNumber:

        password = input('Enter password: \n')

        for accountNumber, userDetails in database.items():
            if accountNumber == int(accountNumberFromUser):
                if userDetails[3] == password:
                    bankOperation(userDetails)
        
        print('Invalid account or password')
        login()

    else:
        init()


def accountNumberValidation(accountNumber):
    #check if account_no is not empty
    if accountNumber:

        #if account_no is 10 digits
        if len(str(accountNumber)) == 10:

             #if the account_number is an integer
            try:
                int(accountNumber)
                return True
            except ValueError:
                print('Invalid Account number, account number should be number')
                return False
            except TypeError:
                print('Invalid Account type')
                return False

        else:
            print('Account Number cannot be more than 10 digits')
            return False
    else:
        print('Account Number is a required field')
        return False


#register function
def register():

    print('******* Register ********')

    email = input('Email address: \n')
    firstName = input('First Name: \n')
    lastName = input('Last Name: \n')
    password = input('Create Password: \n')
    
    try:
        accountNumber = generateAccountNumber()

    except ValueError:
        print('Account generation failed')
        init()

    
    database[accountNumber] = [firstName, lastName, email, password]
    
    print('Your account has been created')
    
    print('== ==== ====== ==== ===')
    print('Your account number is : %d' %accountNumber)

    print('Make sure you keep it safe')
    print('== ==== ====== ==== ===')
    
    login()


#bank operation
def bankOperation(user):
    print('Welcome %s %s' %(user[0], user[1] ))

    selectedOption = input('What would you like to do today: (1) Deposit (2) Withdrawal (3) Logout (4) Exit')
    
    try:
        int(selectedOption)

        if (selectedOption == 1):
            depositOperation()
        elif (selectedOption == 2):
            withdrawalOperation()
        elif (selectedOption == 3):
            logout()
        elif(selectedOption == 4):
            exit()

        return True

    except ValueError:
        print('Invalid option selected')
        bankOperation(user)
        return False


def withdrawalOperation():
    print('Withdrawal')

    #get current balance
    getCurrentBalance(userDetails, balance)
    #get amount to withdraw
    #check if current balance > withdraw balance
    #deduct withdrawn amount form current balance
    #display current balance


def depositOperation():
    print('Deposit Operations')
    #get current balance
    #get amount to deposit
    #add deposited amount to current balance
    #display current balance
    
    userSelection = int(input('Do you want to perform another operation: (1) Yes (2) No'))

    if userSelection == 1:
        bankOperation()
    elif userSelection == 2:
        logout()
    else:
        print('You have selected a wrong option')

#generate account number
def generateAccountNumber():
    #Generating Account Number
    return random.randrange(1111111111, 999999999)

def getCurrentBalance(userDetails, balance):
    return userDetails[4] == balance

def logout():
    ##clear all session
    print('Thank you for banking with us')
    userSelection = int(input('*** Will you to login again: (1) Yes (2) No ***'))

    if userSelection == 1:
        login()
    elif userSelection == 2:
        exit()
    else:
        print('You have selected a wrong option')
  
##Actual Banking System
init()