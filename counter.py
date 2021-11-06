#1번
def solution(arr):
    cnt_1 = arr.count(1)
    cnt_2 = arr.count(2)
    cnt_3 = arr.count(3)
    answer = []
    if cnt_1 == cnt_2 == cnt_3:
        answer.extend([0, 0, 0])

    elif cnt_1 > cnt_2 and cnt_1 > cnt_3:
        a = cnt_1 - cnt_2
        b = cnt_1 - cnt_3
        answer.extend([0, a, b])
    elif cnt_2 > cnt_3 and cnt_2 > cnt_1:
        a = cnt_2 - cnt_1
        b = cnt_2 - cnt_3
        answer.extend([a, 0, b])
    else:
        a = cnt_3 - cnt_1
        b = cnt_3 - cnt_2
        answer.extend([a, b, 0])

    return answer

# 2번
from datetime import datetime

def solution(log):
    num = len(log)
    cnt = 0
    form = "%H:%M"
    time_result = 0

    answer = ''

    for i in range(num):
        if i % 2 == 1:

            time1 = datetime.strptime(log[i], form)
            time2 = datetime.strptime(log[cnt], form)
            cnt += 2

            cnt_time = int((time1 - time2).total_seconds())

            if cnt_time >= 6300:
                cnt_time = 6300

            elif cnt_time < 300:
                cnt_time = 0

            time_result += cnt_time

    hours = time_result // 3600
    time_result = time_result - hours * 3600
    mins = time_result // 60

    if hours < 10:
        answer = "0" + str(hours) + ":" + str(mins)
    else:
        answer = str(hours) + ":" + str(mins)

    return answer

