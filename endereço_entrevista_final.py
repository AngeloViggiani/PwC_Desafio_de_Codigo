#Função para verificar se um elemento da lista é digito
def verificar_se_numero(lista, indice):
  if lista[indice].isdigit():
    return True
  return False

#Função que separa uma string em palavras sem vírgulas
def sem_virgula (string):
  string = string.replace(",","")
  string = string.split(" ")
  return string

#Função para verificar se o último elemento de uma lista é uma letra.
def verificar_se_ultimo_letra(lista):
  if not lista[len(lista)-1].isdigit():
    return True
  return False

#Função para descobrir se uma lista tem dois elementos
def lista_2(lista):
  if len(lista) == 2:
    return True
  return False

#Função para descobrir se uma lista tem mais de dois elementos
def lista_3(lista):
  if len(lista) > 2:
    return True
  return False

#Função para encontrar o índice da palavra "no"
def encontrar_indice_no(lista):
  valores_buscados = ["no", "n", "nº","bloco"]
  for indice, elemento in enumerate(lista):
    if elemento.lower() in valores_buscados:
      return indice

#Função para encontrar o índice de um número na lista
def encontrar_indice_num(lista):
  for indice, elemento in enumerate(lista):
    if elemento.isdigit():
      return indice

#Função principal
def endereco(endereco):
  #Separar a string em palavras
  EnderecoSeparado = sem_virgula(endereco)

  #Declarar variáveis
  Nome = ""
  Numero = ""


  #Selecionar Caso

  #CASO 1: Endereço de duas palavras.
  if lista_2(EnderecoSeparado):
    if verificar_se_numero(EnderecoSeparado, 0):
      Numero = EnderecoSeparado[0]
      Nome = EnderecoSeparado[1]
      return Nome,Numero
    else:
      Numero = EnderecoSeparado[1]
      Nome = EnderecoSeparado[0]
      return Nome,Numero
      
    
  #CASO 2: Mais de duas palavras.
  elif lista_3(EnderecoSeparado):
    
    #CASO 2A: Um dos elementos da lista está na lista está na string original.
    if "No" in EnderecoSeparado or "no" in EnderecoSeparado or "bloco" in EnderecoSeparado or "Bloco" in EnderecoSeparado:
      #Selecionar tudo que vier antes do "No" como Nome e o que vier depois como Numero
      for i in range(0,encontrar_indice_no(EnderecoSeparado)):
        Nome = Nome + " " + EnderecoSeparado[i]
      for i in range(encontrar_indice_no(EnderecoSeparado),len(EnderecoSeparado)):
        Numero = Numero + " " + EnderecoSeparado[i]
      
      Nome = Nome.lstrip()
      Numero = Numero.lstrip()
      return Nome,Numero

    #CASO 2B: A primeira substring é um número.
    elif verificar_se_numero(EnderecoSeparado,0):
      #Selecionar o primeiro índice como Numero e o resto como Nome.
      Numero = EnderecoSeparado[0]
      for i in range(1,len(EnderecoSeparado)):
        Nome = Nome + " " + EnderecoSeparado[i]
      
      Nome = Nome.lstrip()
      Numero = Numero.lstrip()
      return Nome,Numero

    #CASO 2C: Apenas a última substring é um número.
    elif verificar_se_numero(EnderecoSeparado,len(EnderecoSeparado)-1):
    #Selecionar o primeiro índice como Numero e o resto como Nome.
      Numero = EnderecoSeparado[len(EnderecoSeparado)-1]
      for i in range(len(EnderecoSeparado)-1):
        Nome = Nome + " " + EnderecoSeparado[i]
      
      Nome = Nome.lstrip()
      Numero = Numero.lstrip()
      return Nome,Numero

    #CASO 2D: A última substring é uma letra.
    elif verificar_se_ultimo_letra(EnderecoSeparado):
      for i in range(0,encontrar_indice_num(EnderecoSeparado)):
        Nome = Nome + " " + EnderecoSeparado[i]
      for i in range(encontrar_indice_num(EnderecoSeparado),len(EnderecoSeparado)):
        Numero = Numero + " " + EnderecoSeparado[i]
      
      Nome = Nome.lstrip()
      Numero = Numero.lstrip()
      return Nome,Numero 

lista_enderecos = ["Miritiba 339","Babaçu 500","Cambuí 804B","Rio Branco 23","Quirino dos Santos 23 b","4, Rue de la République","100 Broadway Av","Calle Sagasta, 26","Calle 44 No 1991","Aragona 71 Bloco 7 ap 25"]
def teste_1 (lista):
  for i in range(len(lista)):
    print (endereco(lista[i]))


endereco(input("Digite seu endereço: "))