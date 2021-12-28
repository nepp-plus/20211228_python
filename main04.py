# 파일은 열고나면 반드시 닫아야함.
# 파이썬의 with 문법 이용시 => 열고 난 파일을, with 구문이 끝나면 자동 종료.

with open('student_list.txt', 'a') as my_file:
    my_file.write('이 파일은 학생 목록을 저장합니다.')