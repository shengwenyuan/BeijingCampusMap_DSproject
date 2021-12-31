import json

with open('./stationHallmark.json', 'r') as f:
    stationHallmark=json.load(f)

goals = {'BJUT':["北工大西门", "14号线东段", "subway"],
         'PKU':["北京大学东门", "4号线大兴线", "subway"],
         'UIBE':["对外经贸大学东门", "119", "bus"], 
         'BNU':["北京师范大学南门", "92", "bus"],
         'BIT':["良乡大学城西", "房山线", "subway"],
         'BJU':["北京交通大学东门", "87", "bus"], 
         'RUC':["人民大学", "4号线大兴线", "subway"], 
         'CUC':["传媒大学", "八通线", "subway"]}      
campus = {}

def nsort():
    for stationIndex, station in stationHallmark.items():
        for k, v in goals.items():
            if [station[0], station[3], station[4]] == v:
                campus[k] = str(stationIndex)
    print(campus)


if __name__=='__main__':
    nsort()
    with open("campus.json", 'w') as f:
        json.dump(campus,f)