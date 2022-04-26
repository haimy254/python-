from users import User
class Credentials:
    '''
    class that generates new instaces of user credentials of their accounts
    '''
    
    pass
    credentials_list=[]   
    
    
    def __init__(self,account,username,password):
            self.account=account
            self.username=username
            self.password=password
    
    def save_credentials(self):
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a account and returns a credentials that matches that account.

        Args:
            account: account to search for
        Returns :
            credentials of person that matches the account.
        '''

        for credentials in cls.credentials_list:
            if credentials.account == account:
                return credentials
            
    @classmethod
    def credentials_exists(cls,account):
      '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            account: accoount to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists      
             '''

      for credentials in cls.credentials_list:
          if credentials.account==account:
              return True
          
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list