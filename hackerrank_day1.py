def timeConversion(s):
    hour, minute, second = s.split(':')
    if second[2:] == "PM" and hour != '12':
        hour = str(int(hour) + 12)
    elif second[2:] == "AM" and hour == '12':
        hour = "00"
    else:
        hour = "12"
    time = hour + ':' + minute + ':' + second[0:2]
    return time