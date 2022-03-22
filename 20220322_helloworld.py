print("Hello, World!")  #큰따옴표와 작은따옴표는 같음
print('Red velvet\'s favorite song is Red flavour')  #' <-가 있는 경우 큰따옴표를 써야한다. 아니면 ' 앞에 \를 붙여준다.
print("Red velvet's favorite song is Red flavour")

name='양다연'
print('Hello, '+name+'!')   #JAVA 형식
print('Hello, %s!' % name)  #C 형식
print('Hello, {}!'.format(name))    #format 함수
print(f'Hello, {name}!')    #f-string 형식
