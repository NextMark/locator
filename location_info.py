class LocationInfo(object):
    """docstring for LocationInfo"""
    country
    country_id
    area
    area_id
    region
    region_id
    city
    city_id
    county
    county_id
    isp
    isp_id
    ip

    def __init__(self, arg):
        super(LocationInfo, self).__init__()
        self.arg = arg

    def __init__(self, country , country_id, area, area_id, region, region_id, city, city_id, county, county_id, isp, isp_id, ip):
        self.country = country
        self.country_id = country_id
        self.area = area
        self.area_id = area_id
        self.region = region
        self.region_id = region_id
        self.city = city
        self.city_id = city_id
        self.county = county
        self.county_id = county_id
        self.isp = isp
        self.isp_id = isp_id
        self.ip = ip
