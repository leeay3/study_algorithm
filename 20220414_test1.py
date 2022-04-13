# 공백 없애기

# 이 문제는 입력된 문자열에서 공백을 제거하여 출력하는 프로그램을 작성하는 것 입니다.
# 예를 들어 "This is Sparta !"가 입력 되었다면 "ThisisSparta!"가 출력되도록 하면 되는 것 입니다.

# 입력 : 50자 이내의 문장
# 출력 : 입력에서 공백이 제거된 문장

user_input = input()

user_input = user_input.replace(" ", "")

print(user_input)