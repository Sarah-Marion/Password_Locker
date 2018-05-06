#!/usr/bin/env python3.6
from credential import Credential
from user_data import User

# Funtions dependent on the User Class
def create_user(fullname, email, username, password):
    """
    Function to create a new user
    """
    new_user = User(fullname, email, username, password)
    return new_user

def save_new_user(new_user):
    """
    Function to save user
    """
    new_user.save_user()

def check_existing_user(username):
    """
    Function that check if a user exists/is logged in with that username and return a Boolean
    """
    return User.user_exists(username)

def find_user(username):
    """
    Function that finds a user by username and returns the user
    """
    return User.find_by_username(username)

# Funtions dependent on the Cred Class
def create_cred(accountName, email, username, password):
    """
    Function to create new credentials
    """
    new_cred = User(accountName, email, username, password)
    return new_cred

def save_new_cred(new_cred):
    """
    Function to save credentials
    """
    new_cred.save_cred()

def del_cred(cred):
    """
    Function to delete credentials
    """
    cred.delete_cred()

def check_existing_cred(accountName):
    """
    Function that check if credentials exist with that accountName and return a Boolean
    """
    return Credential.cred_exists(accountName)

def find_cred(accountName):
    """
    Function that finds a user's credentials by accountName and returns the credentials
    """
    return Credential.find_by_accountName(accountName)

def gen_password(username):

    return Credential.gen_password(username)

def display_accounts():
    """
    Function that returns all the saved accounts
    """
    return Credential.display_accounts()

def main():
    print("Welcome to Password Locker")
    print("-"*10)

    while True:
        print("Please use the following short codes:")
        print ("su - Sign-up, li - Login, ex - Exit")
        print('\n')
        short_code = input().lower()
        
        if short_code == 'su':
            print("Sign up to create a Password Locker account")
            print("-"*20)

            print("Fullname.....")
            fullname = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()

            print("Password.....")
            password = input()

            save_new_user(User(fullname, email, username, password))
            print('\n')
            print(f"Welcome {username}, your account has successfully been created")
            print ('\n')

        elif short_code == 'li':
            print("Login to your Password Locker account")
            print("-"*20)

            # while True:

            print("Username.....")
            search_user = input()
            if check_existing_user(search_user):
                user_find = find_user(search_user)
                # while True:
                print("Password.....")
                password = input()
                if password == user_find.password:
                    print(f"Welcome {username}, you are logged in!")
                    print ('\n')


                    while True:
                        print("Please use the following short codes:")
                        print("""
                        add - Add & save existing accounts, gen - Generate password for new account,
                        disp - display accounts, del - Delete account, lo - Log out
                        """)

                        short_code = input().lower()

                        if short_code == 'add':
                            print ('\n')
                            print("Add new account")
                            print("-"*10)

                            print("Account Name.....")
                            accountName = input()

                            print("Email Address.....")
                            email = input()

                            print("Username.....")
                            username = input()

                            print("Password.....")
                            password = input()

                            save_new_cred(Credential(accountName, email, username, password))
                            print('\n')
                            print(f"Your {accountName} account has successfully been added!")
                            print ('\n')

                        elif short_code == 'gen':
                            print ('\n')
                            print("A random password will be created for this account")
                            print("-"*30)

                            print("Account Name.....")
                            accountName = input()

                            print("Email Address.....")
                            email = input()

                            print("Username.....")
                            username = input()

                            password = gen_password(username)
                            print(f"Your password is {password}")
                            save_new_cred(Credential(accountName, email, username, password))
                            print('\n')
                            print(f"Your {accountName} account has successfully been added!")
                            print ('\n')

                        elif short_code == 'disp':
                            if display_accounts():
                                print ('\n')
                                print("Here is a list of all your accounts")
                                print('\n')

                                for cred in display_accounts():
                                    print(f"{cred.accountName}, {cred.email}, {cred.username}, {cred.password}")
                                    print('\n')
                            else:
                                print('\n')
                                print("You dont seem to have any contacts saved yet")
                                print('\n')

                        elif short_code == 'del':
                            print ('\n')
                            print("What is the name of the account you want to delete?...")
                            accountName = input()
                            if find_cred(accountName):
                                del_cred = input()
                                print('\n')
                                print(f"Your {accountName} account has successfully been deleted!")
                                print ('\n')

                        elif short_code == 'lo':
                            print ('\n')
                            print("Sorry to see you go... Come back soon!")
                            print ('\n')
                            break

                        else:
                            print ('\n')
                            print("I really didn't get that. Please use the short codes")
                            print ('\n')
                            # break

                    else:
                        print("Incorrect password")
                        print ('\n')

                else:
                    print(f"{username} does not exist, please sign up.")
            elif short_code == 'ex':
                print("\n")
                print("An interrupt detected...Exiting..")
                print("\n")
                break
            else:
                print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()