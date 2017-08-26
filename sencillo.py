class dojo(object):

	def __init__(self,x,y,s):
		self.menor=x
		self.mayor=y
		self.salto=s
		self.rango=range(menor,mayor,salto)

	def sum(self):
		suma=0
		for i in self.rango:
			suma+=i #suma=suma+i

		print(suma)
		return suma

print("Ingrese menor")
menor = int(input())

print("Ingrese mayor")
mayor = int(input())

print("Ingrese salto")
salto = int(input())

#rango=range(menor,mayor)

calcular = dojo(menor,mayor,salto)

print(menor,mayor,salto)
#print("La suma e: ",sum(rango))

calcular.sum()