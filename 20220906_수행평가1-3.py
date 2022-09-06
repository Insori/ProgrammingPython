#3. 십진수를 2진수로

# def dec_to_bin(number):
    # return bin(number)[2:]

def dec_to_bin(number):
    result = ''
    while True:
        # number가 0이면 끝내고 결과 return
        if number == 0:
            return result
        # 아니면 number를 2로 나눈 나머지를 앞으로 보관, number는 number를 2로 나눈 몫으로 설정하자
        else:
            reminder = number % 2
            result = str(reminder) + result
            number = number // 2

print(dec_to_bin(10))   #1010
print(dec_to_bin(2))   #10
print(dec_to_bin(77))   #1001101
print(dec_to_bin(1024))   #10000000000