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

    def test_Database(self):
        Connect.connect()
        Connect.setupDB()
        
        query = "SHOW DATABASES LIKE 'ChessMate';"
        self.assertEqual(Queries.getSQuery(query, None).decode('utf-8'), "ChessMate")

        query = "SHOW TABLES IN ChessMate LIKE 'easy_missions';"
        self.assertEqual(Queries.getSQuery(query, None).decode('utf-8'), "easy_missions")

        query = "SHOW TABLES IN ChessMate LIKE 'medium_missions';"
        self.assertEqual(Queries.getSQuery(query, None).decode('utf-8'), "medium_missions")
        
        query = "SHOW TABLES IN ChessMate LIKE 'hard_missions';"
        self.assertEqual(Queries.getSQuery(query, None).decode('utf-8'), "hard_missions")
        
        query = "SHOW TABLES IN ChessMate LIKE 'expert_missions';"
        self.assertEqual(Queries.getSQuery(query, None).decode('utf-8'), "expert_missions")

        Connect.dropMissions()
        
        query = "SHOW TABLES IN ChessMate LIKE 'easy_missions';"
        self.assertEqual(Queries.getSQuery(query, None), None)

        query = "SHOW TABLES IN ChessMate LIKE 'medium_missions';"
        self.assertEqual(Queries.getSQuery(query, None), None)

        query = "SHOW TABLES IN ChessMate LIKE 'hard_missions';"
        self.assertEqual(Queries.getSQuery(query, None), None)

        query = "SHOW TABLES IN ChessMate LIKE 'expert_missions';"
        self.assertEqual(Queries.getSQuery(query, None), None)

        Connect.dropDB()

        query = "SHOW DATABASES LIKE 'ChessMate';"
        self.assertEqual(Queries.getSQuery(query, None), None)

        Connect.setupDB()
        Connect.close()

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

    def test_doQuery_init(self):
        self.assertFalse(Queries.doQuery(None, None))
        self.assertFalse(Queries.doQuery("", None))