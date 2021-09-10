import re
def solution(new_id):
    new_id_1 = new_id.lower()
    new_id_2 = ''
    for c in new_id_1:
        if 'a' <= c <= 'z' or '0' <= c <='9' or c == '-' or c =='_' or c == '.':
            new_id_2 += c
    new_id_3 = new_id_2.replace('..','.')
    while True:
        if len(new_id_3) != len(new_id_3.replace('..','.')):
            new_id_3 = new_id_3.replace('..','.')
        else:
            break
    new_id_4 = list(new_id_3)
    if new_id_4[0]=='.':
        del new_id_4[0]
    try:
        if new_id_4[len(new_id_4)-1]=='.':
            del new_id_4[len(new_id_4)-1]
    except:
        new_id_4 = ''
    new_id_4 = ''.join(new_id_4)
    if new_id_4=='':
        new_id_5 = 'a'
    else:
        new_id_5 = new_id_4
    new_id_6=''
    if len(new_id_5)>=16:
        for i in range(0,15):
            new_id_6 += new_id_5[i]
    else:
        new_id_6 = new_id_5
    while len(new_id_6)<3:
        new_id_6 += new_id_6[len(new_id_6)-1]
    new_id_7 = new_id_6
    answer = new_id_7
    if answer!=new_id:
        return solution(answer)
    else:
        return answer

id = solution(input())
print(id)