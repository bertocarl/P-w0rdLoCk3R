#!/usr/bin/env python3.6
from user import User

def save_user(user):
    user.save_user()

def create_user(user):
    user.create_user()

def display_users(user):
    display_users()

def check_existing_users(search_number):
    check_existing_users()

def find_users(search_number):
    find_users()

def main():
    print("Hello Welcome to Password Locker Application")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

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
            e_address = input()

            save_users(create_user(f_name, l_name, p_number, e_address))  # create and save new user.
            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.phone_number}")

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
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Phone number.......{search_user.phone_number}")
                print(f"Email address.......{search_user.email}")
            else:
                print("That user does not exist")

        elif short_code == "ex":
            print("Thank you for using Password Locker Application....")
            break
        else:
            print("I really didn't get that. Please use the short codes")
