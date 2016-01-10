import socket
'''
List the services from a range of ports entered by the user
'''
# Ask for port ranges
while True:
    try:
        low = int(input("Enter low port number[0]: "))
    except ValueError:
        low = 0
    try:
        high = int(input("Enter high port number[65535]: "))
    except ValueError:
        high = 65535
    if high >= low:
        break   
    print("invalid entry")
# Print the services
for i in range(low, high+1):
    try:
        service = socket.getservbyport(i)
    except OSError:
        continue
    print("Service for port {0} is {1}".format(i, service))
