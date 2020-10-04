day = int(input(''))
#print(day)
latitude = float(input(''))
diff = (day/360)*latitude
#print(latitude)
#print(diff)
hrs = round(diff)
mins = diff - hrs
angleHours = (hrs/12)*360 + mins*30
angleMinutes = mins*360
answer = abs(abs(angleHours) - abs(angleMinutes))
if answer > 180:
    answer = 360-answer
print(answer)
