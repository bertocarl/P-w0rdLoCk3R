import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        """
        Set up method to run before each test class
        """
        self.new_user = User("aomware@gmail.com","aomware","password")
       
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.email, "aomware@gmail.com")
        self.assertEqual(self.new_user.user_name, "aomware")
        self.assertEqual(self.new_user.password, "password")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user objects to our user list
        """
        self.new_user.save_user()
        test_user = User("test@use.com","TestUser","password1") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we can not find the users
        '''

        self.new_user.save_user()
        test_user =  User("testemail","test user","testpassword")
        test_user.save_user()

        user_exist = User.user_exist("Test")

self.assertTrue(user_exist)


if __name__ == '__main__':
    unittest.main()
