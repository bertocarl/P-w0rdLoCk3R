# import pyperclip
import string
import random
class Credentials:
    """
    Class that generates new instances of credentials.
    """
    pass

    credential_list = [] # Empty credential lists

    def save_credential(self):

        Credential.credential_list.append(self)

    def delete_credential(self):

        Credential.credential_list.remove(self)
    def generate_password(self,stringLength=8,char= string.ascii_letters+string.digits):
        '''
        This is a method to generate random string passwords for the application
        '''

        pass_gen = ''.join(random.choice(char) for i in range(stringLength))
            return pass_gen

    @classmethod
    def find_by_email(cls,number):

        for credential in cls.credential_list:
            if credential.email == number:
                return credential

    @classmethod
    def credential_exist(cls,number):

        for credential in cls.credential_list:
            if credential.email == number:
                    return True

        return False

    @classmethod
    def display_credential(cls):

        return cls.credential_list

    @classmethod
    def copy_email(cls,number):
        credential_found = Credential.find_by_email(number)
        pyperclip.copy(credential_found.email)





    def __init__(self,account,account_name,password):

      # docstring removed for simplicity

        self.account = account
        self.account_name = account_name
        self.password = password