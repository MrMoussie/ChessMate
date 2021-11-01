import sys, unittest

sys.path.append("../../src/SQL")
import Account, Connect, Queries

# CONNECT
class TestConnect(unittest.TestCase):
    def test_connectExists_getSQL_close(self):
        self.assertFalse(Connect.connectExists())
        self.assertEqual(Connect.getSQL(), None)
        
        Connect.connect()
        self.assertTrue(Connect.connectExists())
        self.assertNotEqual(Connect.getSQL(), None)

        Connect.close()
        self.assertFalse(Connect.connectExists())
        self.assertEqual(Connect.getSQL(), None)


# ACCOUNT
class TestAccount(unittest.TestCase):
    def test_salt(self):
        self.assertNotEqual(Account.generateSalt(), None)
    
    def test_hash(self):
        password = salt = "1234"
        self.assertNotEqual(Account.hash(password, salt), None)
        self.assertTrue(password not in Account.hash(password, salt))