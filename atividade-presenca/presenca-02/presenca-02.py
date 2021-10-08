def printDecimal(dec):
    return dec

def printOctal(octl):
    octal = oct(octl)
    return octal

def printHexadecimal(hexa):
    hexadecimal = hex(hexa)
    return hexadecimal

def printBinario(binar):
    binario = bin(binar)
    return binario

def imprimaTela(n, func1, func2, func3, func4):
    return ("""
Decimal       Octal     Hexadecimal           Binario
------------- --------- --------------------- -----------------
{:d} {:>15s} {:>9s} {:>26s}""".format(func1(n), func2(n), func3(n), func4(n)))


for i in range(0, 256):
    print(imprimaTela(i, printDecimal, printOctal, printHexadecimal, printBinario))