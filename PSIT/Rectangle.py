"""Rectangle"""
def area():
    """function find area"""
    height = int(input())
    weight = int(input())
    print(height*weight)
    print(perimeter(height, weight))

def perimeter(num_1, num_2):
    """function find perimeter"""
    ans = (num_1*2)+(num_2*2)
    return ans
area()
