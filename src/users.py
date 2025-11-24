import uuid
class UserManager:
    def __init__(self, initial_data=None):
        if initial_data is None:
            initial_data = []
        self.users = initial_data

    def create_user(self, name):
        # short id using uuid
        user_id = str(uuid.uuid4())[:8]
        user = {
            "id": user_id,
            "name": name
        }
        self.users.append(user)
        return user_id

    def list_users(self):
         return self.users

    def find_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
