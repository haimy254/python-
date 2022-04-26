import unittest #importing the unittest module 

from credentials import Credentials #importing the credentials class

class test_credentials(unittest.TestCase):
  
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials=Credentials("haimana","waimina","1234567")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account,"haimana")
        self.assertEqual(self.new_credentials.username,"waimina")
        self.assertEqual(self.new_credentials.password,"1234567")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        Credentials.credentials_list=[] 
        
    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials= Credentials("qare","uta","098765")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    
        
if __name__==('__main__'):
         unittest.main()   