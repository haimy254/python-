
import unittest
from users import User

class TestUser(unittest.TestCase):
   def setUp(self):
       self.new_user=User("waimina", "1234567")
       
def __init__(self):
         self.assertEqual(self.new_user.username,"waimana")
         self.assertEqual(self.new_user.password,"1234567")
      
      
    
def test_self_user(self):
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
    
def setUp(self):
    self.new_user=User("haimana", "987456")
    
def test_inti(self):
    self.assertEqual(self.new_user.username,"haimana")
    self.assertEqual(self.new_user.password,"987456")
    
if __name__=='__main__':
    unittest.main()
    
# user_have_an_account=input("do you have an existing account? ")


# if(user_have_an_account):
#   def test_display_all_user(self):
#       self.assertEqual(Account.displpay_users())
#     #if user has an account 
#     #1) Receive credentials (username and password)
#     #2) Check credentials
#     #3) view your credentials
#     #4) you can delete 
# else:
#     #if uuser doesn't have an account 
#     #create an account 
#     # save the account 
