import json
import math

a = input("官谱json名称:\n")
b = input("希望导出的rpe json名称:\n")

file_json = open(a,"r",encoding="utf-8")
file_json = json.loads(file_json.read())
rpe = {
    "BPMList":[],
    "META":{
        "RPEVersion":100,
        "name":input("名称:"),
        "song":input("音频名称:"),
        "background":input("曲绘名称:"),
        "charter":input("谱师:"),
        "composer":input("曲师:"),
        "id":"00000000",
        "level":input("难度:"),
        "offset":0
    },
    "judgeLineGroup":["Default"],
    "judgeLineList":[]
}
#写入info.txt
info = "#\nName: {}\nPath: {}\nSong: {}\nPicture: {}\nChart: {}\nLevel: {}\nComposer: {}\nCharter: {}".format(
    rpe["META"]["name"],rpe["META"]["id"],rpe["META"]["song"],rpe["META"]["background"],b,rpe["META"]["level"],rpe["META"]["composer"],rpe["META"]["charter"])
info_txt = open("info.txt","w",encoding="utf-8")
info_txt.write(info)
info_txt.close()

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
    if file_json["formatVersion"] == 3:
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
    elif file_json["formatVersion"] == 1:
        #一代远古官谱
        for i in judgeline["judgeLineMoveEvents"]:
            rpe["judgeLineList"][count]["eventLayers"][0]["moveXEvents"].append(
                {"easingType":1,
                "end":-450+(i["end"]//1000)/880*900,
                "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
                "linkgroup":0,
                "start":-450+(i["start"]//1000)/880*900,
                "startTime":[math.floor(i["startTime"]/32),int(i["startTime"])%32,32]})
            rpe["judgeLineList"][count]["eventLayers"][0]["moveYEvents"].append(
                {"easingType":1,
                "end":-450+(i["end"]%1000)/520*900,
                "endTime":[math.floor(i["endTime"]/32),int(i["endTime"])%32,32],
                "linkgroup":0,
                "start":-450+(i["start"]%1000)/520*900,
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
    if not ("numOfNotes" in judgeline): # 解决了部分谱面没有 numOfNotes 的问题
        print("找不到 numOfNotes，已自动计算")
        rpe["judgeLineList"][count]["numOfNotes"] = len(judgeline["notesAbove"]) + len(judgeline["notesBelow"])
    else:
           rpe["judgeLineList"][count]["numOfNotes"] = judgeline["numOfNotes"]
    count+=1

file_rpe = open(b,"w",encoding="utf-8")
file_rpe.write(json.dumps(rpe))
file_rpe.close()
