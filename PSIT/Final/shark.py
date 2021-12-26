"""SHARK"""
def zone(name_fish):
    """check shark zone"""
    if name_fish == "BULL SHARK":
        return "THE SHALLOW ZONE"
    elif name_fish == "CHAIN CATSHARK" or name_fish == "GREAT WHITE SHARK"\
        or name_fish == "GUMMY SHARK" or name_fish == "BLUE SHARK"\
            or name_fish == "MAKO SHARK":
        return "THE TWILIGHT ZONE"
    elif name_fish == "FRILLED SHARK" or name_fish == "GOBLIN SHARK"\
        or name_fish == "SIXGILL SHARK" or name_fish == "GREENLAND SHARK"\
            or name_fish == "COOKIECUTTER SHARK":
        return "THE MIDNIGHT ZONE"
    elif name_fish == "MEGAMOUTH SHARK":
        return "THE ABYSSAL ZONE"
def shark():
    """function shark"""
    name_fish = input()
    if "SHARK" in name_fish:
        print(zone(name_fish))
    else:
        print("ZONE JAI MA KLUNG RAK DUAY KAN MAI.")
shark()
