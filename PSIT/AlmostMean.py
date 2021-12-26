"""AlmostMean"""
def main(num, ave, score, val, data):
    """AlmostMean"""
    for _ in range(num):
        student = input()
        val.append(student)
        score.append(float(student[9:]))
        ave += float(student[9:])
    data.extend(score)
    score.append(ave/num)
    score.sort()
    nearest = score[(score.index(ave/num))-1]
    print(val[data.index(nearest)])
main(int(input()), 0, [], [], [])
