"""Donut"""
def main():
    """function compute"""
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    pack = num_b+num_c
    price_pack = num_a*num_b

    pack_need = num_d//pack
    remain_need = num_d%pack

    if remain_need > 0:
        #Scenario 1
        pack_need_1 = pack_need+1
        price_s1 = pack_need_1*price_pack

        #Scenario 2
        buy_remain = num_d%pack
        price_s2 = pack_need*price_pack+buy_remain*num_a

        if price_s1 < price_s2:
            print("%d %d"%(price_s1, pack_need_1*pack))
        elif price_s2 < price_s1:
            print("%d %d"%(price_s2, num_d))
        else:
            if pack_need_1*pack > num_d:
                print("%d %d"%(price_s1, pack_need_1*pack))
            else:
                print("%d %d"%(price_s1, num_d))
    else:
        print("%d %d"%(pack_need*price_pack, pack_need*pack))
main()
