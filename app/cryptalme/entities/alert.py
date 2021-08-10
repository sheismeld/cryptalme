from enum import Enum
from typing import List

from cryptalme.entities.user import User


class AlertType(Enum):
    ABOVE = 'ABOVE'
    UNDER = 'UNDER'


class Alert:
    def __init__(self, stop_price: float, alert_type: str, user: User, alert_id: int = None):
        self.alert_type = alert_type
        self.stop_price = stop_price
        self.id = alert_id
        self.user: User = user
        self.handlers: List[int] = list()
