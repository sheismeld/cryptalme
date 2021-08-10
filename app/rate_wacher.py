#!/usr/bin/env python
import json
from typing import List

import websocket

from cryptalme.adapters.alert_console_handler import RedisCache

try:
    import thread
except ImportError:
    import _thread as thread
import time

redis = RedisCache.get_instance()


class RateWatcher:

    def __init__(self, api_key, assets=None, quote="USD", enable_trace=False):
        self.API_KEY = api_key
        self.assets: List[str] = assets
        self.quote = quote
        self.enable_trace = enable_trace

    def on_message(self, ws, message):
        message = json.loads(message)

        if message.get("asset_id_quote") == self.quote:
            print(message)
            redis.publish("rate", message.get("rate"))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            greeting = {
                "type": "hello",
                "apikey": self.API_KEY,
                "heartbeat": False,
                "subscribe_data_type": ["exrate"],
                "subscribe_filter_asset_id": self.assets,
                "asset_id_quote": "USD"
            }
            ws.send(json.dumps(greeting))

        thread.start_new_thread(run, ())

    def launch(self):
        websocket.enableTrace(self.enable_trace)
        ws = websocket.WebSocketApp(
            "wss://ws-sandbox.coinapi.io/v1/",
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open,
        )
        ws.run_forever()


if __name__ == "__main__":
    rate_watcher = RateWatcher(
        api_key="253A1294-1FF1-4137-9880-5BC0D041AE5F",
        assets=["BTC"],
    )
    rate_watcher.launch()

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()
