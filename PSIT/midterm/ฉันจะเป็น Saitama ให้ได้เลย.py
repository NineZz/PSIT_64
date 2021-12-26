"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def find_mx(num_a, num_b):
    """mx"""
    if num_a > num_b:
        return num_a
    return num_b

def main():
    """ฉันจะเป็น Saitama ให้ได้เลย"""
    push_up = int(input())
    sit_up = int(input())
    squash = int(input())
    run = int(input())
    rep_p = int(input())
    rep_s = int(input())
    rep_r = int(input())
    rep_sq = int(input())
    day_p = push_up/rep_p
    day_s = sit_up/rep_s
    day_r = run/rep_r
    day_sq = squash/rep_sq
    day_mx = find_mx(find_mx(find_mx(day_p, day_s), day_r), day_sq)
    print(math.ceil(day_mx))
main()
