"""Muddled Menu"""
def main(cando):
    """Muddled Menu"""
    while True:
        menu = input()
        if menu == 'DONE' or menu == 'CLOSED':
            break
        elif menu == "SOMETHING'S WRONG":
            cando.clear()
        elif menu[:5] == "Can't":
            cando.remove(menu[10:])
        elif menu[-1] == 'N':
            cando.append(menu[:-3])
        else:
            num = menu.index('#')+1
            cando.insert(int(menu[num:])-1, menu[:num-2])
    if menu == 'CLOSED':
        cando.clear()
    print('Full Course:', cando, 'Reversed:', cando[::-1])
main([])
