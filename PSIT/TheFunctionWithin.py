"""function within"""
def main():
    """function input"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numd = float(input())

    print(func_f(func_f(numa)))
    print(func_g(func_f(numa-numb)))
    print(func_h(func_f(numa+numb), func_f(numa+numc), func_g(func_f(numd**2))))
    print(func_i(func_h(func_f(numa+numb), func_f(numa-numc), func_g(func_f(numd**2))), \
        func_g(func_f(numa-numb)), func_f(func_f(func_f(func_f(func_f(numc))))), numd**8))

def func_f(numx):
    """function f"""
    return 2*numx

def func_g(numx):
    """function g"""
    return 3*numx**4-numx**3+2*numx**2+10

def func_h(numx, numy, numz):
    """function h"""
    return (numz+numx)**2-numx*numy+numy**2

def func_i(numa, numb, numc, numd):
    """function i"""
    return (numa**2+numb**2-numc**2)/(numd**2-2*numa*numd+2*numa)

main()
