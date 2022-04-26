import unittest

from users import User

class test_users(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("waimina","1234567")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
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

        user_exists = User.user_exists("waimina")

        self.assertTrue(user_exists)
      
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        self.new_user.save_user()
        test_user = User("waimina","1234567") # new contact
        test_user.save_user()

        found_user = User.find_by_username("waimina")

        self.assertEqual(found_user.username,test_user.username)
 
    def test_display_all_user(self):
        '''
        method that returns a list of all user saved
        '''

        self.assertEqual(User.display_user(),User.user_list)

    
if __name__=='__main__':
        unittest.main()
    
  