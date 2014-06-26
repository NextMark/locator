import ConfigParser


def get_config(section, conf_name):
    config = ConfigParser.ConfigParser()
    config.read("conf/config.ini")
    conf = config.get(section, conf_name)
    return conf

TAOBAO_API = get_config("taobaoapi", "taobao_api")
IP_START = get_config("ip_range", "ip_start")
IP_END = get_config("ip_range", "ip_end")
