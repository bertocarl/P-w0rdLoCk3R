# import pyperclip
class User:
    """
    Class that generates new instances of users.
    """
    pass

    user_list = [] # Empty user lists

    def save_user(self):

        User.user_list.append(self)

    def delete_user(self):

        User.user_list.remove(self)

    @classmethod
    def user_exist(cls,number):

        for user in cls.user_list:
            if user.phone_number == number:
                    return True
                    
        return False

    
    @classmethod
    def display_users(cls):

        return cls.user_list

    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)


    def __init__(self,user_name,email,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.email = email
        self.password = password