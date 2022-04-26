import unittest

from credentials import Credentials

class test_credentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials=Credentials("haimana","waimina","1234567")

    def test_init(self):
        self.assertEqual(self.new_credentials.account,"haimana")
        self.assertEqual(self.new_credentials.username,"waimina")
        self.assertEqual(self.new_credentials.password,"1234567")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)