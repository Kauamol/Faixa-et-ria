idade = int(input("Digite sua idade"))
if (idade<12):
    print("você é uma criança")
elif (idade>=12) and (idade<=17):
    print("Você é um adolescente")
elif (idade>=18) and (idade<=60):
    print  ("Você é um adulto")
else:
    print("Você é um idoso")
