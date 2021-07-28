from adapters.storage import Storage
from entities.user import User

class UserUseCase:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get_user(self, user_id):
        return self.storage.get_user(user_id)

    def create_user(self, user: User):
        return self.storage.create_user(user)

    def update_user(self, user_id: int, user: User):
        return self.storage.update_user(user_id, user)

    def delete_user(self, user_id):
        return self.delete_user(user_id)

