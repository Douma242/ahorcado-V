import funciones
print("Bienvenido")
palabras=[]
guiones=[]
gana=False
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
	if "_" not in guiones:
		errores=8
if "_" in guiones:
	print("Fallaste la respuesta era: ", p)
else:
	print("Ganaste")
print ("Bai Bai")
