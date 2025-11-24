class SeatManager:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = {}

        self.total_seats = initial_data.get("total_seats", 10)

        raw_seats = initial_data.get("seats", {})

        self.seats = {}
        for key, value in raw_seats.items():
            try:
                seat_num = int(key)
                self.seats[seat_num] = value
            except ValueError:
                print("Warning: seat key not integer:", key)


    def list_seats(self):
        return self.seats

    def allocate(self, seat_id, user_id, user_mgr=None):

        if seat_id not in self.seats:
            return False

        if self.seats[seat_id] is not None:
            return False

        if user_mgr:
            if user_mgr.find_user(user_id) is None:
                return False

        self.seats[seat_id] = user_id
        return True

    def release(self, seat_id):
        if seat_id not in self.seats:
            return False

        if self.seats[seat_id] is None:
            return False

        self.seats[seat_id] = None
        return True

    def to_dict(self):
        return {
            "total_seats": self.total_seats,
            "seats": {str(k): self.seats[k] for k in self.seats}
        }
