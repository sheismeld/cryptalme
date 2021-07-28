from adapters.storage import Storage
from entities.alert import Alert
from entities.user import User
from models import UserModel, AlertModel


class DjangoStorage(Storage):
    def get_user(self, user_id: int):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist as e:
            user = None
        return user

    def create_user(self, user: User):
        new_user = UserModel.create_simple_user(user)
        return new_user.to_entity()

    def update_user(self, user_id: int, user: User):
        updated_user = UserModel.update_simple_user(user_id, user)
        return updated_user.to_entity()

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        return user.delete()

    def get_alert(self, alert_id):
        try:
            alert = AlertModel.objects.get(pk=alert_id)
        except AlertModel.DoesNotExist as e:
            alert = None
        return alert

    def create_alert(self, user_id: int, alert: Alert):
        alert = AlertModel.from_entity(alert)
        alert.save()
        return alert.to_entity()

    def update_alert(self, alert_id: int, alert_type: str, stop_price: int):
        alert = self.get_alert(alert_id=alert_id)
        alert.alert_type = alert_type
        alert.stop_price = stop_price
        alert.save()
        return alert

    def delete_alert(self, alert_id: int):
        alert = self.get_alert(alert_id=alert_id)
        return alert.delete()
