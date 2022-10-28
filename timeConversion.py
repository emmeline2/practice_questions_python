def timeConversion(s):
    # Write your code here
    amOrPm = s[8:]
    
    if amOrPm == "PM": 
        if s[0:2] != "12":
            print("S[0:2]: ", s[0:2])
            hours = int(s[0:2])
            hours += 12
            slist = list(s)
            s = str(hours)
            temp = ''.join(c for c in slist[2:])
            s += temp
    else:
        if s[0:2] == "12":
            slist = list(s)
            s = str("00")
            temp = ''.join(c for c in slist[2:])
            s += temp
    
    return s[:8]
