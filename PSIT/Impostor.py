"""Impostor"""

def main():
    """Impostor"""
    imposter, dictfew, lst, life, dead = 0, {}, [], {}, {}
    while True:
        fewza = str(input())
        if fewza == "Start":
            break
        dictfew[fewza.split('"')[1]] = fewza.split('"')[3]
    while True:
        fewza = str(input())
        if fewza == "End":
            break
        lst.append(fewza)
    for _, value in dictfew.items():
        if value == "Impostor":
            imposter += 1
    for key, value in dictfew.items():
        if key not in lst:
            life[key] = value
    for fewzax in lst:
        if dictfew[fewzax] == "Impostor":
            imposter -= 1
        dead[fewzax] = dictfew[fewzax]
    print('%d Impostor Remains' % (imposter))
    print('***Alive***')
    for key in sorted(life):
        print(key + " : " + life[key])
    print('***Dead***')
    for key in sorted(dead):
        print(key + " : " + dead[key])
main()
