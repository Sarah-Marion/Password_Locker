import unittest
import pyperclip
from credential import Credential

class credential_test(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_profile = Credential ("github", "Sarah", "devsarahmarion@gmail.com", "password")


    def test_init(self):
        """
        test init to test if the object is initialized properly
        """    
        self.assertTrue(self.new_profile.profile_name, "github")
        self.assertTrue(self.new_profile.profile_username, "Sarah")
        self.assertTrue(self.new_profile.profile_email,"devsarahmarion@gmail.com")
        self.assertTrue(self.new_profile.profile_password)


if __name__ == "__main__":
    unittest.main()
