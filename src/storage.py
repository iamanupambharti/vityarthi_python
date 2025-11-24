import json
import os


def load_users(path):
    if not os.path.exists(path):
        print("Users file not found. Starting with an empty list.")
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Warning: users.json doesn't contain a list.")
                return []
    except Exception as e:
        print("Error loading users:", e)
        return []


def save_users(path, users):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(users, f, indent=2)
    except Exception as e:
        print("Error saving users:", e)


def load_seats(path):
    if not os.path.exists(path):
        print("Seats file not found. Using default seat setup.")
        return {
            "total_seats": 10,
            "seats": {str(i): None for i in range(1, 11)}
        }

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print("Error loading seats:", e)

        return {
            "total_seats": 10,
            "seats": {str(i): None for i in range(1, 11)}
        }


def save_seats(path, seats_data):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(seats_data, f, indent=2)
    except Exception as e:
        print("Error saving seats:", e)
