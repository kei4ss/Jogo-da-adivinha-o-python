# author: Miquéias Ferreira Dos Santos
# Github: @kei4ss
# Since: 26/05/2025

import random
import time

loop_principal = True
animais = [
    "🐶 Cachorro",
    "🐱 Gato",
    "🐘 Elefante",
    "🐒 Macaco",
    "🐢 Tartaruga",
    "🦁 Leão",
    "🐮 Vaca",
    "🐍 Cobra",
    "🐧 Pinguim",
    "🐴 Cavalo",
]

profissoes = [
    "👨‍🏫 Professor",
    "👩‍⚕️ Médica",
    "👨‍💻 Programador",
    "👨‍🍳 Cozinheiro",
    "👩‍🚒 Bombeira",
    "👷 Engenheiro",
    "👩‍⚖️ Juíza",
    "👨‍🎨 Artista",
    "👩‍🔬 Cientista",
    "👮 Policial"
]

personagens_anime = [
    "🌀 Naruto Uzumaki (Naruto)",
    "🗡️ Goku (Dragon Ball)",
    "🍓 Ichigo Kurosaki (Bleach)",
    "⚔️ Luffy (One Piece)",
    "👓 Light Yagami (Death Note)",
    "🧤 Edward Elric (Fullmetal Alchemist)",
    "👊 Saitama (One Punch Man)",
    "🪙 Lelouch Lamperouge (Code Geass)",
    "👺 Tanjiro Kamado (Demon Slayer)",
    "🧍 Mikasa Ackerman (Attack on Titan)"
]

