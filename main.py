class Teste():
    def __init__(self, funcao,resultado):
        self.funcao = funcao
        self.resultado = resultado

    def Iniciar(self):
        if self.funcao() == self.resultado:
            print("Passou no teste")
        else:
            print("Nâo passou no teste.")


def FuncaoQueRetornaUmNumero():
    return 3

teste = Teste(FuncaoQueRetornaUmNumero,2)
teste.Iniciar()
