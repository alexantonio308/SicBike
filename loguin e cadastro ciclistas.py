import biblioteca
opcao = ""
dados_ciclistas = []
gerador_matricula = 1000


while opcao != "x":
   biblioteca.clear()
   biblioteca.inicial()
   modalidade = []
   nome = []
   email = []
   celular = []
   cpf = []
   rg = []
   dataNascimento = []
   contador_MATRICULA = []
   if len(dados_ciclistas) > 0:
      print("sua matricula é ",gerador_matricula,"decore para logar de acordo com o usuario")
   opcao = input("digite sua opção:")
   #biblioteca.clear() limpa a tela
   biblioteca.clear()
   
   if opcao == "1":
      print("Cadastro Ciclista\n")
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
         
      biblioteca.clear()    
      print("Dados do Usuario\n")
      nome.append(input("digite seu nome:"))
      email.append(input("Digite seu email:"))
      celular.append(input("digite seu numero de celular ou telefone:"))

      biblioteca.clear()
      print("\nDados Pessoais\n")
      cpf.append(input("digite seu cpf:"))
      rg.append(input("digite seu RG:"))
      dataNascimento.append(input("digite sua data de nascimento:"))
      #-------------------------------------------------------------------------
      gerador_matricula += 1
      contador_MATRICULA.append(gerador_matricula)
      dados = modalidade + nome + email + celular + cpf + rg + dataNascimento + contador_MATRICULA
      dados_ciclistas.append(dados)
      print(dados_ciclistas)
      
      arquivo = open("ciclistas.txt","w")
      print(contador_MATRICULA,file = arquivo)
      for x in dados_ciclistas:
          print(x,file = arquivo)
      arquivo.close()
      
      
      #opçao de loguin
   elif opcao == "2":
      arq = open("dados_loguin.ewe","w")
      for dado_ciclista in dados_ciclistas:
          for w in dado_ciclista:
              print(w,file = arq)
      arq.close()
      #__________Criando arquivo que contem os itens das sublistas listados para verificação do for e verificando pela função loguin__
      print("loguin de usuario")
      arq = open("dados_loguin.ewe","r")
      nome_matri = arq.read()
      matricula = (input("digite sua matricula:"))
      cpf = input("digite seu cpf:")
      if matricula in nome_matri and cpf in nome_matri:
         biblioteca.clear() 
         print("longado")
         print("[1] Apagar cadastro")
         print("[2] Imprimir cadastro")
         escolha = input("escolha sua opção:")
         if escolha == "1":
            verificacao = input("realmente deseja apagar sua matricula?[s/n]")
            if verificacao == "s":
               del dados_ciclistas[int(matricula)-int(1001)]
               arquivo = open("ciclistas.txt","w")
               for x in dados_ciclistas:
                  print(x,file = arquivo)
               arquivo.close()

     


print ("\n" * 130) 
print("Saindo do sistema...")
   