# Quando "loop_principal" for falso, o jogo acabará
while loop_principal:

    # Menu principal do jogo
    print("\n🎲🎉 === JOGO DE CHARADAS === 🎉🎲")
    print(" 1️⃣  Jogar")
    print(" 2️⃣  Ver temas")
    print(" 3️⃣  Sair")
    resposta_menu_principal = input("-> ").lower()

    # Caso o usuário selecione "Jogar"
    if resposta_menu_principal == "jogar" or resposta_menu_principal == "1":
        print("\n🧠 Você escolheu *JOGAR*!")
        time.sleep(1)

        # Escolhendo aleatoriamente 1 dos temas (Animais, profissoes ou personagens de anime)
        # de acordo com um número de 0 à 2. Cada número representa um tema.
        tema = random.randint(0, 2)
        temaEscolhido = ""
        listaDeElementos = []

        if tema == 0: # para animais
            temaEscolhido = "🐾 animais"
            listaDeElementos = animais[::]
        elif tema == 1: # para profissoes
            temaEscolhido = "💪 profissoes"
            listaDeElementos = profissoes[::]
        elif tema == 2: # para personagens de anime
            temaEscolhido = "🎌 personagens de anime"
            listaDeElementos = personagens_anime[::]

        print("Tema sortado: " + temaEscolhido)
        time.sleep(0.5)
        print("    Você é: ", random.choice(listaDeElementos))
        time.sleep(1)

        print('Você tem 30 segundos para explicar o que você pegou!')

        for i in range (30, 0, -1):
            print(i)
            time.sleep(1)
        
        print("\nO tempo acabou!")
        input("Aperte ENTER para continuar!")
        
    # Caso o usuário selecione para ver os temas
    elif resposta_menu_principal == "ver temas" or resposta_menu_principal == "2":
        print("\n📘 Você escolheu *VER TEMAS*!")
        time.sleep(0.3)
        print("🐾 ANIMAIS")
        time.sleep(0.4)
        for animal in animais:
            print(" - ", animal)
            time.sleep(0.2)
        
        time.sleep(0.5)
        print("\n💪 PROFISSOES")
        for profissao in profissoes:
            print(" - ", profissao)
            time.sleep(0.2)

        time.sleep(0.5)
        print("\n🎌 PERSONAGENS DE ANIME")
        for personagem in personagens_anime:
            print(" - ", personagem)
            time.sleep(0.2)

        while True:
            print("\n📘 === MENU DE TEMAS === 📘")
            print(" 1️⃣  Adicionar novo elemento à um dos temas")
            print(" 2️⃣  Remover um elemento de um dos temas")
            print(" 3️⃣  Voltar ao menu principal")
            resposta_menu_tema = input("-> ").lower()

            if "novo elemento" in resposta_menu_tema or resposta_menu_tema == "1":
                print("\n📜 === ESCOLHA UM TEMA === 📜")
                print(" 1️⃣  Animais")
                print(" 2️⃣  Profissoes")
                print(" 3️⃣  personagens de anime")
                resposta_menu_escolha_tema = input("-> ").lower()
                
                if resposta_menu_escolha_tema == "animais" or resposta_menu_escolha_tema == "1":
                    print("🐾 animais foi escolhido")
                    novoElemento = input("Insira o novo elemento para o tema ANIMAIS: ").capitalize()
                    animais.append(novoElemento)
                elif resposta_menu_escolha_tema == "profissoes" or resposta_menu_escolha_tema == "2":
                    print("💪 profissoes foi escolhido")
                    novoElemento = input("Insira o novo elemento para o tema PROFISSOES: ").capitalize()
                    profissoes.append(novoElemento)
                elif "anime" in resposta_menu_escolha_tema or resposta_menu_escolha_tema == "3":
                    print("🎌 personagens de anime foi escolhido")
                    novoElemento = input("Insira o novo elemento para o tema PERSONAGENS DE ANIME: ").capitalize()
                    personagens_anime.append(novoElemento)
                else:
                    print("Sinto muito... Parece que '",resposta_menu_escolha_tema,"' não é um comando válido!" )

            elif "remover elemento" in resposta_menu_tema or resposta_menu_tema == "2":
                print("\n📜 === ESCOLHA UM TEMA === 📜")
                print(" 1️⃣  Animais")
                print(" 2️⃣  Profissoes")
                print(" 3️⃣  personagens de anime")
                resposta_menu_escolha_tema = input("-> ").lower()

                if resposta_menu_escolha_tema == "animais" or resposta_menu_escolha_tema == "1":
                    print("🐾 animais foi escolhido")
                    elementoParaRemover = input("Insira o nome do elemento que será removido: ")
                    if elementoParaRemover in animais:
                        animais.remove(elementoParaRemover)
                        print("✅ Elemento removido com sucesso!")
                    else:
                        print("🚫 Elemento não foi encontrado na lista de animais")
                    
                elif resposta_menu_escolha_tema == "profissoes" or resposta_menu_escolha_tema == "2":
                    print("💪 profissoes foi escolhido")
                    elementoParaRemover = input("Insira o nome do elemento que será removido: ")
                    if elementoParaRemover in profissoes:
                        profissoes.remove(elementoParaRemover)
                        print("✅ Elemento removido com sucesso!")
                    else:
                        print("🚫 Elemento não foi encontrado na lista de profissoes")
                    
                elif "anime" in resposta_menu_escolha_tema or resposta_menu_escolha_tema == "3":
                    print("🎌 personagens de anime foi escolhido")
                    elementoParaRemover = input("Insira o nome do elemento que será removido: ")
                    if elementoParaRemover in personagens_anime:
                        personagens_anime.remove(elementoParaRemover)
                        print("✅ Elemento removido com sucesso!")
                    else:
                        print("🚫 Elemento não foi encontrado na lista de personagens de anime.")

                    

            elif "voltar" in resposta_menu_tema or resposta_menu_tema == "3":
                break

            else:
                print("Sinto muito... Parece que '",resposta_menu_tema,"' não é um comando válido!" )
                time.sleep(1) 


    # Caso o usuário selecione sair do jogo
    elif resposta_menu_principal == "sair" or resposta_menu_principal == "3":
        print("👋 Saindo do jogo. Até mais!")
        loop_principal = False
    

    # Caso digita alguma coisa que não seja uma das opções
    else:
        print("Sinto muito... Parece que '",resposta_menu_principal,"' não é um comando válido!" )
        time.sleep(1)