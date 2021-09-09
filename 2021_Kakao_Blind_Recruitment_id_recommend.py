import re
def solution(new_id):
    new_id_1 = new_id.lower()
    new_id_2 = re.sub('[~!@#$%^&*()=+{}:?,<>/]', '', new_id_1)
    new_id_3 = new_id_2.replace('...','.')
    new_id_3 = new_id_3.replace('..','.')
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
    new_id_8 = list(new_id_7)
    if new_id_8[0]=='.':
        del new_id_8[0]
    try:
        if new_id_8[len(new_id_8)-1]=='.':
            del new_id_8[len(new_id_8)-1]
    except:
        new_id_8 = ''
    new_id_8 = ''.join(new_id_8)
    answer = new_id_8
    return answer

id = solution(input())
print(id)
#s = 'z-'
#while len(s)<3:
#    s += s[len(s)-1]
#print(s)