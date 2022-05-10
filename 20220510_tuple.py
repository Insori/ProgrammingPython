t = ()
xy = (2560,1440)
color = 129,247,216
print(t)
print(xy)   #(2560, 1440)
print(color)    #(129, 247, 216)
print(xy+color) #(2560, 1440, 129, 247, 216)
print(xy*2) #(2560, 1440, 2560, 1440)

#패킹, 언패킹: 자동
color = 129,247,216 #패킹(묶음)
red, green, blue = color    #언패킹
print(red)  #129
x, y = (1920,1080)
print(y)
print(color[1]) #인덱싱 가능
print(color[0:2])   #슬라이싱 가능

#color[1] = 255  #값을 바꿀 수 없음

new_tuple = xy+color+(1440,1090)
print(new_tuple)    #(2560, 1440, 129, 247, 216, 1440, 1090)
print(new_tuple.index(1440))    #1440의 인덱스 자리 - 1
print(new_tuple.count(1440))    #1440의 개수 - 2

임채영, 이예진 = 10, 8
print(임채영)  #10
print(이예진)  #8
이예진, 임채영 = 임채영, 이예진
print(임채영)  #8
print(이예진)  #10
