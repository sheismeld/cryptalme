from enum import Enum


class AlertType(Enum):
    ABOVE = 'ABOVE'
    UNDER = 'UNDER'


class Alert:
    def __init__(self, stop_price: float, alert_type: str, id=None,):
        self.alert_type = alert_type
        self.stop_price = stop_price
        self.id = id
