import itertools
def solution(orders, course):
    table = {}
    for i in course:
        table[i] = {}
    for s in orders:
        for i in course:
            for comb in itertools.combinations(s,):
                menu = ''.join(sorted(comb))
                if menu not in table[i].keys():
                    table[i][menu] = 1
                else:
                    table[i][menu] += 1
    answer = []
    for i in course:
        if len(table[i]) == 0:
            continue
        biggest = max(table[i].values())
        if biggest < 2:
            continue
        for key in table[i].keys():
            if biggest == table[i][key]:
                answer.append(key)
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders,course))