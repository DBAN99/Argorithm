def gradingStudents(grades):
    answer = []

    for i in grades:

        if i < 38 or (i % 5 < 3):

            score = i

        else:
            mod_num = i % 5

            round_num = 5 - mod_num

            score = i + round_num

        answer.append(score)

    return answer