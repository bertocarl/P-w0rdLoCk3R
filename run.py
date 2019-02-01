#!/usr/bin/env python3.6
from user import User

from credentials import Credentials
import keyring


def create_user(email, user_name, password):
    '''
    Function to create a new user
    '''
    new_user = User(email, user_name, password)
    return new_user

def create_credentials(account,account_name,account_password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(account,account_name,account_password)
    return new_credentials

def save_user(user):
    '''
    Function to save users
    '''
    user.save_user(user)

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_user(user):
    '''
    Function to delete a credentials
    '''
    user.delete_user()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()

def find_credentials(account_name):
    '''
    Function that finds a credentials by number and returns the credentials
    '''
    return Credentials.find_by_account(account_name)

def check_existing_credentials(account_name):
    '''
    Function that check if a credentials exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(account_name)

def display_credentials():
    '''
    Function that returns all the saved credentialss
    '''
    return Credentials.display_credentials()

def main():
        print('Welcome TO PASSWORD LOCKER !!!')
        print("Use these short codes:\n [1] - Yes \n [2] - No")
        status = input("Do you have a Password Locker account yet?")

        if status == '1':
            
            print(" To login , enter your account deails : ")
            user_name = input("Enter your usename name : ")
            password = ('Password: ')
            user_exists = user_name

            if user_exists == user_name :
                print(" ")
                print (f"Welcome back {user_name} /n Please choose an option to continue")
                print(" ")

        elif status == '2':
            print("Create an account")
            email= input('Enter email: ')
            user_name= input('Select Username: ')
            pass_1 = input('Password: ')
            pass_2 = input('Re-enter Password: ')
                  
            while pass_1 != pass_2:
                print("sorry your passwords do not match")
                print("Enter your password again")
                pass_1 = input('Password: ')
                pass_2 = input('Re-enter Password: ')

        
            else:
                print(f"New Password Locker Account for {user_name} has been created")
                print(" You can now login to your account : ")
                new_user = input("Enter your usename name : ")
                new_password = pass_2

                
            while new_user !=  user_name or new_password != pass_2:
                print("you have entered a wrong username or password")
                print("Please enter your login information again....") 
                new_user = input("Enter usename: ")
                new_password = pass_2        

            else:
                print(f"Welcome {new_user} to your Password locker account. \n")  

                while True:
                    print("Select an option below to continue:")
                    print("")

                    print(" [v] View your saved accounts \n [+] Add a new account \n [-] Delete credentials \n [*] Find an account \n [0] Logout \n [cp] Copy information")
                    option = input()
                    
                    if option == '0':
                        print("See you later....")
                        break

                    elif option == "-":
                        while True:
                            print("Type credential name you want to delete......")
                            search_account = input()
                            if check_existing_credentials(search_account):
                                search_credential = find_credentials(search_account)
                                print(f"Account :{search_credential.user_account}\n Password: {search_credential.account_password}")
                                print(f"are you sure you want to delete {search_credential.user_account} ? \n [y] \n [n]")
                                answer = input().lower()

                                if answer == 'y':
                                    del_credentials(search_credential)
                                    print("Account has been deleted sucessfully")
                                    break
                                elif answer == 'n':
                                    continue
                                else:
                                    break

                    elif option == "+":
                        while True:

                            print ("Enter Account Name")
                            user_account = input()
                            print("Enter your desired password")
                            print(" [c] To create your own password use  \n [gen] Generate a random one use  ")
                            keyword = input().lower()
                            if keyword == "c" :
                                account_password = input()
                                print(f" Account : {user_account}")
                                print(f" Password : {account_password}")
                                print(" ")

                            
                            else:

                                if keyword = "gen":
                                    char = 'abcdefghijklmnopqrstuvwxyz0123456789'
                                    password =random.choice(char) 
                                    print('password')                             
                                    break

                    elif option == "v":
                        print("")
                        if display_credentials(): 
                            for credential in display_credentials():
                                print(f"Account Name : {credential.user_account}") 
                                print(f"Password : {credential.account_password}")
                        else:
                            print("")
                            print(" You don't have any credentials yet")
                            print("")

                    elif option == "*":
                        while True:
                            print("Enter an account name to find credentials")
                            search_account = input()
                            if check_existing_credentials(search_account):
                                    search_account = find_credentials(search_account)
                                    print(f"{search_account.user_account} \n {search_account.account_password}")
                                    print('-'*10)
                            else:
                                    print("The credential doesn't exist")
                                    break

if __name__ == '__main__':

    main()