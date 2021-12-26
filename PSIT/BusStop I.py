""""BusStop I"""

def main(num1, num2):
    """"BusStop I"""
    lst, pai, person, count = [], [], [], 0
    for _ in range(num2):
        st1 = str(input()).split()
        paione = int(st1[0])
        pai.append(int(st1[0]))
        st1.pop(0)
        lst.append([paione, st1])
    for i in sorted(pai):
        checkpai = sorted([a for a in pai if int(a) > i])
        lstpai = [a for a in lst if int(a[0]) == int(i)]
        for _ in range(5):
            for j in person:
                if int(j) == int(lstpai[0][0]):
                    count += 1
                    person.remove(int(j))
        for j in lstpai[0][1]:
            if len(person) < num1 and checkpai.count(int(j)) == 1:
                person.append(int(j))
    print(count)
main(int(input()), int(input()))
