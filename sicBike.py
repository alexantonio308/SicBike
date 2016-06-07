import biblioteca_entradas_telas as tel
import arquivos as arq
import os

cont = arq.contador()

tel.sicbike()
opcao = ""
while opcao != "x":
    tel.clear()
    tel.menu_inicial()
    nome = ""
    opcao = input("digite sua opção:")
    if opcao == "1":
        cont += 1
        arq.n_matricula(cont)
        dados = []
        tel.input_dados(dados)
        arq.criador_matricula(dados,dados[0],cont)
        print("\nSeu login é %s, sua matricula é " %dados[0],cont)
        tel.press()
                
    elif opcao == "2":
        opcao2 = True
        tel.clear()
        tel.login()
        nome = input("digite seu nome:")
        matricula = input("Digite sua matricula:")
        nome = tel.diretorio(nome,matricula)
        try:
            with open(nome, 'rb') as f:
                while opcao2:
                    tel.clear()
                    tel.tela_login()
                    opcao2 = input("digite sua opção:")
                    usuario = arq.leitor_de_matricula(nome)
                    if opcao2 == "1":            
                        arq.verificar_matricula(usuario)
                    if opcao2 == "2":
                        usuario = tel.editar_matricula(usuario)
                        arq.criador_matricula(usuario,usuario[0])
                    if opcao2 == "x":
                        opcao2 = False                                          
        except IOError:
            print('Ciclista não encontrado!')
            tel.press()

    elif opcao == "3":
        arq.excluir_matricula()
        print("Ciclista escluido")
        tel.press
                
    elif opcao == "4":
        arquivos = os.listdir('ciclistas/')
        arq.listar_ciclistas(arquivos)   
    else:   
        tel.press()
        
tel.time_sleep()

