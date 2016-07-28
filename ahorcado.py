import funciones
print("Bienvenido")
palabras=[]
guiones=[]
gana=False
errores=0
p=funciones.palabritas(palabras)
for letra in p:
	guiones.append("_")
opc=8*len(p)
while errores < opc:
	print("waka")
	while "_" in guiones:
		oculto=" ".join(guiones)
		print (p)
		print(oculto)
		res=input("Coloque letra: ")
		for i in range (0, len(p)):
			if p[i]==res:
				guiones[i]=res
			if res!=p:
				errores=errores+1
		print(errores)

print (p)
print ("Bai Bai")
