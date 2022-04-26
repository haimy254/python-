class User:
   
    pass
    user_list=[]   
    
    
        
    def __init__(self,username,password):
            self.username=username
            self.password=password
    
    def save_user(self):
        User.user_list.append(self)
        
    def delete_user(self):
        User.user_list.remove(self)
            
    @classmethod
    def user_exists(cls,password):
      '''
        Method that checks if a user exists from the user list.
        Args:
            password: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists      
             '''

      for user in cls.user_list:
          if user.password==password:
              return True
          
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a account and returns a user that matches that account.

        Args:
            account: account to search for
        Returns :
            User of person that matches the account.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user

                  
          
        
