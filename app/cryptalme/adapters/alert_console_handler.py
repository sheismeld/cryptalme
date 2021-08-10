from abc import ABC, abstractmethod
from typing import Optional, Callable, List, Any
from redis import Redis
from redis.client import PubSubWorkerThread, StrictRedis
from cryptalme.adapters.pub_sub_handler import PubSubHandler
from cryptalme.entities.alert import Alert


"""
    Singleton pettern for RedisCache to restrict instanciation to only one.
    Stactic variable are so implemented.
"""
class RedisCache:
    _instance: Optional[Redis] = None

    @staticmethod
    def get_instance() -> Redis:
        if RedisCache._instance is None:
            RedisCache._instance = StrictRedis(host='localhost', port=6379, password="redispass")
        return RedisCache._instance


class RedisPubSubHandler(PubSubHandler):
    def __init__(self, instance: Redis):
        self.instance = instance
        self.pubsub = self.instance.pubsub()
        self.thread: Optional[PubSubWorkerThread] = None

    def subscribe(self, channel: str, func: Callable):
        print("subscribe ok")
        self.pubsub.subscribe(**{channel: func})
        self.thread = self.pubsub.run_in_thread(sleep_time=0.01)

    def unsubscribe(self, channel):
        self.pubsub.unsubscribe(channel)
        self.thread.stop()


class NotifierStrategy(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass


class ConsoleNotifier(NotifierStrategy):
    @staticmethod
    def execute(alert: Alert):
        msg = "Alert: the BTC is {} {}".format(alert.alert_type, alert.stop_price)
        print(msg)


class AlertSubscriber:
    def __init__(self, alert: Alert, handler: PubSubHandler):
        self.alert = alert
        self.handler = handler

    def register(self):
        self.handler.subscribe("rate", self.on_message)

    def unregister(self):
        self.handler.unsubscribe("rate")

    def on_message(self, msg):
        price = float(msg.get("data"))
        under: bool = self.alert.alert_type == 'UNDER' and price <= self.alert.stop_price
        above: bool = self.alert.alert_type == 'ABOVE' and price >= self.alert.stop_price
        if under or above:
            self.notify_all()
            self.unregister()

    def notify_all(self):
        ConsoleNotifier.execute(self.alert)
