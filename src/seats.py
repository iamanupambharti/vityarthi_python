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
