from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from route_plan.models import RouteInfo
from route_plan.serializer import RouteInfoSerializer

import json
from route_plan.swymap.algorithms import dijkstra, heapDijkstra


@api_view(['GET'])
def routeinfo_detail(request, ftw, format=None):
    if request.method == 'GET':
        
        if not RouteInfo.objects.filter(FTW=ftw).exists():
            with open('./route_plan/swymap/stationHallmark.json', 'r') as f:
                stationHallmark = json.load(f)
            with open('./route_plan/swymap/stationGraph.json', 'r') as f:
                stationGraph = json.load(f)
            with open('./route_plan/swymap/campus.json', 'r') as f:
                campus = json.load(f)

            fr, to, w = ftw.split('-')
            w = int(w)
            if w > 2 or fr not in campus or to not in campus or fr==to:
                return Response(status=status.HTTP_204_NO_CONTENT)
            distance = heapDijkstra(campus[fr], w)
            # distance = dijkstra(campus[fr], w)

            routeStations = []
            index_now = campus[to]
            while index_now != campus[fr]:
                index_before = distance[index_now][1]
                routeStations.append(index_now)
                index_now = index_before
            routeStations.append(index_now)

            w0, w1, w2, step_cnt, taken_cnt = [0]*5
            lt = stationHallmark[campus[fr]][4]
            last_w2 = w2
            index_now = routeStations.pop()
            while routeStations != []:
                index_next = routeStations.pop()
                station = RouteInfo(
                    stepnum = step_cnt,
                    stationHallmark = index_now,
                    stationName = stationHallmark[index_now][0],
                    gcj02_longi = stationHallmark[index_now][1][0],
                    gcj02_lati = stationHallmark[index_now][1][1],
                    wgs84_longi = stationHallmark[index_now][2][0],
                    wgs84_lati = stationHallmark[index_now][2][1],
                    lineName = stationHallmark[index_now][3],
                    lineType = stationHallmark[index_now][4],
                    w_dist = w0,
                    w_time = w1,
                    w_cost = w2,
                    FTW = ftw,
                )
                station.save()
                #compute the weight of next station(fullfilled in next loop)
                w0 += stationGraph[index_now][index_next][0]
                w1 += stationGraph[index_now][index_next][1]
                if [stationHallmark[index_now][3], stationHallmark[index_now][4]] != \
                [stationHallmark[index_next][3], stationHallmark[index_next][4]]:
                    if stationHallmark[index_now][4]==stationHallmark[index_next][4]=='subway':
                        taken_cnt += 1
                    else:
                        taken_cnt = 0
                        last_w2 = w2
                    lt = stationHallmark[index_next][4]
                else:
                    taken_cnt += 1
                if lt == 'bus':
                    ticket = 1 + taken_cnt//12
                elif lt == 'subway':
                    ticket = 3 + taken_cnt//3
                w2 = last_w2 + ticket

                index_now = index_next
                step_cnt = step_cnt+1

        routeinfo = RouteInfo.objects.all().filter(FTW=ftw)
        serializer = RouteInfoSerializer(routeinfo, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)