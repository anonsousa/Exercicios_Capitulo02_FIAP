print(" ############## VERIFICAR A SAUDE DO CORAÇÃO ############## ")


bpm = int(input("Informe suas bpm: "))
idade = int(input("Informe idade: "))

if idade <= 2 and bpm >= 120 and bpm <= 140:
    print("Batimentos normais!")

elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
    print("Batimentos normais!")
elif idade >= 18 and idade <= 60 and bpm >= 70 and bpm <= 80:
    print("Batimentos normais!")
elif idade >= 60 and bpm >= 50 and bpm <= 60:
    print("Batimentos normais!")
else:
    print("Não foi possivel verificar os batimentos!")