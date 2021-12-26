"""RemoveTag"""
def main(val):
    """RemoveTag"""
    while True: #Title This is a
        if val.find('>') == -1:
            break
        no1 = val.index('<') #0
        no2 = val.index('>') #3
        val = val.replace(val[no1:no2+1], ' ')
                        # val[0:4]
                        # Title</h1><p>This is a
    print(val.split())
main(input())
