import unittest
from src.seats import SeatManager
from src.users import UserManager

class TestSeatManager(unittest.TestCase):
    def setUp(self):
        initial = {
            "total_seats": 5,
            "seats": {str(i): None for i in range(1, 6)}
        }
        self.sm = SeatManager(initial)
        self.um = UserManager([])
        self.uid = self.um.create_user("TestUser")

    def test_list_seats_initial(self):
        seats = self.sm.list_seats()
        self.assertEqual(len(seats), 5)
        self.assertTrue(all(v is None for v in seats.values()))
        print("Initial seat list OK")

    def test_allocate_success(self):
        ok = self.sm.allocate(1, self.uid, self.um)
        self.assertTrue(ok)
        self.assertEqual(self.sm.list_seats()[1], self.uid)
        print("Allocation succeeded for seat 1")

    def test_allocate_fail_when_taken(self):
        ok1 = self.sm.allocate(2, self.uid, self.um)
        self.assertTrue(ok1)
        ok2 = self.sm.allocate(2, self.uid, self.um)
        self.assertFalse(ok2)
        print("Double allocation prevented")

    def test_release_success(self):
        self.sm.allocate(3, self.uid, self.um)
        ok = self.sm.release(3)
        self.assertTrue(ok)
        self.assertIsNone(self.sm.list_seats()[3])
        print("Release succeeded for seat 3")

    def test_release_fail_invalid(self):
        ok = self.sm.release(99)
        self.assertFalse(ok)
        print("Release invalid seat handled")

if __name__ == "__main__":
    unittest.main()
