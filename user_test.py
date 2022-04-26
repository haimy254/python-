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
    
    def tearDown(self):
        User.user_list=[]
        
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("haimy", "254")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
            
    def test_delete_user(self):
        self.new_user.save_user()
        test_user= User("haimy", "254")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
     
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("waimina", "1234567",) # new user
        test_user.save_user()

        user_exists = User.user_exists("1234567")

        self.assertTrue(user_exists)
      
      
    
    
if __name__=='__main__':
        unittest.main()
    
  