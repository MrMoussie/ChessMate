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
    
    def test_hash_init(self):
        password = salt = "1234"
        self.assertNotEqual(Account.hash(password, salt), None)
        self.assertTrue(password not in Account.hash(password, salt))

# QUERIES
class TestQueries(unittest.TestCase):
    def test_getSQuery_init(self):
        self.assertEqual(Queries.getSQuery(None, None), None)
        self.assertEqual(Queries.getSQuery("", None), None)
        self.assertEqual(Queries.getSQuery("DO", None), None)

    def test_doQuery_init(self):
        self.assertFalse(Queries.doQuery(None, None))
        self.assertFalse(Queries.doQuery("", None))
        self.assertFalse(Queries.doQuery("DO", None))

    def test_SQL(self):
        Connect.connect()

        # TO DO