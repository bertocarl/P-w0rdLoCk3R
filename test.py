import unittest # Importing the unittest module
from user import User # Importing the User class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.user_list = User("","","","" # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user_list.user_name,"")
        self.assertEqual(self.user_list.email,"")
        self.assertEqual(self.user_list.password,"")


if __name__ == '__main__':
    unittest.main()