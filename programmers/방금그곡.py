def solution(m, musicinfos):
    
    answer_list = []
    SongTime = []
    
    for i in range(len(musicinfos)):
        temp = musicinfos[i].split(",")
        StartTemp = temp[0].split(":")
        EndTemp = temp[1].split(":")
    
        if int(EndTemp[0]) == int(StartTemp[0]):
            DuringTime = int(EndTemp[1]) - int(StartTemp[1])
        else:
            if EndTemp[0] == "00":
                EndTemp[0] = "24"
                DuringTime = ((int(EndTemp[0]) - int(StartTemp[0]))*60 + int(EndTemp[1])) - int(StartTemp[1])
            else:
                DuringTime = ((int(EndTemp[0]) - int(StartTemp[0]))*60 + int(EndTemp[1])) - int(StartTemp[1])
        
        RithmTemp = []
        
        for i in range(len(temp[3])):
            if temp[3][i] == "#":
                RithmTemp.pop(-1)
                RithmTemp.append(temp[3][i - 1].lower() + temp[3][i])
            else:
                RithmTemp.append(temp[3][i])
            
        if len(RithmTemp) > DuringTime:
            OriginalRithm = ""
            for i in range(DuringTime):
                OriginalRithm += (RithmTemp[i])
        else:
            ColumnRithm = ""
            for i in range(len(RithmTemp)):
                ColumnRithm += RithmTemp[i]
            OriginalRithm = ColumnRithm*(DuringTime//len(RithmTemp))
            
            for i in range(DuringTime%len(RithmTemp)):
                OriginalRithm += (RithmTemp[i])
        
        AnswerRithmList = []
        for i in range(len(m)):
            if m[i] == "#":
                AnswerRithmList.pop(-1)
                AnswerRithmList.append(m[i - 1].lower() + m[i])
            else:
                AnswerRithmList.append(m[i])
        
        AnswerRithm = ""
        for i in AnswerRithmList:
            AnswerRithm += i
        
        if AnswerRithm in OriginalRithm:
            answer_list.append(temp[2])
            SongTime.append(DuringTime)
    
    if len(answer_list) == 1:
        answer = answer_list[0]
    elif len(answer_list) == 0:
        answer = "(None)"
    else:
        flag = 0
        answer = ""
        for i in range(len(answer_list)):
            if flag < SongTime[i]:
                flag = SongTime[i]
                answer = answer_list[i]
    
    return answer