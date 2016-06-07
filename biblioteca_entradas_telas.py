import pickle
import time
import re

def clear():
    print ("\n" * 50)

def press():
    ir = input("Precione enter para continuar!")

def sicbike():
    clear()
    print("                                      BEM VINDO            ")
    print("                                      Sic Bike             ")
    print("                           CADASTRO DE CICLISTAS OLIMPICOS")
    comecar = input("\n                            Aperte ENTER para comecar")
    
def menu_inicial():
   print("------------------------SicBIKE-----------------------")
   print("[                  [1] Cadastrar                      ]")
   print("[                  [2] Login                          ]")
   print("[                  [3] Apagar cadastro                ]")
   print("[                  [4] Listar ciclistas               ]")
   print("[                  [x] Sair                           ]")
   print("------------------------------------------------------")

def diretorio(parametro,cont):
    nome = parametro+str(cont)
    nome = "ciclistas/%s.txt" %str(nome)
    return nome
    
def login():
    print("_____________________LOGIN CICLISTA____________________\n")

def tela_editar():
    print("_______________________EDITAR__________________________\n")

def tela_login():
    print("[1] Verificar matricula")
    print("[2] Editar Matricula")
    print("[x] Voltar")    

def validar_cpf(cpf):
    while len(cpf) < 14 or len(cpf) > 14 or cpf[3] != "." or cpf[7] != "." or cpf[11] != "-":
        print("CPF invalido")
        cpf = (input("Digite seu CPF ex:(703.041.864-23):"))

def validar_email(email):
    validade = True
    while validade:
        email = input("Coloque seu e-mail ex:(usuario@hotmail.com):")
        match = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
        if match:
            print("Email valido ", match.group())
            return email
            validade = False
        else:
            print("email invalido!")        

def validar_data(data):
    while len(data) < 0 or len(data) > 10 or data[2] != "/" or data[5] != "/":
        print("data invalida")
        data = input("Data de nascimento ex:(03/06/2016):")
        
def modalidade(modo):
    clear()
    print("________________CADASTRO__________________\n")
    print("Modalidades Olimpicas\n*1 Pista\n*2 Estrada\n*3 Mountain bike\n*4 BMX")
    escolheu = True
    escolha = ""
    while escolheu:
        escolha = input("\nEscolha sua modalidade:")
        if escolha == "1":
           modo = ("Pista")
           escolheu = False
        if escolha == "2":
           escolheu = False
           modo = ("Estrada")
        if escolha == "3":
           escolheu = False
           modo = ("Mountain bike")
        if escolha == "4":
           escolheu = False
           modo = ("BMX")
    return modo   
        
def input_dados(lista):
    modo = ""
    email = ""
    modo = modalidade(modo)    
    print("______DADOS PESSOAIS_____")
    nome = (input("Nome:"))
    email = validar_email(email)
    
    cpf = (input("Digite seu CPF ex:(703.041.864-23):"))
    validar_cpf(cpf)
    
    data = input("Data de nascimento ex:(03/06/2016):")
    validar_data(data)
    lista.append(nome)
    lista.append(cpf)
    lista.append(email)
    lista.append(data)
    lista.append(modo)

def editar_matricula(parametro): 
    continua = True
    while continua:
        clear()
        print("Cilcista %s" %parametro[0])
        print("\n[1] Cpf\n[2] e-mail\n[3] Data de Nascimento\n[4] Modalidade\n[x] Voltar")
        escolha = input("\nEscolha sua opção:")
        if escolha == "1":
            tela_editar()
            parametro[1] = (input("Digite seu CPF ex:(703.041.864-23):"))
            validar_cpf(parametro[1])
        if escolha == "2":
            tela_editar()
            parametro[2] = tel.validar_email(parametro[2])
        if escolha == "3":
            parametro[3] = input("Data de nascimento ex:(03/06/2016):")
            validar_data(parametro[3])
        if escolha == "4":
            tela_editar()
            parametro[4] = tel.modalidade(parametro[4])
        if escolha == "x":
            continua = False            
    return parametro    

def time_sleep():
     print("Saindo do sistema...")
     for x in range(40):
         print("#"*2,end = "")
         time.sleep(0.03)
     clear()
     print("off")
