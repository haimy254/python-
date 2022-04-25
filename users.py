class User:
   
    pass
    user_list=[]   
    
    
        
    def __init__(self,username,password):
            self.username=username
            self.password=password
    
    def save_user(self):
        User.user_listappend(self)
            
           
            
# def create_user(username,password):
         
   
        
