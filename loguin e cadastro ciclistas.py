import biblioteca_listagem as biblioteca
import telas as tela

opcao = ""
dados_ciclistas = []
gerador_matricula = 1000


while opcao != "x":
   tela.clear()
   tela.inicial()
   opcao = input("digite sua opção:")
   
   tela.clear()
   modalidade = []
   nome = []
   email = []
   celular = []
   cpf = []
   rg = []
   dataNascimento = []
   contador = []
   
   if opcao == "1":
      print("Cadastro Ciclista\n")
      print("*1 Master\n*2 Junior\n*3 Turismo\n*4 Peso pesado")
      tela.cad_modalidade(modalidade)
         
      tela.clear()
      tela.dados_usuario(nome,email,celular)

      tela.clear()
      tela.dados_pessoais(cpf,rg,dataNascimento)
      #-------------------------------------------------------------------------
      gerador_matricula += 1
      contador.append(gerador_matricula)
      dados = modalidade + nome + email + celular + cpf + rg + dataNascimento + contador
      #______________________________________________________________________________
      dados_ciclistas.append(dados)
      #__________________________________________________________________________________
      arquivo = open("ciclistas.txt","w")
      biblioteca.listar_lista(dados_ciclistas,contador,arquivo)
      arquivo.close()
      tela.show_matricula(gerador_matricula)
   
   #opçao de loguin
   elif opcao == "2":
      arq = open("dados_loguin.ewe","w")
      biblioteca.listar_lista2(dados_ciclistas,contador,arq)
      arq.close()
      #_____________________________________________________
      print("loguin de usuario")
      arq = open("dados_loguin.ewe","r")
      nome_matri = arq.read()
      matricula = (input("digite sua matricula:"))
      cpf = input("digite seu cpf:")
      local_matricula = int(matricula)-int(1001)
      
      if matricula in nome_matri and cpf in nome_matri:
         tela.clear()
         escolha = ""
         while escolha != "x":
            tela.clear()
            tela.tela_loguin()
            escolha = input("escolha sua opção:")
            
            
            if escolha == "1":
               verificacao = input("realmente deseja apagar sua matricula?[s/n]")
               if verificacao == "s":
                  del dados_ciclistas[local_matricula]
                  arquivo = open("ciclistas.txt","w")
                  biblioteca.listar_lista(dados_ciclistas,contador,arquivo)
                  arquivo.close()

            elif escolha == "2":
               arquiv = open("Matricula.txt","w")
               tela.imprimir_matricula(dados_ciclistas[local_matricula],arquiv)
               arquiv.close()
               tela.clear()
               print("arquivo de Matricula gerado")

            elif escolha == "3":
               tela.clear()
               tela.verificar_matricula(dados_ciclistas[local_matricula])
            
            else:
               print("opção invalida")

   else:
      print("opção invalida\n")


tela.clear() 
print("Saindo do sistema...")
   
