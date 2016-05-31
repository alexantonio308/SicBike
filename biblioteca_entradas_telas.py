import pickle
def clear():
    print ("\n" * 90)

def press():
    ir = input("precione enter para continuar!")

def menu_inicial():
   print("------------------------SicBIKE--------------------\n")
   print("                  [1] Cadastrar   ")
   print("                  [2] Loguin      ")
   print("                  [x] Sair        ")
   print("---------------------------------------------------")    

def menu_loguin():
    print("[1] Apagar cadastro")
    print("[2] Gerar arquivo de Matricula")
    print("[3] Verificar matricula")
    print("[x] Voltar")
    
def input_dados(lista):
    lista.append(input("Nome:"))
    lista.append(input("CPF:"))
    lista.append(input("eMAIL:"))
    lista.append(input("Modalidade:"))

def conta_matricula(parametro):
    arq = open("conta.txt","wb")
    pickle.dump(parametro,file = arq)
    arq.close()

def matricula_creator(parametro):
    nome = "Matricula%s.txt" %str(contador)
    arq = open(nome, "wb")
    pickle.dump(parametro, file = arq)
    arq.close()

def matricula_read(parametro):
    nome2 = "Matricula%s.txt" %str(parametro)
    arquivo = open(nome2, "rb")
    dados2 = pickle.load(arquivo)
    return dados2

def listar_matricula(parametro):
    for item in parametro:
        print(item)
