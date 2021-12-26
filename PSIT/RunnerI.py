"""Runner"""
def main(distance, speed, winner, w_time):
    """Runner"""
    for i in range(int(input())):
        runner = input().split()
        r_time = (distance-int(runner[1]))/int(runner[0])
        if (i == 0) or (r_time < w_time) or (r_time == w_time and int(runner[0]) > int(speed[0])):
            winner = i+1
            w_time = r_time
            speed = runner
    print(winner)
main(int(input()), [], 0, 0)
