import biblioteca
opcao = ""
# dados_ciclistas tem as listas de cadastros dos usuarios...
dados_ciclistas = []


while opcao != "x":
   #biblioteca.inicial imprime o menu 
   biblioteca.inicial()
   opcao = input("digite sua opção:")
   modalidade = []
   nome = []
   email = []
   celular = []
   cpf = []
   rg = []
   dataNascimento = []
   #todos os dados das listas acima vão para uma lista dados que vira sub-lista de dados_ciclistas
   if opcao == "1":
      print("Cadastro Ciclista\n")
      #de acordo com a opção do usuario a modalidade é adicionada ao cadastro dele
      print("*1 Master\n*2 Junior\n*3 Turismo\n*4 Peso pesado")
      escolha = input("\nescolha sua modalidade:")
      if escolha == "1":
         modalidade.append("Ciclista Master")
      elif escolha == "2":
         modalidade.append("Ciclista Junior")
      elif escolha == "3":
         modalidade.append("Modo Turismo")
      elif escolha == "4":
         modalidade.append("Ciclista Peso pesado")
      else:
         ("opção invalida")
         
      #________________adicionando dados nas listas_______________________________________________________________________________________     
      print("\ndados do usuario\n")
      nome.append(input("digite seu nome:"))
      email.append(input("Digite seu email:"))
      celular.append(input("digite seu numero de celular ou telefone:"))

      print("\nDados pessoais\n")
      cpf.append(input("digite seu cpf:"))
      rg.append(input("digite seu RG:"))
      dataNascimento.append(input("digite sua data de nascimento:"))
      #-------------------------------------------------------------------------

      #____________________________criando sublista e adicionando a lista de dados dos ciclistas cadastrados_______________________________
      dados = modalidade + nome + email + celular + cpf + rg + dataNascimento
      dados_ciclistas.append(dados)
      print(dados_ciclistas)
      
      #____________________________criando arquivo que possui listas dos dados de cada usuario_____________________________________
      arquivo = open("ciclistas.txt","w")
      for x in dados_ciclistas:
          print(x,file = arquivo)
      arquivo.close()  
           
   # opçao de loguin
   elif opcao == "2":
      #__________Criando arquivo que contem os dados do usuario percorridos_______
      arq = open("dados_loguin.ewe","w")
      for y in dados_ciclistas:
          for w in y:
              print(w,file = arq)
      arq.close()
      #__________Criando arquivo que contem os itens das sublistas listados para verificação do for e verificando pela função loguin__
      print("loguin de usuario")
      arq = open("dados_loguin.ewe","r")
      nome_cpf = arq.read()
      nome = str(input("digite seu nome:"))
      cpf = str(input("digite seu cpf:"))
      biblioteca.loguin(nome_cpf,nome,cpf)

   else:
      print("opção invalida")

     



print("Saindo do sistema...")
   
