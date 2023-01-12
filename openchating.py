def solution(record):
    answer = []
    user_id = dict() # 모든 유저는 [유저 아이디]로 구분
    action = [] # 들락날락 기록 (~˘▾˘)~
    
    for in_and_out in record:
        inout_split = in_and_out.split() # 각 단어는 공백으로 구분

        if inout_split[0] == 'Enter': # Enter일때는 user_id에 id 저장 후 in_and_out에 Enter했음을 나타내는 'Enter'과 id 저장
            action.append(['E', inout_split[1]])
            user_id[inout_split[1]] = inout_split[2]
            
        elif inout_split[0] == 'Leave':
            action.append(['L', inout_split[1]])
        
        elif inout_split[0] == 'Change': # answer에는 Change를 기록하지 않음
            user_id[inout_split[1]] = inout_split[2]

    for record in action:
        id = user_id[record[1]]
        if record[0] == 'E':
                answer.append(f"{id}님이 들어왔습니다.")
        elif record[0] == 'L':
            answer.append(f"{id}님이 나갔습니다.")          

    return answer