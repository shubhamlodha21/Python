import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hrs = (int(time.strftime('%H')))

print(hrs)

if ((hrs>=0) and (hrs<=5)):
    print("GOOD NIGHT")
elif (hrs>=6 and hrs<=12):
    print("GOOD MORNING")
elif (hrs>=13 and hrs<=18):
    print("GOOD AFTERNOON")
else:
    print("GOOD EVENING")

