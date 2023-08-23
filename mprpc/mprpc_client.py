from mprpc import RPCClient
client = RPCClient('192.168.10.208', 6000)
print( client.call('sum', 1, 2))
print( client.call('multply', 1, 2))