"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0      

    def itemLinha(self, item):
        linha = list()
        for x in [item._sequencial, item._descricao, item._quantidade, item._valorUnitario, item._valorItem]:
            linha.append(str(x))
        return linha

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor

    def imprimirNotaFiscal(self):
           data = datetime.datetime.now().strftime("%d-%m-%Y")       
           linha= '-' * 111
           linha2 = '_' * 111
           formatacao_nota = '{}\n' \
           'NOTA FISCAL{:>100}\n' \
           'Cliente:{:>4}{:>4}Nome: {}\n' \
           'CPF/CNPJ: {}\n' \
           '{}\n' \
           'ITENS\n' \
           '{}\n' \
           'Seq{:>3}Descrição{:>52}QTD{:>7}Valor Unit{:12}Preço\n' \
           '{}  {}    {}     {}     {}'.format(linha,
                                              data,
                                              self._cliente._codigo, ' ', self._cliente._nome,
                                              self._cliente._cnpjcpf,
                                              linha,
                                              linha,
                                              ' ', ' ', ' ', ' ',
                                              '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)
           print(formatacao_nota)
           for item in self._itens:
             print("{:4s} {:56s}      {:>3s}       {:>10s}       {:>15s}".format(*self.itemLinha(item)))
             print(linha2)
             self.calcularNotaFiscal()
           print("Valor Total: " + str(self.valorNota))