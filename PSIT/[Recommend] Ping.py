"""[Recommend] Ping"""

def checkstatus(text, status):
    """Ping"""
    if text.count('out.') >= 1 or text.count('fail') >= 1:
        return 1
    else:
        if status == 2:
            return text[text.find("time") + 4:text.find("ms")]
        else:
            return 0

def main():
    """Ping"""
    st1, st2, st3, st4, st5, st6, st7, ipfew = input(), input(), \
input(), input(), input(), input(), input(), ''
    st1.count("few")
    st2.count("few")
    if st3.count("[") <= 0:
        ipfew = st3[st3.find("Pinging ") + 8:st3.find(" with")]
    else:
        ipfew = st3[st3.find("[") + 1:st3.find("]")]
    intf = checkstatus(st4, 1) + checkstatus(st5, 1) + checkstatus(st6, 1) + checkstatus(st7, 1)
    print('Ping statistics for %s:' %(ipfew))
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),' \
%(abs(int(intf) - 4), int(intf), str(int(intf) * 25) + "%"))
    if intf < 4:
        time1, time2, time3, time4 = str(checkstatus(st4, 2)), \
str(checkstatus(st5, 2)), str(checkstatus(st6, 2)), str(checkstatus(st7, 2))
        print('Approximate round trip times in milli-seconds:')
        if str(time1).count("<") >= 1 or str(time2).count("<") or str(time3).count("<")\
 or str(time4).count("<"):
            print('    Minimum = 0ms, Maximum = 0ms, Average = 0ms')
        else:
            maximum = max(int(-1 if time1[1:] == "" else time1[1:]), int(-1 if time2[1:] == "" \
else time2[1:]), int(-1 if time3[1:] == "" else time3[1:]), int(-1 if time4[1:] == "" else \
time4[1:]))
            minimum = min(int(1000000 if time1[1:] == "" else time1[1:]), int(1000000 \
if time2[1:] == "" else time2[1:]), int(1000000 if time3[1:] == "" else time3[1:]), \
int(1000000 if time4[1:] == "" else time4[1:]))
            print('    Minimum = %dms, Maximum = %dms, Average = %dms' %(minimum, maximum,\
 (int(0 if time1[1:] == "" else time1[1:]) + int(0 if time2[1:] == "" \
else time2[1:]) + int(0 if time3[1:] == "" else time3[1:]) + int(0 if time4[1:] == "" \
else time4[1:])) / (abs(intf - 4))))
main()
