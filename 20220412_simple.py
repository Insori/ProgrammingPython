#예약어
import keyword
print(keyword.kwlist)

print('-'*200)

#달력 보기
import calendar
print(calendar.month(2022, 4))
print(calendar.month(2006, 2))
print(calendar.month(2022, 12))

print('-'*200)

#현재 날짜와 시각 보기
import datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.minute, now.second)   #지금 시각
birthday = datetime.datetime(2006, 2, 17)
print(now - birthday)   #얼마나 상았는지
christmas = datetime.datetime(2022, 12, 25)
print(christmas - now)  #크리스마스까지 얼마나 남았는지

print('-'*200)

#윈도우 보기
#import tkinter as tk
#base = tk.Tk()
#base.mainloop()

#turtle
import turtle as t
t.shape('turtle')
t.speed(2)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

t.forward(100)
t.left(144)
t.forward(100)
t.left(144)
t.forward(100)
t.left(144)
t.forward(100)
t.left(144)
t.forward(100)





t.mainloop()