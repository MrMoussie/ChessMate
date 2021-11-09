import unittest, sys

sys.path.append("../Chess")
import Leaderboard

sys.path.append("../SQL")
import Connect, Account, Queries

class LeaderboardTest(unittest.TestCase):

    def test_getLeaderboard(self):
        self.assertIsNone(Leaderboard.getLeaderboard())

        Connect.connect()
        Connect.setupDB()

        self.assertIsNotNone(Leaderboard.getLeaderboard())

        Connect.close()

    def test_updateElo_getElo(self):
        Connect.connect()
        Connect.setupDB()

        cred = "test"
        Account.register(cred, cred, cred)
        Leaderboard.updateElo(cred, 100)
        self.assertEqual(Leaderboard.getElo(cred), 100)

        Connect.close()

    def test_addElo(self):
        Connect.connect()
        Connect.setupDB()

        cred = "test"
        Account.register(cred, cred, cred)
        current = Leaderboard.getElo(cred)
        Leaderboard.addElo(cred, 100)
        self.assertEqual(Leaderboard.getElo(cred), current + 100)

        Connect.close()

    def test_addPoints(self):
        Connect.connect()
        Connect.setupDB()

        cred = "test"
        Account.register(cred, cred, cred)
        current = Queries.getSQuery("SELECT missionPoints FROM leaderboard WHERE name = %s", cred)
        Leaderboard.addPoints(cred, 100)
        new = Queries.getSQuery("SELECT missionPoints FROM leaderboard WHERE name = %s", cred)
        self.assertEqual(new, current + 100)

        Connect.close()

    def test_incrementWins(self):
        Connect.connect()
        Connect.setupDB()

        cred = "test"
        Account.register(cred, cred, cred)
        current = Queries.getSQuery("SELECT wins FROM leaderboard WHERE name = %s", cred)
        Leaderboard.incrementWins(cred)
        new = Queries.getSQuery("SELECT wins FROM leaderboard WHERE name = %s", cred)
        self.assertEqual(new, current + 1)

        Connect.close()

    def test_incrementLoss(self):
        Connect.connect()
        Connect.setupDB()

        cred = "test"
        Account.register(cred, cred, cred)
        current = Queries.getSQuery("SELECT loss FROM leaderboard WHERE name = %s", cred)
        Leaderboard.incrementLoss(cred)
        new = Queries.getSQuery("SELECT loss FROM leaderboard WHERE name = %s", cred)
        self.assertEqual(new, current + 1)

        Connect.close()