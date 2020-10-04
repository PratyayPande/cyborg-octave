import datetime


def str_to_dt(a):
    return datetime.time(int(a[:a[0].find(':')]), int(a[a[0].find(':') + 1:]))


def dtconv(a):
    fin = []
    for i in range(0, len(a)):
        fin.append(str_to_dt(a[i][0]))
        fin.append(str_to_dt(a[i][1]))
    return fin


def find_next_time(c, tm):
    # function to find next time (start/end) from the given calendar after tm
    # return next time and whether the time is a start or end time
    indx = 0
    time = datetime.time(0, 0)
    for i in range(0, len(c)):
        if tm > c[i]:
            time = c[i]
            indx = i
            break
    return [time, indx]


cal1 = [['08:00', '09:30'], ['10:45', '12:30'], ['15:00', '17:00']]
dom1 = ['08:00', '18:00']
cal2 = [['09:00', '10:00'], ['11:00', '11:30'], ['12:00', '14:00'], ['16:00', '17:00']]
dom2 = ['07:00', '18:30']
meet_dur = 30
merge = cal1
c1 = dtconv(cal1)
c2 = dtconv(cal2)
d1 = dtconv(dom1)
d2 = dtconv(dom2)
stack = []
td = datetime.timedelta(minutes=meet_dur)
d = [max(d1[0], d2[0]), min(d1[1], d2[1])]
# completed conversion to datetime instances
c1 = [d[0]] + c1 + [d[1]]
l_occ_1 = [0, -1]
l_occ_2 = [0, -1]
# find next occupied start time
possible = []
init_index = d[0]
index = d[0]
while init_index < d[1]:
    r1 = find_next_time(c1, index)
    r2 = find_next_time(c2, index)
    j = [datetime.time(0, 0), 0]
    if r1[0] > r2[0]:
        j = r1
    else:
        j = r2
    if j[1] % 2 == 0:  # case if the next time is a start time
        stack.append('[')
    if j[1] % 2 == 1:  # case if the next time is an end time
        stack = stack[1:]
    index = j[0]
    if not stack:
        init_index = index
    if stack == ['[']:
        diff = (index.hour * 60 + index.minute) - (init_index.hour * 60 + init_index.minute)
        if diff > meet_dur:
            possible.append([init_index, index])
print(possible)
