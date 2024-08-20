#1 - pessoa fisica / 2 - pessoa juridica /3 - sair
#1 - castrar pessoa fisica / 2 - listar pessoa fisica / 3 sair
from datetime import date, datetime
from Pessoa import PessoaFisica
from Pessoa import Endereco, PessoaFisica

def main():
  lista_pf = []
  while True:
    opcao = input('1 - pessoa fisica / 2 - pessoa juridica /3 - sair ')
    if opcao == '1':
      while True:
        opcao = input('1 - castrar pessoa fisica / 2 - listar pessoa fisica / 3 sair ')
        if opcao == '1':
          novopf = PessoaFisica()
          novo_end_pf = Endereco()

          novopf.nome = input('Digite o nome da pessoa fisica: ')
          novopf.cpf = input('Digite o cpf da pessoa fisica: ')
          novopf.rendimento = float(input('Digite o rendimento da pessoa fisica: '))

          data_nacimento = input('Digite a data de nascimento da pessoa fisica: ')
          novopf.dataNacimento = datetime.strptime(data_nacimento, '%d/%m/%Y').date()
          idade = (date.today() - novopf.dataNacimento).days // 365
          if idade < 18:
            print('Pessoa fisica menor de idade')
          else:
            print('Pessoa fisica maior de idade')
            continue
          
          novo_end_pf.lagradouro = input('Digite o logradouro da pessoa fisica: ')
          novo_end_pf.numero = input('Digite o numero da pessoa fisica: ')
          end_comercial = input('A pessoa fisica possui endereco comercial? (S/N) ')
          novo_end_pf.endereco_comecial = end_comercial.strip().upper() == 'S' 

          novopf.endereco = novo_end_pf

          lista_pf.append(novopf)
          print('Pessoa fisica cadastrada com sucesso!')
          continue
        elif opcao == 2:
            if lista_pf:
             for cada_pf in lista_pf:
              print(f'Nome: {cada_pf.nome}')
              print(f'CPF: {cada_pf.cpf}')
              print(f'endereço: {cada_pf.endereco.lagradouro}, N{cada_pf.endereco}')
              print(f'Data de nascimento: {cada_pf.dataNacimento.strftime('%d/%m/%y')}')
              print(f'Imposto: {cada_pf.calcula_imposto(cada_pf.rendimento)}')
              print('Digite 0 para sair')
              input()
            else:
                print('Nenhuma pessoa fisica cadastrada')
          
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opção invalida')

    elif opcao == 2:
      print('Fucionalidade para pessoa juridica nao implementas')
      pass

    elif opcao == 0:
      print('obrigado por utilizar o nosso sistema valeu')
      break
    else:
      print('opacao invalida por favor digita uma das opcao validas')

if __name__=='__main__':
  main()#chama a funcao principal
  