import socketserver

class TCPHandler(socketserver.TCPServer):
    def handle(self):
        self.request

socketserver.TCPServer()
