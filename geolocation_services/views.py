from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.core.exceptions import ObjectDoesNotExist

from geolocation_services.models import Location
from geolocation_services.serializers import LocationSerializer  

from utils.google_maps import GoogleMapClient 

from company_services import settings 


class LocationGeneralApi(APIView):
    """
    List all Location, or create a new snippet.
    """
    def get(self, request):        
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    """
    Saves a Location when an Address is Found in Google Maps.
    """
    def post(self, request):
        response = {}
        httpStatus = status.HTTP_500_INTERNAL_SERVER_ERROR
        try:            
            if 'address' in request.data:
                googleMap = GoogleMapClient(settings.API_KEY_GEOCODE, settings.API_KEY_ELEVATION)
                jsonAddress = googleMap.searchByAddress(request.data['address'])
                
                if jsonAddress != None and len(jsonAddress['results']) > 0:           
                    jsonLocation = jsonAddress['results'][0]    
                    
                    lat = jsonLocation['geometry']['location']['lat']
                    lng = jsonLocation['geometry']['location']['lng']
                    elevation = 0.0
                    
                    jsonElevation = googleMap.searchElevation(lat, lng)
                                    
                    if jsonElevation != None:
                        elevation = jsonElevation['results'][0]['elevation']                                    
                    
                    objLocation = Location.objects.create(address      = request.data['address'],
                                                       latitude     = lat,
                                                       longitude    = lng,
                                                       elevation    = elevation
                                                       )
                    objLocation.save()
                    response = LocationSerializer(objLocation).data
                    httpStatus = status.HTTP_200_OK
                else:
                    response = {'message' : 'No results for ' +request.data['address']}
                    httpStatus = status.HTTP_200_OK
            else:
                response = {'message' : 'Invalid Parameters' }
                httpStatus = status.HTTP_400_BAD_REQUEST            
        except Exception as e:    
            response = {'message' : e.message }
            httpStatus = status.HTTP_500_INTERNAL_SERVER_ERROR        
        finally:
            return Response(response, status=httpStatus)
        
class LocationDetailApi(APIView):
    
    def find_by_id(self, pk):
        try:
            objLocation = Location.objects.get(pk=pk)
            return objLocation
        except ObjectDoesNotExist:
            return None
    
    """
    Search a Specific Location by ID
    """
    def get(self, request, pk):    
        response = {}
        httpStatus = status.HTTP_204_NO_CONTENT
        objLocation = self.find_by_id(pk)
        if (objLocation != None):
            response = LocationSerializer(objLocation).data
            httpStatus = status.HTTP_200_OK
            
            
        return Response(response, status=httpStatus)
            