import random

class Credential:
    """
    class that generates new instances of user credentials
    """
    def __init__(self, accountName, email, username, password):
        self.accountName = accountName
        self.email = email
        self.username = username
        self.password = password
    
    cred_list = []


    def save_cred(self):
        """
        save_cred method saves user object into cred_list
        """
        Credential.cred_list.append(self)



    @classmethod
    def cred_exists(cls,accountName):        
        """
        check_profile_exist method checks if there is another matching or similar profile
        Args:
            profile to search if it exists
        Returns:
            Boolean: True or false depending if the profile exists
        """
        
        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return True
            else:
                return False 

    
    def delete_cred(self):
        """
        delete_profile method that deletes a particular profile
        """
        Credential.cred_list.remove(self)


    @classmethod
    def display_accounts(cls):
        """
        method that returns the cred list
        """
        return cls.cred_list
 

    @classmethod
    def find_by_accountName(cls,accountName):
        """
        Method that takes in an account name and returns the credentials that match that account name.
        Args:
            accountName: Account name to search for
        Returns :
            Full credentials that matches the accountName.
        """

        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return cred

    @classmethod
    def gen_password(cls,username):
        """
        generate_random_password method that returns a randomly generated password
        Args:
            length: The actual length of the password that is to be generated
        """
        letters = username[1:4]
        num1 = str(random.randint(0,9))
        num2 = str(random.randint(9,16))
        gen_pass = "!"+ num1 + letters + num2 + "$" + letters.upper()
        return gen_pass




