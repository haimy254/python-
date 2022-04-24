from collections import UserString
from os import uname
import unittest
from main import users

class testAccount(unittest.TestCase):
   def setUp(self):
       self.new_user=users("waimina", "1234567")
       
def __init__(self):
         self.assertEqual(self.new_user.username,"waimana")
         self.assertEqual(self.new_user.paasword,"1234567")
      
    

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
