# 2212 인소리

# 1
def sum_odd(num):
    num_sum=0
    for i in num:
        if int(i)%2==1:
            num_sum+=int(i)
        else:
            pass
    return num_sum

result = sum_odd('01012345678')
print(result)
result = sum_odd('01022224444')
print(result)
result = sum_odd('01099999999')
print(result)

# 2
def encrypt(word):
    word_2=''
    for i in word:
        if i=='a' or i =='e' or i=='i' or i=='o' or i=='u' or i=='A' or i =='E' or i=='O':
            word_2+='*'
        else:
            word_2+=i
    return word_2

print(encrypt('ive'))
print(encrypt('nct dream'))
print(encrypt('AEiou'))
print(encrypt('GOOGLE'))
print(encrypt('BTS'))

# 3
def dec_to_bin(n):
    bin_2 = bin(n)
    bin_3=bin_2[2:]
    return bin_3

print(dec_to_bin(10))
print(dec_to_bin(2))
print(dec_to_bin(77))
print(dec_to_bin(1024))

# 4
def abbreviate(word):
    word2=' '
    for i in word:
        if i>='a' and i<='z':
            word2+=i.upper()
        else:
            word2+=i
    word3 = ''
    for j in range(0,len(word2)):
        if word2[j]==' ':
            word3+=word2[j+1]+'. '
    return word3

print(abbreviate("Maverick"))
print(abbreviate("HAE CHAN"))
print(abbreviate("jin young park"))

# 5
def fare_pc(minute):
    p=1000
    pay=0
    if minute>0 and minute<=10:
        pay=p*1
    elif minute>10 and minute<=20:
        pay=p*2
    elif minute>20 and minute<=30:
        pay=p*3
    elif minute>30 and minute<=40:
        pay=p*4
    return pay

print(fare_pc(minute=3))
print(fare_pc(minute=20))
print(fare_pc(minute=34))

# 6
def get_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    bmi = round(bmi, 2)
    if bmi<18.5:
       p='저체중 '+str(bmi)
    elif bmi>=18.5 and bmi<23:
        p='정상 '+str(bmi)
    elif bmi>=23 and bmi<25:
        p='과체중 '+str(bmi)
    elif bmi>=25:
        p='비만 '+str(bmi)
    return p

print(get_bmi(height=170, weight=60))
print(get_bmi(height=150, weight=60))
print(get_bmi(height=180, weight=50))
print(get_bmi(height=160, weight=60))

# 7
# def minus_time(hour1, minute1, hour2, minute2):
#     h=hour1-hour2
#     m=minute1-minute2
#     a=' '
#     return h,m,a
#
# sign, hour, minute=minus_time(hour1=13, minute1=40, hour2=6, minute2=33)
# print(sign, hour, minute)
# sign, hour, minute=minus_time(hour1=6, minute1=33, hour2=13, minute2=40)
# print(sign, hour, minute)
# sign, hour, minute=minus_time(hour1=13, minute1=40, hour2=13, minute2=40)
# print(sign, hour, minute)
# sign, hour, minute=minus_time(hour1=2, minute1=3, hour2=0, minute2=4)
# print(sign, hour, minute)
# sign, hour, minute=minus_time(hour1=2, minute1=3, hour2=2, minute2=4)
# print(sign, hour, minute)












# 2122 인소리