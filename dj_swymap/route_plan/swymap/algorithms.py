import json
Inf = float('inf')
import os

with open('./route_plan/swymap/stationGraph.json', 'r') as f:
    stationGraph=json.load(f)
# with open('/home/swy/ds_design/dj_swymap/route_plan/swymap/stationGraph.json', 'r') as f:
#     stationGraph=json.load(f)

#最小堆
def upadjust(nums, w_i):
    if len(nums)==1:
        return
    childindex = len(nums)-1
    parentindex = (childindex-1)//2
    temp = nums[childindex]
    while childindex>0 and temp[1][w_i] < nums[parentindex][1][w_i]:
        nums[childindex] = nums[parentindex]
        childindex = parentindex
        parentindex = (parentindex-1)//2
    nums[childindex] = temp

def downadjust(nums, w_i, parentindex):
    if len(nums)==1:
        return
    temp = nums[parentindex]
    childindex = 2*parentindex + 1
    while childindex < (len(nums)-1):
        if childindex +1 <len(nums) and nums[childindex+1][1][w_i] < nums[childindex][1][w_i]:
            childindex += 1
        if temp[1][w_i] < nums[childindex][1][w_i]:
            break
        nums[parentindex] = nums[childindex]
        parentindex = childindex
        childindex = childindex*2+1
    nums[parentindex] = temp

# def buildMaxHeap(nums, w_i):
#     for i in range((len(nums)-1)//2,-1,-1):
#         downadjust(nums, w_i,i)

'''
adj: stationGraph   src: startStation   dst: finalStation   n: total station number
dist: distance from startStation to the nowStation
'''

def dijkstra(srcStation='2737', w_choice=0):
    distance = {}
    book = {}
    for i in stationGraph.keys():
        book[i] = False
        distance[i] = [Inf, srcStation]
    distance[srcStation][0] = 0
    u = srcStation
    n = len(stationGraph)

    for _ in range(n-1):  #loop n-1 times
        book[u] = True
        next_u, min_road = None, Inf
        for index in stationGraph.keys():
            if index in stationGraph[u].keys():
                weight = stationGraph[u][index][w_choice]
            else:   
                weight = Inf
                continue
            
            if (not book[index]) and ((distance[u][0]+weight) < distance[index][0]):
                distance[index][0] = distance[u][0] + weight
                distance[index][1] = u
        
        for k, v in book.items():
            if not v:
                if distance[k][0] < min_road:
                    next_u, min_road = k, distance[k][0]
        
        u = next_u
    # print(distance)
    return distance

def heapDijkstra(srcStation='252', w_choice=0):
    print("start dijstra running for w_choice=", w_choice)
    routeHeap = []
    distance = {}
    graph = stationGraph
    u = srcStation
    last_w = 0
    book = {}
    for i in graph.keys():
        book[i] = False
        distance[i] = [Inf, srcStation]
    distance[u][0] = 0
    book[u] = True
    for _ in range(len(graph)-1):
        for i, w in graph[u].items():
            if not book[i]:
                w[w_choice] += last_w
                routeHeap.append([i, w, u])
                upadjust(routeHeap, w_choice)

        while(book[routeHeap[0][0]]):
            if len(routeHeap)>1:
                routeHeap[0]=routeHeap.pop()
                downadjust(routeHeap, w_choice, 0)
            else: 
                routeHeap.pop()
                break
        if len(routeHeap)==0:    
            continue
        u = routeHeap[0][0]
        
        last_w = routeHeap[0][1][w_choice]
        distance[u][0] = routeHeap[0][1][w_choice]
        distance[u][1] = routeHeap[0][2]
        book[u] = True
        # if u=='95':
        #     print('95',distance[u])
        # if u=='3112':
        #     print('3112',distance[u])
        # if u=='1890':
        #     print('1890',distance[u])
        # if u=='1912':
        #     print('1912', distance[u])
        # if u=='3090':
        #     print('3090',distance[u])
        # if u=='2611':
        #     print('2611', distance[u])
        if len(routeHeap)>1:
            routeHeap[0]=routeHeap.pop()
            downadjust(routeHeap, w_choice, 0)
        else: routeHeap.pop()

    print("end of dijstra running for w_choice=", w_choice)
    
    return distance

if __name__=='__main__':
    distance = heapDijkstra('3214', 0)

    with open('/home/swy/ds_design/dj_swymap/route_plan/swymap/stationHallmark.json', 'r') as f:
        stationHallmark=json.load(f)

    print('{}<--'.format(3177), end='')
    i='3177'
    while distance[i][1] != '3214':
        tmp = distance[i][1]
        name = stationHallmark[tmp][0]
        print('{}<--'.format(name), end='')
        i = tmp
    print('3214')
    print(distance['3177'][0])