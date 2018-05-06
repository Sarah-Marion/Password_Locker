import unittest
from user_data import User

class user_test(unittest.TestCase):
    """
    Test class that defines test cases for the user_data class behaviours
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_user = User("Sarah Marion","devsarahmarion@gmail.com","dev Sarah","@#saR!aH09")


    def test_init(self):
        """
        test init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.fullname,"Sarah Marion")
        self.assertEqual(self.new_user.email,"devsarahmarion@gmail.com")
        self.assertEqual(self.new_user.username, "dev Sarah")
        self.assertEqual(self.new_user.password, "@#saR!aH09")


    def test_create_new_account(self):
        """
        test_create_new_account test case to test if the new user object is
        saved into the user list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


    def tearDown(self):
        """
        teardown method that does clean up after each test case has run
        """
        User.user_list = []


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_user_exists(self):
        """
        test_check_user_exists to test if a user exists or not
        """
        self.new_user.save_user()
        test_user = User("Mary Jane","mj@gmail.com","May-Jay","%^Mjay@23")
        test_user.save_user()
        user_exists = User.user_exists("May-Jay")
        self.assertTrue(user_exists)


    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by user and display information
        '''

        self.new_user.save_user()
        test_user = User("Mary Jane","mj@gmail.com","May-Jay","%^Mjay@23")
        test_user.save_user()
        found_user = User.find_by_username("May-Jay")
        self.assertEqual(found_user.password,test_user.password


if __name__ == "__main__":
    unittest.main()