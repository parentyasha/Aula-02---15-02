class Atividade:
    status="Deu certo"
    def __init__(self,nomeAti,prioridade,pessoa,projeto,dataIni,dataFim):
        self.nomeAti=nomeAti
        self.prioridade=prioridade
        self.pessoa=pessoa
        self.projeto=projeto
        self.dataIni=dataIni
        self.dataFim=dataFim

    def finalizar_atividade(self):
        self.status="finalizada"

    def __str__(self):
        return self.nomeAti

class Pessoa:
    def __init__(self,nomeP,dataNasc):
        self.nomeP=nomeP
        self.dataNasc=dataNasc

    def __str__(self):
        return "Pessoa:"+self.nomeP+"Data Nasc.:"+self.dataNasc

    def __str__(self):
        return self.nomeP

class Projeto:
    def __init__(self,nomeProj,dataIni,dataFim):
        self.nomeProj=nomeProj
        self.dataIni=dataIni
        self.dataFim=dataFim

    def __str__(self):
        return self.nome

p=Projeto("Projeto 1", "15-02-2019", "31-12-2019")
print(p.nomeProj)
print(p.dataIni)
print(p.dataFim)
"\n"
pe=Pessoa("Lucas","23-02-2019")
print(pe.nomeP)
print(pe.dataNasc)
"\n"
a=Atividade("Ativade 1","1",pe,p,"17-02-2019","19-02-2019")
print(a.nomeAti)
print(a.prioridade)
print(a.pe)
print(a.p)


print(a.status)
a.finalizar_atividade()
print(a.status)
