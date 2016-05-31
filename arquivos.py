import pickle
def conta_matricula(contador):
    arq = open("conta.ewe","wb")
    pickle.dump(contador,file = arq)
    arq.close()

def leito_cotador(contador):
    arquivo = open("conta.ewe","rb")
    contador = pickle.load(arquivo)
    return contador

def matricula_creator(parametro,parametro2):
    nome = "Matricula%s.txt" %str(parametro2)
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
