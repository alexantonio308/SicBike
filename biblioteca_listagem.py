def salvar_arquivo(dados):
   arquivo = open("ciclistas.txt","w")
   for x in range(len(dados)):
      print(dados[x],file = arquivo)
   arquivo.close() 

def clear():
    print ("\n" * 130)
   
def listar_lista(lista,contador,arquivo):
    for x in range(len(lista)):
	    print(lista[x],file = arquivo)
		
def listar_lista2(lista,contador,arq):		
	for dado_ciclista in lista:
          for w in dado_ciclista:
              print(w,file = arq)

