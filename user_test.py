
import unittest
# import pyperclip
from users import User

class test_users(unittest.TestCase):

    def setUp(self):
        self.new_user=User("waimina","1234567")

    def test_init(self):
        self.assertEqual(self.new_user.username,"waimina")
        self.assertEqual(self.new_user.password,"1234567")
        
    
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    
    
if __name__=='__main__':
        unittest.main()
    
  