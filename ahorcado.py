import funciones
print("Bienvenido")
palabras=[]
i=[1,2,3,4,5,6,7,8]
p=funciones.palabritas(palabras)
lenp=len(p)
oculto="_ "*lenp
print (p)
print(oculto)
pa=list(p)
res=input("Coloque letra: ")
if res in pa:
	gana=True
else:
	print("Pato")

