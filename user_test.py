import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("aomware@gmail.com","aomware123") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.f_name,"")
        self.assertEqual(self.new_user.l_name,"")
        self.assertEqual(self.new_user.p_number,"")
        self.assertEqual(self.new_user.email,"")
        self.assertEqual(self.new_user.password,"")


    def test_save_user(self):
    '''
    test_save_user test case to test if the user object is saved into
     the user list
    '''
    self.new_user.save_user()  # saving the new user
    self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
