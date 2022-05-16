
def accountNumberValidation(accountNumber):
    # check if account_no is not empty
    if accountNumber:

        # if account_no is 10 digits
        if len(str(accountNumber)) == 10:
             # if the account_number is an integer
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

# accountNumberValidation(8687237620)

# def validateRegistrationInput(input):
#     # check a list of input
#     # check each item in the list for correct datatype
#     print('Validate Registration input')
