class Diario():
    def __init__(self, id, *notas):
        self.id = id
        self.notas = list(map(lambda x : x.__dict__, notas))

    def resultado(self):
        print("Alunos:")
        for a in self.notas:
            print(a["nome"])
        print("Total:", sum(list(map(lambda x : x["nota"], self.notas))))

class notaAluno():
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

