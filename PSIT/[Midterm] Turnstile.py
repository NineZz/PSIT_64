"""[Midterm] Turnstile"""
def main():
    """[Midterm] Turnstile"""
    log_act = ""
    people = 0
    while True:
        action = input()
        if action == "END":
            break
        log_act += action
        if log_act == "CP":
            people += 1
        if len(log_act) == 2:
            log_act = log_act[1:]
    print(people)
main()
