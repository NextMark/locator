#!env/bin
import socket, struct
import global_function as func
import urllib2
import json
import time

FILE = open("data/ip_lib.txt", "w")

def ip_to_long(ip):
	"""
    	Convert an IP string to long
    	"""
    	packedIP = socket.inet_aton(ip)
    	return struct.unpack("!L", packedIP)[0]

def long_to_ip(long_ip):
	"""
    	Convert an Long to ip
    	"""
	return socket.inet_ntoa(struct.pack('!L', long_ip))

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
    	subvalue = value["data"]
    	location_info = ""
    	for subkey in subvalue:
		 location_info = "%s%s:%s|" % (location_info,subkey, subvalue[subkey])
	write_to_file(location_info + "\n")
	print location_info

def write_to_file(location_info):
	location_info = location_info.encode('gb2312')
	FILE.write(location_info)

def main():
	api = func.TAOBAO_API
    	ip_range = [ip_to_long(func.IP_START), ip_to_long(func.IP_END)]
    	for long_ip in xrange(ip_range[0], ip_range[1]):
    		position_ip = long_to_ip(long_ip)
    		func.set_config("position", "ip", position_ip)
    		time.sleep(0.1)
    		parse_json(request_url(get_location(api, long_ip)))

def end():
	FILE.close()

if __name__ == '__main__':
	main()
	end()
