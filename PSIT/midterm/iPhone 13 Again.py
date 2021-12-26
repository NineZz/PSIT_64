"""iPhone 13 Again"""
def model(iphone):
    """model"""
    if iphone == "iPhone 13 mini":
        return 25900
    elif iphone == "iPhone 13":
        return 29900
    elif iphone == "iPhone 13 Pro":
        return 38900
    elif iphone == "iPhone 13 Pro Max":
        return 42900
    else:
        return 0

def price(iphone, rom):
    """price"""
    base = model(iphone)
    if base == 0:
        return "Not Available"
    elif rom == "128 GB":
        return base
    elif rom == "256 GB":
        return base+4000
    elif rom == "512 GB":
        return base+12000
    elif rom == "1 TB" and base >= 38900:
        return base+20000
    else:
        return "Not Available"

def main():
    """iPhone 13 Again"""
    iphone = input()
    rom = input()
    print(price(iphone, rom))
main()
