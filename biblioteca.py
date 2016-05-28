def inicial():
   print("\n****sicBike****")
   print("[1] Cadastrar")
   print("[2] Loguin")
   print("[x] Sair")

def salvar_arquivo(dados):
   arquivo = open("ciclistas.txt","w")
   for x in range(len(dados)):
      print(dados[x],file = arquivo)
   arquivo.close() 

def loguin(arquivo,nome_usuario,cpf_usuario):
   if nome_usuario in arquivo and cpf_usuario in arquivo:
      print("longado")
      print("[1] Apagar cadastro")
      print("[2] Imprimir cadastro")
      
   else:
      print("nome ou senha invalidos")

def clear():
    print ("\n" * 130)
   
def listar_lista(lista,contador,arquivo):
    for x in range(len(lista)):
	    print(lista[x],file = arquivo)
		
def listar_lista2(lista,contador,arq):		
	for dado_ciclista in lista:
          for w in dado_ciclista:
              print(w,file = arq)

def imprimir_matricula_ciclista(lista,arquiv):
    for dado in range(1):
        print("Modalidade:",lista[dado],file = arquiv)
        print("Nome:",lista[dado+1],file = arquiv)
        print("Email:",lista[dado+2],file = arquiv)
        print("Celular:",lista[dado+3],file = arquiv)
        print("Cpf:",lista[dado+4],file = arquiv)
        print("Registro Geral(RG):",lista[dado+5],file = arquiv)
        print("Data de nascimento:",lista[dado+6],file = arquiv)
        print("Matricula:",lista[dado+7],file = arquiv)

def verificar_matricula(lista):
   for dado in range(1):
        print("Modalidade:",lista[dado])
        print("Nome:",lista[dado+1])
        print("Email:",lista[dado+2])
        print("Celular:",lista[dado+3])
        print("Cpf:",lista[dado+4])
        print("Registro Geral(RG):",lista[dado+5])
        print("Data de nascimento:",lista[dado+6])
        print("Matricula:",lista[dado+7])
   
