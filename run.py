#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(f_name,l_name,p_number,email,password):

    new_user = User(f_name,l_name,p_number,email,password)
    return new_user

def create_credential(email,platform,password):

    new_credential = Credential(email,platform,password)
    return new_credential

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def save_users(user):

    user.save_user()

def save_credential(credential):

    credential.save_credential()

def del_user(user):

    user.delete_user()

def delete_credential(credential):

    credential.delete_credential()

def find_user(number):

    return User.find_by_number(number)

def find_credential(number):

    return Credential.find_by_email(number)

def check_existing_users(number):

    return User.user_exist(number)

def check_existing_credential(number):

    return Credential.credential_exist(number)

def display_users():

    return User.display_users()

def display_credential():

    return Credential.display_credential()

def test_copy_email():

    return User.copy_email()

def test_copy_email():

    return Credential.copy_email()

def main():
    print("Hello Welcome to Password Locker Application")
     
        email = input("email") 
        password = input("Password: ")
    
        if email == 'aomware@gmail.com' and password == 'admin':
            print(f"Hello {username}. what would you like to do?")
            print('\n')
        else:
            break

    while True:
        print(
            "Use these short codes : cu - create a new user, du - display users, fu -find a user, ex -exit the user list ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-" * 10)

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            email = input()

            print("Password ...")
            password = input()

            save_users(create_user(f_name,l_name,p_number,email,password))

            print ('\n')

            print(f"New User {f_name} {l_name} created")

            print ('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.f_name} {user.l_name} .....{user.p_number}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any users saved yet")
                print('\n')

        elif short_code == 'fu':

            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_users(search_number):
                search_user = find_users(search_number)
                print(f"{search_user.name} {search_user.l_f_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Thank you for using Password Locker Application....")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()