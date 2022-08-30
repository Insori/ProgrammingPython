# 1. 전화번호를 인자로 받아, 각 숫자 중 홀수만 더해서 합계를 리턴하는 sum_odd 함수를 작성하시오.
def sum_odd(phone_number):
    sum_value = 0
    # 전화번호에서 하나씩 꺼내기
    for number in phone_number:
        # 문자 -> 숫자로 형변환
        number = int(number)
        # 홀수인지 구분하기
        if number % 2 == 1:
            # 합계 구하기
            sum_value += number
    return sum_value

result = sum_odd('01012345678')
print(result)   # 17
result = sum_odd('01022224444')
print(result)   # 1
result = sum_odd('01099999999')
print(result)   # 73
