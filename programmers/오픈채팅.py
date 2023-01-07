def solution(record):
    user_dict = dict()
    answer = []
    for chat in record:
        if len(chat.split(" ")) == 3:
            cmd, uid, name = chat.split(" ")
            user_dict[uid] = name
        else:
            cmd, uid = chat.split(" ")
    for chat in record:
        if len(chat.split(" ")) == 3:
            cmd, uid, name = chat.split(" ")
        else:
            cmd, uid = chat.split(" ")

        if cmd == "Enter":
            ans = f"{user_dict[uid]}님이 들어왔습니다."
            answer.append(ans)
        elif cmd == "Leave":
            ans = f"{user_dict[uid]}님이 나갔습니다."
            answer.append(ans)
        else:
            pass
    return answer