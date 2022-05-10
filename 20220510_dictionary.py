#dictionary: 사전(단어(key): 뜻(value))
ㅇ = {}
urls = {'google': 'google.com', 18: 'unesco.org'}
print(urls)

#요소 추가
urls['유튜브'] = 'youtube.com' #없는 key에 값을 넣어줌
print(urls)

#요소 수정
urls['google'] = 'google.co.kr' #있는 key에 값을 넣어줌
print(urls)

#요소 출력
print(urls['google'])
print(urls[18]) #18: key - 인덱스 아님***

#요소 제거
del urls['유튜브']
print(urls)
#urls.pop()  #list에서는 맨 뒤에 값을 제거
urls.pop(18)    #key값을 안 주면 위처럼 에러
print(urls)

birthdays = {'다연': 5, '자윤': 11}
birthdays_list = [5,11]
print(birthdays['다연'])
print(birthdays.get('다연'))
print('google.co.kr' in urls)   #False
print('google' in urls) #True - key만 검색 가능
print('google.co.kr' in urls.values())  #True
urls['유튜브'] = 'youtube.com'
print(urls.values())    #값들을 모아놓은 것
print(urls.keys())      #key들을 모아놓은 것
print(urls.items())     #key, 값 튜플들을 모아놓은 것