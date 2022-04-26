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