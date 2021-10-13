x = 0
caractere = "-"
maiorPalavra = ""
while True:
    print("Para encerrar digite 0\nEscreva uma frase: ")
    frase = input().split()
    tamanhos = []
    if frase == ['0']:
        print("Finalizando")
        break
    for i in frase:
        tamanhos.append(str(len(i)))
        if len(i) >= x:
            x = len(i)
            maiorPalavra = i
    print(caractere.join(tamanhos))

print("A maior palavra é: %s" % maiorPalavra)
