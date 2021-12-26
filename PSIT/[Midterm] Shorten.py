"""[Midterm] Shorten"""
def main():
    """[Midterm] Shorten"""
    start = None
    prev = None
    answer = ""
    while True:
        number = int(input())
        if number == -1:
            break

        if prev == None:
            start = number
            prev = number
            continue
        else:
            if prev != number-1:
                if start == prev:
                    answer += "%d, "%start
                else:
                    answer += "%d-%d, "%(start, prev)
                start = number
                prev = number
            else:
                prev = number
    if start != None:
        if start == prev:
            answer += "%d, "%start
        else:
            answer += "%d-%d, "%(start, prev)

    print(answer.strip(", "))
main()
