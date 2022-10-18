# 키(cm)와 몸무게(kg)를 입력받아 비만정도(저체중, 정상, 과체중, 비만)와 BMI 지수를 리턴하는 get_bmi
'''
BMI 계산법: 몸무게(kg)를 키(m)의 제곱으로 나눈 값
bmi < 18.5: 저체중
18.5 <= bmi <23: 정상
23 <= bmi < 25: 과체중
25 <= bmi: 비만
'''
print(get_bmi(height=170, weight=60))