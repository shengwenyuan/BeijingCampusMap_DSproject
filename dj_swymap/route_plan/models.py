from typing import Sequence
from django.db import models
from django.db.models.enums import Choices

class RouteInfo(models.Model):
    # stationIndex : [ stationName, gcj02, wgs84, lineName, lineType ]
    stepnum = models.IntegerField()

    stationHallmark = models.IntegerField()

    stationName = models.CharField(max_length=30)
    gcj02_longi = models.FloatField()
    gcj02_lati = models.FloatField()
    wgs84_longi = models.FloatField()
    wgs84_lati = models.FloatField()
    lineName = models.CharField(max_length=30)
    lineType = models.CharField(choices=[("bus", "bus"), ("subway", "subway")], max_length=20)
    FTW = models.CharField(max_length=80)
    w_dist = models.FloatField()
    w_time = models.IntegerField()
    w_cost = models.IntegerField()