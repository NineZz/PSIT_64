"""Kabata"""
def main():
    """Kabata"""
    for _ in range(int(input())):
        val = input()
        if val.find('baka') != -1:
            val = val.replace('baka', '0')
        if val.find('bakka') != -1:
            val = val.replace('bakka', '')
        if val.find('ka') != -1:
            val = val.replace('ka', '')
        if val.find('ba') != -1:
            val = val.replace('ba', '')
        if val.find('ta') != -1:
            val = val.replace('ta', '')
        print('no' if len(val) != 0 else 'yes')
main()
