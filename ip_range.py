#!env/bin

import os
import sys
import socket, struct
import location_info
import global_function as func
import urllib2
import json
import types

duan = "------------------------------------fengefu"
def ip_to_long(ip):
    """
    Convert an IP string to long
    """
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L", packedIP)[0]


def long_to_ip(long):
	"""
    	Convert an Long to ip
    	"""
	return socket.inet_ntoa(struct.pack('!L', long))

def get_location(api, long_ip):
	string_ip = long_to_ip(long_ip)
	url = '%s%s' % (api, string_ip)
	return url

def request_url(url):
	try:
		data = urllib2.urlopen(url).read()
		return data
	except Exception,e:
		print e

def parse_json(data):
	value = json.loads(data)
	rootlist = value.keys()
	print rootlist
	print duan  
	for rootkey in rootlist:
		print rootkey
    	print duan  
    	subvalue = value[rootkey]  
    	print subvalue  
    	print duan  
    	for subkey in subvalue:  
		print subkey,subvalue[subkey]

def main():
    api = func.TAOBAO_API
    ip_range = [ip_to_long(func.IP_START), ip_to_long(func.IP_END)]
    for long_ip in xrange(ip_range[0], ip_range[1]):
    	parse_json(request_url(get_location(api, long_ip)))

if __name__ == '__main__':
    main()
