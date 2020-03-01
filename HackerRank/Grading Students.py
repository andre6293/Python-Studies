def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:
            pass
        else:
            if 5 - grades[i] % 5 < 3:
                grades[i] = grades[i] + (5 - grades[i] % 5)
            else:
                pass
    return grades


# teste
arr = [73, 67, 38, 33]
print(gradingStudents(arr))
