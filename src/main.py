from users import UserManager
from seats import SeatManager
from storage import load_users, save_users, load_seats, save_seats

USERS_FILE = "data/users.json"
SEATS_FILE = "data/seats.json"


def show_menu():
    print("\n============================")
    print("     SEAT MANAGER CLI     ")
    print("============================")
    print("1. Create User")
    print("2. List Users")
    print("3. List Seats")
    print("4. Allocate Seat")
    print("5. Release Seat")
    print("6. Save & Exit")
    print("0. Exit Without Saving")
    print("----------------------------")


def main():
    users_data = load_users(USERS_FILE)
    seats_data = load_seats(SEATS_FILE)

    user_mgr = UserManager(users_data)
    seat_mgr = SeatManager(seats_data)

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter user name: ").strip()
            email = input("Enter email: ").strip()

            if name == "":
                print("Name cannot be empty.")
            else:
                uid = user_mgr.create_user(name, email)
            if uid is not None:
                print("User created with ID:", uid)
            else:
                print("User not created due to invalid email.")

        elif choice == "2":

            print("\n--- User List ---")
            all_users = user_mgr.list_users()
            if len(all_users) == 0:
                print("No users found.")
            else:
                for u in all_users:
                    email = u.get("email")
                    if email:
                        print(f"{u['id']} - {u['name']}  <{email}>")
                    else:
                        print(f"{u['id']} - {u['name']}  <no-email>")


        elif choice == "3":
            print("\n--- Seat Status ---")
            seats = seat_mgr.list_seats()

            for sid, occ in seats.items():
                if occ is None:
                    print(f"Seat {sid}: Empty")
                else:
                    user = user_mgr.find_user(occ)
                    if user:
                        print(f"Seat {sid}: {user['name']} ({occ})")
                    else:
                        print(f"Seat {sid}: {occ}")

        elif choice == "4":
            try:
                sid = int(input("Enter seat ID: "))
            except ValueError:
                print("Invalid seat number!")
                continue

            uid = input("Enter user ID: ").strip()

            ok = seat_mgr.allocate(sid, uid, user_mgr)
            if ok:
                print("Seat allocated successfully.")
            else:
                print("Failed to allocate seat. Check seat or user ID.")

        elif choice == "5":
            try:
                sid = int(input("Enter seat ID to release: "))
            except ValueError:
                print("Invalid seat number!")
                continue

            ok = seat_mgr.release(sid)
            if ok:
                print("Seat released successfully.")
            else:
                print("Failed to release seat (maybe it was already empty).")

        elif choice == "6":
            print("Saving data...")
            save_users(USERS_FILE, user_mgr.users)
            save_seats(SEATS_FILE, seat_mgr.to_dict())
            print("Data saved. Goodbye!")
            break

        elif choice == "0":
            print("Exiting without saving...")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
