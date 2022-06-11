def solution(id_list, report, k):
    answer=[]
    r = set(report)
    r_d = {i:[] for i in id_list}
    r_cnt = {i:0 for i in id_list}
    r_m = []
    for i in r:
        a,b = i.split()
        r_d[a].append(b)
        r_cnt[b] += 1
    for key,v in r_cnt.items():
        if v >= k:
            r_m.append(key)
    for i in id_list:
        ans_cnt = 0
        for j in r_m:
            if j in r_d[i]:
                ans_cnt += 1
        answer.append(ans_cnt)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))