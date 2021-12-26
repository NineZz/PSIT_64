"""Difference"""
def main(numa, numb, seta, setb):
    """Difference"""
    for _ in range(numa):
        seta.add(int(input()))
    for _ in range(numb):
        setb.add(int(input()))
    ans = sorted(seta-setb)
    print(*ans)
main(int(input()), int(input()), set(), set())
