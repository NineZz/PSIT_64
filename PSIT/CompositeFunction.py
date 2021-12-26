"""CompositeFunction"""
def main():
    """function input"""
    number = float(input())
    print("%.2f"%func_f(func_g(number)))
    print("%.2f"%func_g(func_f(number)))

def func_f(num_x):
    """function f"""
    return num_x*2

def func_g(num_x):
    """function g"""
    return (num_x/2)+1

main()
