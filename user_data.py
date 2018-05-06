class User:
    """
    Class that generates new instances of users
    """
    def __init__(self,fullname, email, username, password):
        
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
    
    user_list = []


    def save_user(self):
        """
        save_user method saves user object into user_list
        """
        User.user_list.append(self)


    @classmethod
    def user_exists(cls, username):
        """
        Method that checks if a user exists in the user list.
        Args:
        username: username to search if the user exists
        Returns :
        Boolean: True or false depending if the user exists 
        """
        for user in cls.user_list:
            if user.username == username:
                return True
            else:
                return False



    @classmethod
    def find_by_username(cls,username):
        """
        find_user method that checks if a username already exists
        """
        for user in cls.user_list:
            if user.username == username:
                return user
            else:
                return 0  





    