class LocationInfo(object):

    """docstring for LocationInfo"""
    country = ''
    province = ''
    city = ''

    def __init__(self, arg):
        super(LocationInfo, self).__init__()
        self.arg = arg

    def __init__(self, country, province, city):
        self.country = country
        self.province = province
        self.city = city
