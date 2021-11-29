def timeConversion(s):
    if s.find('AM') != -1:
        s = s[0:-2]
        s_parse = s.split(':')
        new_hours = int(s_parse[0])
        if new_hours >= 12:
            new_hours -= 12
        if new_hours < 10:
            s_parse[0] = f'0{new_hours}'
        else:
            s_parse[0] = str(new_hours)
        return ':'.join(s_parse)
    else:
        s = s[0:-2]
        s_parse = s.split(':')
        new_hours = int(s_parse[0])
        if new_hours < 12:
            new_hours += 12
        if new_hours == 24:
            s_parse[0] = '00'
        else:
            s_parse[0] = str(new_hours)
        return ':'.join(s_parse)


string = '04:59:59AM'
print(timeConversion(string))
