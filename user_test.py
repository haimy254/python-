import unittest

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
      
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("waimina","1234567") # new contact
        test_user.save_user()

        found_user = User.find_by_number("0711223344")

        self.assertEqual(found_user.email,test_user.email)
 
    
    
if __name__=='__main__':
        unittest.main()
    
  