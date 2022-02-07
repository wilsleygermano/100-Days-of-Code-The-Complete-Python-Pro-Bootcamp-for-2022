print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo à busca do tesouro.")
player = input("Qual o seu nome, aventureiro?\n")
print(f"{player}, prepare-se para uma aventura inegualável.\n")
 
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print(f"você acaba de acordar em um hospital vazio, {player}, e agora precisa buscar ajuda. Ao sair do quarto se depara com um corredor gigantesco sem quaquer sinal de vida. Você vai à esquerda ou direita?")
first_choice = input("Qual direção você escolhe: 'direita' ou 'esquerda'?\n")


if first_choice.lower() == "esquerda":
  print(f"Após chegar ao final do corredor você encontra um bilhete com os seguintes dizeres: 'Deixei escondido a chave da saída no armário da dispensa.'. Logo abaixo está a localização desse armário, então você:\n")
  second_choice = input("Procura o armário? 'S' ou 'N':\n")
  if second_choice.lower() == "s":
    third_choice = input("Após chegar no local indicado você se depara com três armários: um azul, outro vermelho e outro amarelo. Qual armário você abre?\n")
    if third_choice.lower() == "amarelo":
      print("""
      Um zumbi pula em você e te mata.
      Fim do jogo!
      Tente novamente mais tarde.
      """)
    elif third_choice.lower() == "azul":
      print("""
      Um vendedor de NFT tenta lhe incluir em um esquema de pirâmide. Ambos morrem de fome.
      Fim do jogo!
      Tente novamente mais tarde.
      """)
    else:
      print("Você venceu, parabéns.")
  else:
    print("""
    Você morreu de fome preso no hospital!
    Fim do jogo!
    Tente novamente mais tarde.
    """)
else:
  print("""
  Você foi atacadO(a) por um zumbi que estava de tocaia e comeu ceu cérebro.
  Fim do jogo!
  Tente novamente mais tarde
  """)


