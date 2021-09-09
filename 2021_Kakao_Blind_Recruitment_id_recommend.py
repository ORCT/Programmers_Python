import re
def solution(new_id):
    new_id_1 = new_id.lower()
    new_id_2 = re.sub('[~!@#$%^&*()=+{}:?,<>/]', '', new_id_1)
    answer = new_id_2
    return answer

id = solution(input())
print(id)