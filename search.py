import socket
#allows you to create sockets in Python, which is necessary for establishing network connections

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creates a my_socket socket object, specifying AF_INET as the address family (IPv4 addresses) and SOCK_STREAM as the socket type (use TCP for communication)
uri = "000.0.0.0" 
#IP target
for port in range(65536):
    #which iterates over all possible ports, from 0 to 65535. This covers all possible TCP ports
    destination = (uri, port)
    #At each iteration of the loop, this line defines the destination variable as a tuple containing the IP address uri and the port number port.
    connection_result = my_socket.connect_ex(destination)
    #connect_ex method of the my_socket socket object to attempt to connect to the address and port specified in destination. The connect_ex method returns an error code if the connection fails, otherwise it returns 0
    print("Le port", port, "a répondu", connection_result)
    #displays the result of the connection attempt for each port. If the port is open, connection_result will be 0, otherwise it will display an error code corresponding to the connection problem
my_socket.close()
#close the socket once all connections have been tried