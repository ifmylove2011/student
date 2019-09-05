# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def grade_show(score):
    if score >= 90:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    else:
        grade = 'C'
    print(grade)

grade_show(88)