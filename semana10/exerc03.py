def mult(n):
    result = n * 2
    print("O resultado é:",result)
    

def numb():
    n = float(input("Digite o número: "))
    return n

def main():
    n = numb()
    mult(n)

main()
