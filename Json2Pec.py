import json

a = "D:\Coding\Phi_Chart_Transform\demo\Chart_AT.json"
b = "D:\Coding\Phi_Chart_Transform\demo\Chart_AT.pec"

file_json = open(a,"r",encoding="utf-8")
file_pec = open(b,"w",encoding="utf-8")
#转为json
file_json = json.loads(file_json.read())
#写入开头175
file_pec.write("175\n")
#写入bpm
file_pec.write("bp 0.000 {}\n\n".format(file_json["judgeLineList"][0]["bpm"]))
#遍历
count = 0
for judgeline in file_json["judgeLineList"]:
    #判定线速度
    for i in judgeline["speedEvents"]:
        file_pec.write("cv {} {:.3f} {:.3f}\n".format(count,i["startTime"]/32,i["value"]/(5/3)*(77/6)))
    file_pec.write("\n")
    #判定线坐标
    for i in judgeline["judgeLineMoveEvents"]:
        file_pec.write("cp {} {:.3f} {:.2f} {:.2f}\n".format(count,i["startTime"]/32,i["start"]*2048,i["start2"]*1400))
        file_pec.write("cm {} {:.3f} {:.3f} {:.2f} {:.2f} 1\n".format(count,i["startTime"]/32,i["endTime"]/32,i["end"]*2048,i["end2"]*1400))
    file_pec.write("\n")
    #判定线旋转
    for i in judgeline["judgeLineRotateEvents"]:
        file_pec.write("cd {} {:.3f} {:.3f}\n".format(count,i["startTime"]/32,-i["start"]))
        file_pec.write("cr {} {:.3f} {:.3f} {:.3f} 1\n".format(count,i["startTime"]/32,i["endTime"]/32,-i["end"]))
    file_pec.write("\n")
    #判定线不透明度
    for i in judgeline["judgeLineDisappearEvents"]:
        file_pec.write("ca {} {:.3f} {:.3f}\n".format(count,i["startTime"]/32,i["start"]*255))
        file_pec.write("cf {} {:.3f} {:.3f} {:.3f} 1\n".format(count,i["startTime"]/32,i["endTime"]/32,i["end"]*255))

    #音符
    for i in judgeline["notesAbove"]:
        if(i["type"]==1):
            #Tap
            file_pec.write("n1 {} {:.2f} {:.2f} 1 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")
        elif(i["type"]==2):
            #Drag
            file_pec.write("n4 {} {:.2f} {:.2f} 1 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")
        elif(i["type"]==3):
            #Hold
            file_pec.write("n2 {} {:.2f} {:.2f} {:.2f} 1 0\n".format(count,i["time"]/32,(i["time"]+i["holdTime"])/32,i["positionX"]/9*1024))
            file_pec.write("# 1.00\n")
            file_pec.write("& 1.00\n")
        else:
            #Flick
            file_pec.write("n3 {} {:.2f} {:.2f} 1 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")
    for i in judgeline["notesBelow"]:
        if(i["type"]==1):
            #Tap
            file_pec.write("n1 {} {:.2f} {:.2f} 2 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")
        elif(i["type"]==2):
            #Drag
            file_pec.write("n4 {} {:.2f} {:.2f} 2 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")
        elif(i["type"]==3):
            #Hold
            file_pec.write("n2 {} {:.2f} {:.2f} {:.2f} 2 0\n".format(count,i["time"]/32,(i["time"]+i["holdTime"])/32,i["positionX"]/9*1024))
            file_pec.write("# 1.00\n")
            file_pec.write("& 1.00\n")
        else:
            #Flick
            file_pec.write("n3 {} {:.2f} {:.2f} 2 0\n".format(count,i["time"]/32,i["positionX"]/9*1024))
            file_pec.write("# {:.3f}\n".format(i["speed"]))
            file_pec.write("& 1.00\n")

    count+=1