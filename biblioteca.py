def inicial():
   print("****sicBike****")
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
   
