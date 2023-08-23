from gevent.server import StreamServer
from gevent.pool import Pool
from mprpc import RPCServer
import os
class SumServer(RPCServer):
    def sum(self, x, y):
        return x + y
    def multply(self, x, y):
        return x * y



def startserver(host='0.0.0.0', port=12345):
    # Make sure the socket does not already exist    
    try:
        port_kill = "fuser -k " + str(port) + "/tcp"
        os.system(port_kill)
    except OSError:
        raise        

    try:            
        connections = Pool(1000)
        server = StreamServer((host,port),SumServer(),spawn=connections)            
        print("MpRPC server Started.")
        server.serve_forever()
    except ConnectionResetError as e:
        print("startserver: {}".format(e))

startserver('192.168.10.208', 6000)