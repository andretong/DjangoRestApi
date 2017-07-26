'''
Created on 21-06-2017

@author: atong
'''
import requests

class GoogleMapClient(object):

    BASE_URL = 'https://maps.googleapis.com/maps/api/'
    API_KEY_GEOCODE = '<API_KEY_HERE>'
    API_KEY_ELEVATION = '<API_KEY_HERE>'
    
    '''
    Constructor
    '''
    def __init__(self, api_key_geocode, api_key_elevation):
        self.API_KEY_GEOCODE = api_key_geocode
        self.API_KEY_ELEVATION = api_key_elevation
        
    def searchByAddress(self, address):
        try:
            url = self.BASE_URL + 'geocode/json?address=' + address + '&key='+self.API_KEY_GEOCODE
            r = requests.get(url)
            return r.json()
        except:
            return None
    
    def searchElevation(self, lat, lng):
        try:
            url = self.BASE_URL + 'elevation/json?locations=' + str(lat) + ','+ str(lng) +'&key='+self.API_KEY_ELEVATION
            r = requests.get(url)
            return r.json()
        except:
            return None
    