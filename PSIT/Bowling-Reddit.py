""""Bowling-Reddit"""
def main(frames):
    """"Bowling-Reddit"""
    balls = list(map(lambda x: 10 if (x == 'X' or x == '/') \
        else 0 if x == '-' else int(x), "".join(frames.split())))
    ball_1 = 0
    score = 0
    for _ in range(10):
        if balls[ball_1] == 10:
            ball_1 += 1
            score += 10 + balls[ball_1] + balls[ball_1 + 1]
        elif balls[ball_1 + 1] == 10:
            ball_1 += 2
            score += 10 + balls[ball_1]
        else:
            score += balls[ball_1] + balls[ball_1 + 1]
            ball_1 += 2
    return score
print(main(str(input())))
