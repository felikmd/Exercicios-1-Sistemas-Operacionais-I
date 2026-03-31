valor1=int(input("Digite o primeiro valor: "))
valor2=int(input("Digite o segundo valor: "))

maior=max(valor1,valor2)
menor=min(valor1,valor2)

if maior % menor == 0:
    print ("O maior é multiplo do menor")
else:
    print ("O maior não é multiplo do menor")