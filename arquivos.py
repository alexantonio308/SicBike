import pickle
import biblioteca_entradas_telas as tel
import os

def contador():
    arquivo = open("numero de matricula.age", "r")
    mat = int(arquivo.read())
    return mat
    
def n_matricula(cont):
    arquivo = open("numero de matricula.age", "w")
    arquivo.write(str(cont))
    return cont
    
def criador_matricula(parametro,parametro2,parametro3):
    nome = tel.diretorio(parametro2,parametro3)
    arq = open(nome , "wb")
    pickle.dump(parametro, file = arq)
    arq.close()

def leitor_de_matricula(parametro):
    arquivo = open(parametro, "rb")
    dados = pickle.load(arquivo)
    return dados

def verificar_matricula(parametro):
    tel.clear()
    iniciais = ["Nome: %s","Cpf: %s","e-mail: %s","data de nascimento: %s","Modalidade: %s"]
    for i in range(len(parametro)):
        print("[",i+1,"]" ,iniciais[i]%parametro[i])
    tel.press()

def listar_matriculados(parametro,cadastro):
    tel.clear()
    print(cadastro)
    print("_______________MATRICULA___________________\n")
    print(" Nome: %s" %parametro[0])
    print(" Modalidade: %s" %parametro[4])
    print("___________________________________________")
    
def tente_encontrar(parametro):   
    try:
        with open(parametro, "rb") as f:
            return True
    except IOError:
        print("Cilcista não encontrado")
        tel.press()    
        
def excluir_matricula():
    nome = input("digite seu nome:")
    matricula = input("Digite sua matricula:")
    parametro = nome+matricula
    parametro = "ciclistas/%s.txt" %str(parametro)
    if tente_encontrar(parametro):
        os.remove(parametro)
         
def listar_ciclistas(parametro):
    if len(parametro) == 0:
        print("Nenhum ciclista cadastrado")
        tel.press()
    for cadastro in parametro:
        tel.clear()
        cadastro = "ciclistas/" + cadastro
        file = open(cadastro,"rb")
        file = pickle.load(file)
        listar_matriculados(file,cadastro)
        tel.press()