# create record
# update record
# read record
# delete record

import os
import validation

user_db_path = "data/user_record/"


def create(accountNumber, firstName, lastName, email, password):
    # create a file
    userData = firstName + "," + lastName + "," + email + "," + password + str(0)

    if doesAccountNumberExist(accountNumber):

        return False

    if doesEmailExist(email):
        print('User already exists')
        return False

    completionState = False

    try:
        # name of the file accountNumber.txt
        f = open(user_db_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:
        # delete the already created file and print out error
        doesFileContainData = read(user_db_path + str(accountNumber) + ".txt")

        if not doesFileContainData:
            delete(accountNumber)

    else:
        # add the user details to the file
        f.write(str(userData))
        completionState = True

    finally:
        f.close()
        return completionState

    # if saving to file fails, then delete created file
    # return true


def read(userAccountNumber):
    # find user with account number
    # fetch content of the file and return
    isValidAccountNumber = validation.accountNumberValidation(userAccountNumber)

    try:

        if isValidAccountNumber:
            f = open(user_db_path + str(userAccountNumber) + ".txt", "r")
        else:
            f = open(user_db_path + userAccountNumber, "r")

    except FileNotFoundError:

        print('User not found')

    except FileExistsError:

        print("User doesn't exist")

    except TypeError:

        print("Invalid account format")

    else:

        return f.readline()

    return False


def update(userAccountNumber):
    print('Update user record')
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return True


def delete(userAccountNumber):
    # find user with account number
    isDeleteSuccessful = False

    if os.path.exists(user_db_path + str(userAccountNumber) + ".txt"):

        try:
            # delete the user record (file)
            os.remove(user_db_path + str(userAccountNumber) + ".txt")
            isDeleteSuccessful = True

        except FileNotFoundError:
            print('User not found')

        finally:
            return isDeleteSuccessful


def find(userAccountNumber):
    print('Find user')
    # find user record in the data folder


def doesEmailExist(email):
    allUsers = os.listdir(user_db_path)

    for user in allUsers:

        user_list = str.split(read(user))
        if email in user_list:
            return True
        return False


def doesAccountNumberExist(accountNumber):

    allUsers = os.listdir(user_db_path)

    for user in allUsers:

        if user == str(accountNumber) + ".txt":
            return True

        return False


def authenticateUser(accountNumber, password):

    if doesAccountNumberExist(accountNumber):

        user = str.split(read(accountNumber), ',')

        if password == user[3]:
            return user

    return False


# print(authenticateUser(8642379518, "password1"))
