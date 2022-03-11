import sys
from src.main.request import CacheRequestHandler
from src.main.server import CacheServer

if __name__ == '__main__':
    address = ('localhost', 63456)  # let the kernel assign a port
    server = CacheServer(address, CacheRequestHandler)
    try:
        #address = ('localhost', 0)  # let the kernel assign a port
        ip, port = server.server_address  # what port was assigned?
        print(ip, port)
        server.serve_forever()
        # Start the server in a thread
        #t = threading.Thread(target=server.serve_forever)
        #t.setDaemon(False)  # don't hang on exit
        #t.start()
        #
        #set(ip, port)
        #get(ip, port)
        #remove(ip, port)
        # Clean up
    except KeyboardInterrupt:
        server.shutdown()
        server.socket.close()
        sys.exit(0) 
    finally:
        server.shutdown()
        server.socket.close()
