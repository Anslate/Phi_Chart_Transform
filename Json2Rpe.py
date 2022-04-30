import json
import math

a = "D:\Coding\Phi_Chart_Transform\demo\Chart_AT.json"
b = "D:\Coding\Phi_Chart_Transform\demo\Chart_AT2.json"

file_json = open(a,"r",encoding="utf-8")
file_json = json.loads(file_json.read())
rpe = {
    "BPMList":[],
    "META":{
        "RPEVersion":100,
        "background":"Illustration.png",
        "charter":"abc",
        "composer":"abc",
        "id":"00000000",
        "level":"0",
        "name":"abc",
        "offset":0,
        "song":"Rrhar'il.wav"
    },
    "judgeLineGroup":["Default"],
    "judgeLineList":[]
}
#写入bpm
rpe["BPMList"].append({"bpm":file_json["judgeLineList"][0]["bpm"],"startTime":[0,0,1]})
#遍历
count = 0
for judgeline in file_json["judgeLineList"]:
    rpe["judgeLineList"].append({"Group":0,"Name":"Untitled","Texture":"line.png","eventLayers":[{"alphaEvents":[],"moveXEvents":[],"moveYEvents":[],"rotateEvents":[],"speedEvents":[]}]})
    #判定线不透明度
    for i in judgeline["judgeLineDisappearEvents"]:
         rpe["judgeLineList"][count]["eventLayers"][0]["alphaEvents"].append(
            {"easingType":1,
            "end":i["end"]*255,
            "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
            "linkgroup":0,
            "start":i["start"]*255,
            "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})
    #判定线坐标
    for i in judgeline["judgeLineMoveEvents"]:
        rpe["judgeLineList"][count]["eventLayers"][0]["moveXEvents"].append(
            {"easingType":1,
            "end":-450+i["end"]*900,
            "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
            "linkgroup":0,
            "start":-450+i["start"]*900,
            "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})
        rpe["judgeLineList"][count]["eventLayers"][0]["moveYEvents"].append(
            {"easingType":1,
            "end":-450+i["end2"]*900,
            "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
            "linkgroup":0,
            "start":-450+i["start2"]*900,
            "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})    
    #判定线旋转
    for i in judgeline["judgeLineRotateEvents"]:
         rpe["judgeLineList"][count]["eventLayers"][0]["rotateEvents"].append(
            {"easingType":1,
            "end":-i["end"],
            "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
            "linkgroup":0,
            "start":-i["start"],
            "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})
    #判定线速度
    for i in judgeline["speedEvents"]:
        rpe["judgeLineList"][count]["eventLayers"][0]["speedEvents"].append(
            {"end":i["value"]/(5/3)*7.5,
            "endTime":[math.floor(i["startTime"]/32/32),int(i["startTime"]/32)%32,32],
            "linkgroup":0,
            "start":i["value"]/(5/3)*7.5,
            "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})
    #音符
    rpe["judgeLineList"][count]["isCover"] = 1
    rpe["judgeLineList"][count]["notes"] = []
    for i in judgeline["notesAbove"]:
        if(i["type"]==1):
            rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":1,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":1,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            )
        elif(i["type"]==2):   
            rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":1,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":4,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            ) 
        elif(i["type"]==3):
            rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":1,
                    "alpha":255,
                    "endTime":[math.floor((i["time"]+i["holdTime"])/32),int(i["time"]+i["holdTime"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":1.0,
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":2,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            )
        else:
            rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":1,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":3,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            )
        for i in judgeline["notesBelow"]:
            if(i["type"]==1):
                rpe["judgeLineList"][count]["notes"].append(
                   {
                    "above":2,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":1,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
              )
            elif(i["type"]==2):   
                rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":2,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":4,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            ) 
            elif(i["type"]==3):
                rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":2,
                    "alpha":255,
                    "endTime":[math.floor((i["time"]+i["holdTime"])/32),int(i["time"]+i["holdTime"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":1.0,
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":2,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            )
            else:
                rpe["judgeLineList"][count]["notes"].append(
                {
                    "above":2,
                    "alpha":255,
                    "endTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "isFake":0,
                    "positionX":i["positionX"]*(675.0/9),
                    "size":1.0,
                    "speed":i["speed"],
                    "startTime":[math.floor(i["time"]/32),int(i["time"])%32,32],
                    "type":3,
                    "visibleTime" : 999999.0,
                    "yOffset" : 0.0
                }
            )
        
    rpe["judgeLineList"][count]["numOfNotes"] = judgeline["numOfNotes"]
    count+=1

file_rpe = open(b,"w",encoding="utf-8")
file_rpe.write(json.dumps(rpe))
file_rpe.close()