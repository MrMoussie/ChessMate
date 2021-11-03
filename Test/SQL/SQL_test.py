import sys, unittest

sys.path.append("../../src/SQL")
import Account, Connect, Queries

# CONNECT
class TestConnect(unittest.TestCase):
    def test_connectExists_getSQL_close(self):
        self.assertFalse(Connect.connectExists())
        self.assertIsNone(Connect.getSQL())
        
        Connect.connect()
        self.assertTrue(Connect.connectExists())
        self.assertIsNotNone(Connect.getSQL())

        Connect.close()
        self.assertFalse(Connect.connectExists())
        self.assertIsNone(Connect.getSQL())

    def test_Database(self):
        Connect.connect()
        Connect.setupDB()

        try:
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
            self.assertIsNone(Queries.getSQuery(query, None))

            query = "SHOW TABLES IN ChessMate LIKE 'medium_missions';"
            self.assertIsNone(Queries.getSQuery(query, None))

            query = "SHOW TABLES IN ChessMate LIKE 'hard_missions';"
            self.assertIsNone(Queries.getSQuery(query, None))

            query = "SHOW TABLES IN ChessMate LIKE 'expert_missions';"
            self.assertIsNone(Queries.getSQuery(query, None))

            # This test deletes the whole database, use with discretion!
            # Connect.dropDB()

            # query = "SHOW DATABASES LIKE 'ChessMate';"
            # self.assertEqual(Queries.getSQuery(query, None), None)
        except Exception as e:
            print(e)
        finally:
            Connect.setupDB()
            Connect.close()

# ACCOUNT
class TestAccount(unittest.TestCase):
    def test_salt(self):
        self.assertIsNotNone(Account.generateSalt())
    
    def test_hash_init(self):
        password = salt = "1234"
        self.assertIsNotNone(Account.hash(password, salt))
        self.assertTrue(password not in Account.hash(password, salt))

    def test_register_delete_exists(self):
        Connect.connect()
        Connect.setupDB()

        try:
            username = password = email = "TEST"
            Account.register(username, email, password)
            query = "SELECT COUNT(*) FROM {0}.login WHERE name = %s;".format(Connect.db)
            self.assertEqual(Queries.getSQuery(query, username), 1)
            self.assertTrue(Account.emailExists(email))
            self.assertTrue(Account.accountExists(username))

            self.assertTrue(Account.delete(username, password))
            self.assertFalse(Account.delete(username, password))
            self.assertFalse(Account.accountExists(username))
            self.assertFalse(Account.emailExists(email))

        except Exception as e:
            print(e)
        finally:
            Connect.close()
    
    def test_login(self):
        Connect.connect()
        Connect.setupDB()
        
        try:
            username = password = email = "TEST"
            Account.register(username, email, password)

            self.assertTrue(Account.login(username, password))
            self.assertFalse(Account.login(username, username + password))
            self.assertFalse(Account.login(None, None))
            self.assertFalse(Account.login(username, None))
            self.assertFalse(Account.login(None, password))
        except Exception as e:
            print(e)
        finally:
            Account.delete(username, password)
            Connect.close()

# QUERIES
class TestQueries(unittest.TestCase):
    def test_getSQuery_init(self):
        self.assertIsNone(Queries.getSQuery(None, None))
        self.assertIsNone(Queries.getSQuery("", None))

    def test_doQuery_init(self):
        self.assertFalse(Queries.doQuery(None, None))
        self.assertFalse(Queries.doQuery("", None))

    # TO DO