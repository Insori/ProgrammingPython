#4. 이니셜 abbreviate

def abbreviate(name):
    name = name.strip()
    # 한 글자씩 꺼내기
    for index, s in enumerate(name):    # enumerate - index 만들어줌
        # 첫 번째 글자 -> 대문자로 바꾸고 저장
        if index == 0:
            result = s.upper() + '. '
        # 띄어쓰기 -> 한 칸 뒤에 있는 글자를 -> 대문자로 바꾸고 저장
        if s == ' ':
            result += name[index + 1].upper() + '. '

    return result.strip()

def abbreviate2(name):
    result = '. '.join([word[0].upper() for word in name.split()])
    return result + '.'

print(abbreviate('Maverick'))   #M.
print(abbreviate('HAE CHAN'))   #H.C.
print(abbreviate('jin young park')) #J.Y.P.
print(abbreviate(' jin young park')) #J.Y.P.
print('-'*20)
print(abbreviate2('jin young park')) #J.Y.P.
print(abbreviate2(' jin young park')) #J.Y.P.