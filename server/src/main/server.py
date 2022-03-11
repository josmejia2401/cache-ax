import socketserver
import sys
from .request import CacheRequestHandler
from .logger import getLogger
from .task import BackgroundTasks

class CacheServer(socketserver.ThreadingMixIn, socketserver.TCPServer):

    def __init__(self, server_address, handler_class=CacheRequestHandler,):
        self.logger = getLogger('CacheServer')
        self.task = BackgroundTasks()
        self.task.start()
        socketserver.TCPServer.__init__(self, server_address, handler_class)

    def server_activate(self):
        self.logger.debug('server_activate')
        socketserver.TCPServer.server_activate(self)
        return

    def serve_forever(self, poll_interval=0.5):
        self.logger.debug('waiting for request')
        socketserver.TCPServer.serve_forever(self, poll_interval)
        return

    def handle_request(self):
        return socketserver.TCPServer.handle_request(self)

    def verify_request(self, request, client_address):
        return socketserver.TCPServer.verify_request(self, request, client_address,)

    def process_request(self, request, client_address):
        return socketserver.TCPServer.process_request(self, request, client_address,)

    def server_close(self):
        return socketserver.TCPServer.server_close(self)

    def finish_request(self, request, client_address):
        return socketserver.TCPServer.finish_request(self, request, client_address,)

    def close_request(self, request_address):
        return socketserver.TCPServer.close_request(self, request_address,)

    def shutdown(self):
        if self.task.is_alive() == True:
            self.task.stop()
        self.logger.debug('shutdown server')
        return socketserver.TCPServer.shutdown(self)


if __name__ == '__main__':
    try:
        pass
    except KeyboardInterrupt as e:
        sys.exit(0)
