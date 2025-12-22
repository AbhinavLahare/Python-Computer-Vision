import asyncio
import json
import websockets

class WebSocketClient:
    def __init__(self, uri="ws://localhost:8765"):
        self.uri = uri

    async def send_event(self, event):
        async with websockets.connect(self.uri) as ws:
            await ws.send(json.dumps(event))
