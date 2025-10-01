altura = int (input("DIGITE SUA ALTURA"))
peso = int (input("DIGITE SEU PESO"))
imc = peso / altura **2
if (imc < 18,5):
    print("ABAIXO DO PESO")
elif (imc >= 18,5 and imc < 25):
    print("PESO NORMAL")
elif (imc >= 25 and imc < 30):
    print("SOBREPESO")
else:
    print("OBESIDADE")
