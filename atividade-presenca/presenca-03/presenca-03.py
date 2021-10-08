stack = []
a = True
while a:
    element = input("Para encerrar digite 'sair'\nInsira um elemento na pilha:")
    if element != "sair":
        stack.append(element)
    else:
        a = False

try:
    stack = list(map(int, stack))
except:
    pass

print("\nPilha:", stack,"\n")

for i in range(len(stack)):
    fora = input("Excluir elemento? Digite S ou N: ").title()
    if fora == "S":
        print("Elemento retirado:", stack.pop())
        print(stack, "\n")
    elif fora == "N":
        print("")
        break
    else:
        print("Digite S ou N")

print("Pilha:", stack)
