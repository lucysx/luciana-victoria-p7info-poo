queue = []
a = True
while a:
    element = input("Digite 'sair' para encerrar\nInsira um elemento na fila:")
    if element != "sair":
        queue.append(element)
    else:
        a = False

try:
    queue = list(map(int, queue))
except:
    pass

print("\nFila:", queue,"\n")

for i in range(len(queue)):
    fora = input("Excluir elemento? Digite 'sim' ou 'nao': ")
    if fora == "sim":
        print("Elemento excluido:", queue.pop(0))
        print(queue, "\n")
    elif fora == "nao":
        break
    else:
        print("Digite 'sim' ou 'nao'")

print("\nFila:", queue)
