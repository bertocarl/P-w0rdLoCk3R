import unittest # Importing the unittest module
from userCredentials import Credentials # Importing the User class

class TestCredential(unittest.TestCase):

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
        self.credential_list = Credentials("Instagram","FTKaragu","123456") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.credential_list.platform,"")
        self.assertEqual(self.credential_list.account_name,"")
        self.assertEqual(self.credential_list.password,"")


if __name__ == '__main__':
    unittest.main()