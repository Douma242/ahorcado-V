import funciones
print("Bienvenido")
opc="si"
while opc=="si":
	palabras=[]
	guiones=[]
	errores=0
	p=funciones.palabritas(palabras)
	for letra in p:
		guiones.append("_")
	while errores<8:
		oculto=" ".join(guiones)
		print(oculto)
		res=input("Coloque letra: ")
		for i in range (0, len(p)):
			if p[i]==res:
				guiones[i]=res
		if res not in p:
			errores=errores+1
			print(funciones.dibujo(errores))
		if "_" not in guiones:
			errores=8
	if "_" in guiones:
		print("Fallaste la respuesta era: ", p)
	else:
		print("Ganaste")
	opc=input("Desea seguir? ")
print ("Bai Bai")
