#  RPC connection between  mprpc Server & mprpc Client /Rpclibc++ Client
 
## Features

- Supports addition and multiplication operations.
- Utilizes the `gevent` library for asynchronous networking.
- Uses the `mprpc` package for MessagePack-based RPC.
- Uses the `rpclibC++` package for MessagePack-based RPC.

## Install required packages
------
				pip3 install gevent mprpc
## Installation

1. Clone the repository:
   
   				https://github.com/MMuneebtahir/python-helper-utils.git
   ------

   				cd python-helper-utils

## MpRPC Server Example

This is an example of an MpRPC (MessagePack RPC) server implemented using the `gevent` library and the `mprpc` package. The server provides remote procedure calls for simple arithmetic operations.

### Usage
--------------------
You can run the server with the following command:

				python3 server.py

The server will start listening on the specified host and port. Make sure to configure the host and port according to your requirements.

### Available Operations
--------------------
sum(x, y): Returns the sum of two numbers.

multiply(x, y): Returns the product of two numbers.

### Configuration
-------------
You can configure the server's host and port by modifying the start-server function call in the server.py script.

				startserver(host='0.0.0.0', port=12345)

## MpRPC Client Example
This repository provides an example of an MpRPC (MessagePack RPC) client implemented using the `mprpc` package. The client communicates with a remote server to perform arithmetic operations.

### Usage
--------------------
You can use the following code snippet to create an MpRPC client and interact with the remote server:

## RPClib C++ Client Example

Replace '192.168.10.208' and 6000 with the appropriate host and port of the MpRPC server you want to connect to.

### Installation
--------------------
To run the client code, you need the RPC library. Make sure you have the library installed and configured properly.

### Building
--------------------
Compile the C++ code using your preferred compiler:

				g++ -o client client.cpp -lrpc

### Configuration

Ensure that the host and port specified in the `rpc::client` constructor match the configuration of your MpRPC server.


## Contributing
------------
Contributions are welcome! If you find any issues or want to improve the project, feel free to create a pull request.

## License
-------
This project is licensed under the MIT License - see the LICENSE file for details.


