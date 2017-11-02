#!/usr/bin/env python

import socket

def recv_until(conn, str):
	buf = ''
	while not str in buf:
		buf += conn.recv(1)
	return buf

def getValidSubnet(host):
	return '0.0.0.0/0'

def countHosts(subnet):
	sub_len = int(subnet.split('/')[1])
	return str(2**(32 - sub_len))

def isSubnetValid(subnet, host):
	sub_len = int(subnet.split('/')[1])
	host_ip = int(socket.inet_aton(host).encode('hex'),16)
	subnet_ip = int(socket.inet_aton(subnet.split('/')[0]).encode('hex'),16)

	count = 2**(32 - sub_len)

	return 'T' if (host_ip ^ subnet_ip < count) else 'F'
	
TCP_IP = 'hmif.cf'
#TCP_PORT = 8888
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

print recv_until(s, '\n')[:-1]

# Phase 1
for i in range(100):
#for i in range(1):
	buffer = recv_until(s, 'Host: ')
	print buffer,
	host = recv_until(s, '\n')[:-1]
	print host
	buffer = recv_until(s, 'Subnet: ')
	print buffer,
	ans = getValidSubnet(host)
	print ans + ' (' + str(i+1) + ')'
	s.send(ans + '\n')
print recv_until(s, '\n')[:-1]

# Phase 2
for i in range(100):
#for i in range(1):
	buffer = recv_until(s, 'Subnet: ')
	print buffer,
	subnet = recv_until(s, '\n')[:-1]
	print subnet
	buffer = recv_until(s, 'Number of Hosts: ')
	print buffer,
	ans = countHosts(subnet)
	print ans + ' (' + str(i+1) + ')'
	s.send(ans + '\n')
print recv_until(s, '\n')[:-1]

# Phase 3
for i in range(100):
#for i in range(1):
	buffer = recv_until(s, 'Subnet: ')
	print buffer,
	subnet = recv_until(s, '\n')[:-1]
	print subnet
	buffer = recv_until(s, 'Host: ')
	print buffer,
	host = recv_until(s, '\n')[:-1]
	print host
	ans = isSubnetValid(subnet, host)
	print ans + ' (' + str(i+1) + ')'
	s.send(ans + '\n')
print recv_until(s, '\n')[:-1]

s.close()