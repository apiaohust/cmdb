from django.test import TestCase
import urllib
import urllib2
import json


# Create your tests here.
class DateCollector():
    def getServerDate(self):
        url = "http://127.0.0.1:8655/getdata"
        req = urllib2.urlopen(url)
        test = req.read()
        result = json.loads(test)
        print result.get('data').get('serverinfo')
        sysinfo =result.get('data').get('sysinfo')
        admin_ip = result.get('data').get('ip_address')
        server_ip = result.get('data').get('ip_address')


if __name__ == '__main__':
    test = DateCollector()
    test.getServerDate()
