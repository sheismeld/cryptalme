from cryptalme.adapters.storage import Storage
from cryptalme.entities.alert import Alert


class AlertUseCase:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get_alert(self, alert_id):
        return self.storage.get_alert(alert_id)

    def create_alert(self, alert: Alert):
        return self.storage.create_alert(alert)

    def update_alert(self, alert_id: int, alert: Alert):
        return self.storage.update_alert(alert_id, alert)

    def delete_alert(self, alert_id):
        return self.delete_alert(alert_id)
