def clear():
    print ("\n" * 130)
    
def inicial():
   print("------------------------SicBIKE--------------------\n")
   print("                  [1] Cadastrar   ")
   print("                  [2] Loguin      ")
   print("                  [x] Sair        ")
   print("---------------------------------------------------")

def show_matricula(matricula):
    print("sua matricula é %s"%matricula,"será usada pra loguin")
    press = input("precione enter para continuar!")
    

def imprimir_matricula(lista,arquiv):
    for dado in range(1):
        print("-------------------MATRICULA----------------------",file = arquiv)
        print("Modalidade:",lista[dado],file = arquiv)
        print("Nome:",lista[dado+1],file = arquiv)
        print("Email:",lista[dado+2],file = arquiv)
        print("Celular:",lista[dado+3],file = arquiv)
        print("Cpf:",lista[dado+4],file = arquiv)
        print("Registro Geral(RG):",lista[dado+5],file = arquiv)
        print("Data de nascimento:",lista[dado+6],file = arquiv)
        print("Matricula:",lista[dado+7],file = arquiv)
        print("--------------------------------------------------",file = arquiv)

def verificar_matricula(lista):
   for dado in range(1):
       print("-------------------MATRICULA----------------------")
       print("Modalidade:",lista[dado])
       print("Nome:",lista[dado+1])
       print("Email:",lista[dado+2])
       print("Celular:",lista[dado+3])
       print("Cpf:",lista[dado+4])
       print("Registro Geral(RG):",lista[dado+5])
       print("Data de nascimento:",lista[dado+6])
       print("Matricula:",lista[dado+7])
       print("--------------------------------------------------")
       press = input("precione enter para continuar!")
       

def tela_loguin():
    print("[1] Apagar cadastro")
    print("[2] Gerar arquivo de Matricula")
    print("[3] Verificar matricula")
    print("[x] Voltar")


def dados_usuario(p1,p2,p3):
    print("--------------DADOS DO USUARIO------------------")
    p1.append(input("digite seu nome:"))
    p2.append(input("Digite seu email:"))
    p3.append(input("digite seu numero de celular ou telefone:"))
    print("------------------------------------------------")
    

def dados_pessoais(p1,p2,p3):
    print("-------------DADOS DO PESSOAIS------------------")
    p1.append(input("digite seu cpf:"))
    p2.append(input("digite seu RG:"))
    p3.append(input("digite sua data de nascimento:"))
    print("------------------------------------------------")

def cad_modalidade(p2):
    p1 = input("\nescolha sua modalidade:")
    if p1 == "1":
       p2.append("Ciclista Master")
    elif p1 == "2":
       p2.append("Ciclista Junior")
    elif p1 == "3":
       p2.append("Modo Turismo")
    elif p1 == "4":
       p2.append("Ciclista Peso pesado")
    else:
       ("opção invalida")
    
    
    

