import biblioteca_entradas_telas as tel
import arquivos as arq
import pickle
contador = 10
contador = arq.leito_cotador(contador)
opcao = ""


while opcao != "x":
    tel.clear()
    tel.menu_inicial()
    opcao = input("digite sua opção:")
    if opcao == "1":
        dados = []
        tel.input_dados(dados)
        contador += 1
        arq.conta_matricula(contador)
        arq.matricula_creator(dados,contador)
        print("sua matricula é %s" %contador,"decore!")
        tel.press()
        
    elif opcao == "2":
        tel.clear()
        n_matricula = input("digite sua matricula:") 
        usuario = arq.matricula_read(n_matricula)
        arq.listar_matricula(usuario)

    
