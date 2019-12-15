import unittest
from account_class import user_account

class TestAccount(unittest.TestCase):

    def test_address_returns_error_when_there_is_no_at(self):
        with self.assertRaises(Exception):
            user1 = user_account('bryan','gunawan','bryanucl.com','bryanadg','password123')

    def test_names_returns_error_when_there_is_number(self):
        with self.assertRaises(Exception):
            user2 = user_account('bryan','5urn4m3','bryan@ucl.com','bryanadg','password123')

    def test_names_returns_error_when_too_long(self):
        with self.assertRaises(Exception):
            user3 = user_account('bryan','gunawan','bryan@ucl.com','verylongusername','password123')

if __name__ == "__main__":
    unittest.main()