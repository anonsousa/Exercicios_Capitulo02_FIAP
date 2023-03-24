## MONTANDO CONTABILIZADOR DE VOTOS SOMENTE COM ESTRUTURA IF ##


voto01 = input("Informe qual premio deseja ganhar:PLAYSTATION, XBOX, NINTENDO:")
voto02 = input("Informe qual premio deseja ganhar:PLAYSTATION, XBOX, NINTENDO:")
voto03 = input("Informe qual premio deseja ganhar:PLAYSTATION, XBOX, NINTENDO:")
voto04 = input("Informe qual premio deseja ganhar:PLAYSTATION, XBOX, NINTENDO:")
voto05 = input("Informe qual premio deseja ganhar:PLAYSTATION, XBOX, NINTENDO:")


playstation = 0
xbox = 0
nintendo = 0

#voto 1

if voto01.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto01.upper() == "XBOX":
    xbox = xbox + 1
elif voto01.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 1 digitou um console inexistente e seu voto sera anulado")


#voto 2

if voto02.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto02.upper() == "XBOX":
    xbox = xbox + 1
elif voto02.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 2 digitou um console inexistente e seu voto sera anulado")


#voto 3

if voto03.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto03.upper() == "XBOX":
    xbox = xbox + 1
elif voto03.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 3 digitou um console inexistente e seu voto sera anulado")


#voto 4 

if voto04.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto04.upper() == "XBOX":
    xbox = xbox + 1
elif voto04.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 4 digitou um console inexistente e seu voto sera anulado")


#voto 5

if voto05.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto05.upper() == "XBOX":
    xbox = xbox + 1
elif voto05.upper() == "NINTENDO":
    nintendo = nintendo + 1
else:
    print("O colaborador 5 digitou um console inexistente e seu voto sera anulado")

#contabilizando votos

if playstation > xbox and playstation > nintendo:
    print(f"O console escolhido foi PLAYSTATION com {playstation} votos")
elif xbox > playstation and xbox > nintendo:
    print(f"O console escolhido foi XBOX com {xbox} votos")
elif nintendo > playstation and nintendo > xbox:
    print(f"O console escolhido foi NINTENDO com {nintendo} votos")
else:
    print("Empate! favor entrar em contato com a direcao")