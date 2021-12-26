"""Cat Parade"""
def add(breed, check):
    """add"""
    cat = sorted(breed)
    for i in range(len(cat)):
        num = cat.count(cat[i])
        if check != cat[i]:
            print(cat[i], (breed.index(cat[i]))+1, num)
        check = cat[i]
def main(allcat):
    """Cat Parade"""
    while True:
        cat = input()
        if cat == 'END':
            break
        if cat.find(', ') != -1:
            cats = cat.split(', ')
            allcat.extend(cats)
        elif cat == "IT'S A DOG":
            allcat.pop()
        else:
            allcat.append(cat)
    add(allcat, '')
main([])
