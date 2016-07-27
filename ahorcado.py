import funciones
print("Bienvenido")
palabras=[]
guiones=[]
gana=False
errores=0
p=funciones.palabritas(palabras)
for letra in p:
	guiones.append("_")
while errores<=7:
	while "_" in guiones:
		oculto=" ".join(guiones)
		print (p)
		print(oculto)
		res=input("Coloque letra: ")
		for i in range (0, len(p)):
			if p[i]==res:
				guiones[i]=res
		if res not in guiones:
			errores=errores+1
print (p)
print ("Bai Bai")
