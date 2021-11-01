import sys
import unittest

sys.path.append("../../src/SQL")
import Account, Connect, Queries

# ACCOUNT

class TestAccount(unittest.TestCase):
    def test_salt(self):
        self.assertNotEqual(Account.generateSalt(), None)
    
    def test_hash(self):
        password = salt = "1234"
        # TO DO
        
        