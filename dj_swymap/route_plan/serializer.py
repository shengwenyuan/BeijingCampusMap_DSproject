from rest_framework import serializers
from route_plan.models import RouteInfo

class RouteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteInfo
        fields = ['stepnum', 'stationHallmark', 'stationName', 
        'gcj02_longi', 'gcj02_lati', 'wgs84_longi', 'wgs84_lati', 
        'lineName', 'lineType', 'w_dist', 'w_time', 'w_cost', 'FTW']