def somaImposto(custo, taxa):
    custo += custo * (taxa / 100)
    return custo

def taxaImposto():
    custo = float(input("Digite o valor do item: "))
    taxa = float(input("Digite a porcentagem da taxa: "))
    return custo, taxa

def code():
    custo, taxa = taxaImposto()
    custo = somaImposto(custo, taxa)
    print(f"O custo final do item incluindo imposto é de: R${custo:.2f}")

code()
