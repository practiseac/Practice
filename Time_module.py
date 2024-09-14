import time
a=time.strftime("%H:%M:%S")
print(a)
if a==int(time.strftime("%H")) and 0<=a<12:
    print("Good Morning")
elif a==int(time.strftime("%H")) and 12<=a<3:
    print("Good Afternoon")
elif a==int(time.strftime("%H")) and 3<=a<8:
    print("Good evening")
else:
    print("Good Night")
