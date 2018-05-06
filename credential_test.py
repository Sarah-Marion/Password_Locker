import unittest
from credential import Credential
import pyperclip

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
        self.new_cred = Credential ("github", "devsarahmarion@gmail.com","dev-Sarahgh","@#saR!aH09gh")


    def test_init(self):
        """
        test init to test if the object is initialized properly
        """    
        self.assertEqual(self.new_cred.accountName, "github")
        self.assertEqual(self.new_cred.username, "Sarah")
        self.assertEqual(self.new_cred.email, "devsarahmarion@gmail.com")
        self.assertEqual(self.new_cred.password, "@#saR!aH09gh")


    def tearDown(self):
        """
        teardown method that does clean up after each test case has run
        """
        Credential.cred_list = []


    def test_save_cred(self):
        """
        test_save_cred test case to test if the cred object is saved into
         the cred list
        """
        self.new_cred.save_cred()
        self.assertEqual(len(Credential.cred_list), 1)


    def test_cred_exists(self):
        """
        test_profile_exist to check if there is another matching or similar profile
        """
        self.new_cred.save_cred()
        test_cred = Credential("github", "devsarahmarion@gmail.com","dev-Sarahgh","@#saR!aH09gh")    
        test_cred.save_cred()
        cred_exists = Credential.cred_exists("github")
        self.assertTrue(cred_exists)

  
    def test_find_cred_by_accountName(self):
        """
        test to check if we can find a user's credentials by accountName and display information
        """
        self.new_cred.save_cred()
        test_cred = Credential("github", "devsarahmarion@gmail.com","dev-Sarahgh","@#saR!aH09gh")
        test_cred.save_cred()
        found_cred = Credential.find_by_accountName("github")
        self.assertEqual(found_cred.accountName,test_cred.accountName)

    
    def test_display_all_credentials(self):
        """
        test to check if we can display all the accounts a user has
        """
        self.assertEqual(Credential.display_accounts(), Credential.cred_list)

    
    def test_delete_credentials(self):
        """
        test_delete_profile to test if a user can delete a specific profile
        """
        self.new_cred.save_cred()
        test_cred = Credential("github", "devsarahmarion@gmail.com","dev-Sarahgh","@#saR!aH09gh")
        test_cred.save_cred()
        self.new_cred.delete_cred()
        self.assertEqual(len(Credential.cred_list), 1)

    
    def test_gen_password(self):
        """
        test_gen_password to test if a user can generate a random password with a set length
        """
        self.new_cred.save_cred()
        test_cred = Credential("github", "devsarahmarion@gmail.com","dev-Sarahgh","")
        test_cred.password = Credential.gen_password("dev-Sarahgh")
        test_cred.save_cred()
        self.assertTrue(len(test_cred.password) > 2)
    

    # def test_copy_credentials(self):
    #     """
    #     test_copy_credentials to test if a user can copy an item to the clipboard
    #     """
    #     test_cred = Credential("github", "devsarahmarion@gmail.com","dev-Sarahgh")
    #     test_cred.password = Credential.copy_credentials("github")
    #     test_cred.save_cred()
    #     self.assertEqual(test_cred.password,pyperclip.paste()) 

if __name__ == "__main__":
    unittest.main()
