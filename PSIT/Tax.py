"""Tax"""
def check(car_cc):
    """cc"""
    if car_cc <= 600:
        return car_cc*0.5
    if 601 <= car_cc <= 1800:
        return (600*0.5) + ((car_cc-600)*1.5)
    if car_cc > 1800:
        return (600*0.5) + (1200*1.5) + ((car_cc-1800)*4)

def main():
    """tax"""
    years = int(input())
    car_cc = int(input())
    if years < 6:
        print('%.2f'%check(car_cc))
    elif years == 6:
        print('%.2f'%(check(car_cc)*90/100))
    elif years == 7:
        print('%.2f'%(check(car_cc)*80/100))
    elif years == 8:
        print('%.2f'%(check(car_cc)*70/100))
    elif years == 9:
        print('%.2f'%(check(car_cc)*60/100))
    elif years >= 10:
        print('%.2f'%(check(car_cc)*50/100))
main()
