class Evento:
    def __init__(self,nomeEvento,dataIni,dataFim):
        self.nomeEvento=nomeEvento
        self.dataIni=dataIni
        self.dataFim=dataFim

class Pessoa:
    def __init__(self,nomeP,evento):
        self.nomeP=nomeP
        self.evento=evento

class Artigos:
    def __init__(self,nome):
        self.nome=nome

class PessoaFisica(Pessoa):
    def __init__(self,CPF):
        self.CPF=CPF

class PessoaJuridica(Pessoa):
    def __init__(self,CNPJ):
        self.CNPJ=CNPJ

class Autor(Pessoa):
    def __init__(self,qtObras):
        self.numObras=qtObras

class AutorArtigo:
    def __init__(self,autor,artigo):
        self.autor=autor
        self.artigo=artigo

e=Evento("aula de ingles","17/02/19","19/02/19")

pe=Pessoa("Lucas",e)

ar=Artigos("como ser bom em ingles")

pef=("111.222.333-01")

pej=("444.555.666-02")

au=Autor("5")

aa=AutorArtigo(autor,artigo)
