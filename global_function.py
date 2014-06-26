import ConfigParser


def get_config(section, conf_name):
	global config 
	config = ConfigParser.ConfigParser()
	config.read("conf/config.ini")
	conf = config.get(section, conf_name)
	return conf

def set_config(section, key, value):
	config.set(section, key, value)
	config.write(open("conf/config.ini", "w"))

TAOBAO_API = get_config("taobaoapi", "taobao_api")
IP_START = get_config("position", "ip")
IP_END = get_config("ip_range", "ip_end")
