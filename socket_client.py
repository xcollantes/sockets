"""Client using websocket-client."""

# https://websocket-client.readthedocs.io/en/latest/examples.html

import websocket

SERVER_HOST = "ws://127.0.0.1:65432"


def one_off():
    ws = websocket.WebSocket()

    ws.connect(SERVER_HOST)
    ws.send("THIS IS MSG")
    print(ws.recv())
    ws.close()


def web_app():
    ws = websocket.WebSocketApp(SERVER_HOST, on_message=on_message)
    ws.run_forever()


def on_message(message):
    print(message)


if __name__ == "__main__":
    websocket.enableTrace(True)  # For logging
    one_off()
