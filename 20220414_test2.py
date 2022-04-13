# 시험성적 평균과 등급 구하기

# 구름이는 자신의 국어 수학 영어 3 과목의 시험 성적을 확인했습니다.
# 평균과 등급을 알고 싶어하는 구름이를 도와줄 수 있는 프로그램을 작성하십시오.

# 평균은 소수점 2번째 자리까지만(3번째 자리에서 반올림) 출력하며 등급은 평균 90점 이상일 경우 A, 90점 미만 80점 이상인 경우 B, 80점 미만 70정 이상이 C, 70점 미만 60점 이상이 D이고, 60점 미만으로는 F입니다.

# 입력 : 국어 영어 수학 순으로 점수 입력(각 과목 당 100점 만점)
# 출력 : 평균, 등급

user_input = input().split(" ")

sum = 0
for i in range(0, len(user_input)):
    sum = sum + int(user_input[i])

average = sum/len(user_input)
print("%.2f" % round(average,2), end=" ")

if average >= 90:
    print("A")
elif average < 90 and average >= 80:
    print("B")
elif average < 80 and average >= 70:
    print("C")
elif average < 70 and average >= 60:
    print("D")
else:
    print("F")
