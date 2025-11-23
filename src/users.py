# src/users.py
"""
Stage 2: Added create_user() method.
Using simple dicts for storing user data.
"""

import uuid  # using uuid for simple unique ids (beginner friendly)

class UserManager:
    def __init__(self, initial_data=None):
        # keep user data in a list of dicts
        if initial_data is None:
            initial_data = []

        self.users = initial_data

    def create_user(self, name):
        """
        Create a user with a short ID.
        For now, just keep it simple: id + name.
        """
        # making the id short so it is easy to type
        user_id = str(uuid.uuid4())[:8]

        user = {
            "id": user
