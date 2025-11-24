import unittest
from src.users import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.um = UserManager([])

    def test_create_user_returns_id(self):
        uid = self.um.create_user("Alice")
        self.assertIsInstance(uid, str)
        self.assertEqual(len(uid), 8)
        print("Created user id:", uid)

    def test_list_and_find_user(self):
        uid = self.um.create_user("Bob")
        users = self.um.list_users()
        self.assertTrue(any(u["id"] == uid for u in users))

        found = self.um.find_user(uid)
        self.assertIsNotNone(found)
        self.assertEqual(found["name"], "Bob")
        print("Find user OK for:", uid)

if __name__ == "__main__":
    unittest.main()
