from datetime import date

#CLASSE PESSOA ENDERECO
class Endereco:
  def __init__(self, logradouro='', numero='', endereco=None, endereco_comecial=False):
    self.lagradouro = logradouro
    self.numero = numero
    self.endereco_comecial = endereco_comecial

#CLASSE PESSOA
class Pessoa:
  def __init__(self, nome='', rendimento=0.0, endereco=None):
    self.nome = nome
    self.rendimento = rendimento
    self.endereco = endereco

  def calcula_imposto(self, rendimento):
    return rendimento
#CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
  def __init__(self, cpf='', nome='', rendimento=0.0, endereco=None):
    super().__init__(nome, rendimento=0.0, endereco=None, cpf='', dataNacimento=None)
    if endereco is None:
      endereco = Endereco()

    if dataNacimento is None:
      dataNacimento = date.today()

    super().__init__(nome, rendimento, endereco)
    #chama o construtor da superclass pessoa para inicializar os atribrutos herdado




    #Atributos da propria classe
    self.cpf = cpf
    self.dataNacimento = dataNacimento

  def calcula_imposto(self, rendimento: float) -> float:
      if rendimento <= 1500: #sem imposto para redimento
        return 0
      elif 1500 < rendimento <= 3500:
        return rendimento * 0.2
      elif 3500 < rendimento <= 6000:
        return (rendimento / 100) * 3.5
      else:
        return rendimento * 5
#CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
  pass


