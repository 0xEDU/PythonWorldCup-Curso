import card_game
import time
import random
from tkinter import *
from tkinter import filedialog
import wc_interface as wci
import turtle

#BOB
def bob():
    bob = turtle.Turtle()
    while True:
        bob.forward(200)
        bob.right(145)


# função que gera um baralho random
def random_deck(deck,deck_lenght):
    for x in range(deck_lenght):
        p_name = 'Menino Ney' + str(x)
        img_name = 'random.png'
        city = 'Brasiliam'
        #randint para coisas aleatorias
        atck = random.randint(1,100)
        dfc = random.randint(1,100)
        res = random.randint(1,100)
        spd = random.randint(1,100)
        kck = random.randint(1,100)
        card = card_game.card(name = p_name, image=img_name, country = city, attack = atck, defense = dfc, resistance = res, speed = spd, kick = kck)
        deck.append(card)

#Distribui entre player e AI
def shuffle(deck,player,computer):
    deck.shuffle()
    deck.distribute(player,computer)

#Salva o deck
def saved_deck(deck,file_name):
    file = open(file_name,'r')
    prop = ['name','image','country','attack','defense','resistance','speed','kick']
    for line in file:
        card =card_game.card(*prop,line = line)
        deck.append(card)
    file.close()

def pick_a_card():
    # Comprar a carta
    while True:
        player_card = player.deck.pop_card()
        computer_card = computer.deck.pop_card()
    # Mostrar a carta para o jogador
        print('='*50)
        print('Sua carta é: ')
        print('')
        print('Nome:', player_card.name)
        for prop in player_card.properties:
            print(prop + ' : ', player_card.properties[prop])
        time.sleep(0.5)
        return player_card, computer_card

def pre_jogo():
    choice = input('Você gostaria de usar um baralho [s]alvo ou um baralho [a]leatório? ')

    #Escolha de baralhos(loop)
    while True:
        if choice=='a':
            random_deck(deck, 10)
            break
        elif choice=='s':
            saved_deck(deck,'jogadores')
            break
        else:
            print('Digite "a" ou "s".')
            choice = input('Você gostaria de usar um baralho [s]alvo ou um baralho [a]leatório? ')
    shuffle(deck,player,computer)

def player_choice():
    # Escolha do atributo
    print('='*50)
    print('Escolha o atributo a ser jogado')
    while True:
        choice = input('[a]ttack, [d]efense, [r]esistance, [s]peed, [k]ick: ')

        if choice == 'a':
            choice = 'attack'
            break
        elif choice == 'd':
            choice = 'defense'
            break
        elif choice == 'r':
            choice = 'resistance'
            break
        elif choice == 's':
            choice = 'speed'
            break
        elif choice == 'k':
            choice = 'kick'
            break
        else:
            print('Digite uma opção válida.')
    print('')

    #imprimir a escolha
    player_atribute = player_card.properties[choice]
    computer_atribute = computer_card.properties[choice]
    print('')
    print('Você escolheu o atributo ',choice)
    print('Seu jogador tem ',player_atribute)
    time.sleep(1)
    print('O computador tem ',computer_atribute)
    return choice
# Checar o vencedor
def check_winner(choice):
    print('A escolha foi: ',choice)
    player_atribute = player_card.properties[choice]
    computer_atribute = computer_card.properties[choice]
    if player_atribute > computer_atribute:
        print('Você ganhou essa rodada! :D')
        #player.deck.insert('bottom',player_card,computer_card)
        time.sleep(2)
    elif player_atribute < computer_atribute:
        print('O Bot ganhou essa rodada :c')
        #omputer.deck.insert('bottom',player_card,computer_card)
        time.sleep(2)
    else:
        print('Essa rodada foi um empate :l')
        #player.deck.insert('bottom',player_card)
        #computer.deck.insert('bottom',computer_card)
        time.sleep(2)
    if len(player.deck) == 0:
        print('Fim de jogo.')
        time.sleep(0.9)
        print('K.O!!')
        time.sleep(0.9)
        print('Perdeu')
        return 'izi lixo'
    elif len(computer.deck) == 0:
        print('GG!.')
        time.sleep(0.9)
        print('K.O!!')
        return 'izi lixo'
    else:
        return None

#Escolha do BOT
def computer_choice():
    print('Esse turno é do computador')
    time.sleep(2)
    print('Calculando a jogada...')
    time.sleep(4)
    choice = computer_card.max_prop()
    player_atribute = player_card.properties[choice]
    computer_atribute = computer_card.properties[choice]
    print('O computador escolheu ', choice)
    print('O computador tem',computer_atribute,'neste atributo.')
    time.sleep(1)
    print('Voce tem',player_atribute,'neste atributo')
    time.sleep(1)
    return choice

#Textos
#    print('Bem-vindo ao Python Trunfo!')
#    time.sleep(1)
#    player_name = input('Digite o nome do jogador: ')
#    time.sleep(1)
#    print('Olá,', player_name)
#    print('Espere enquanto criamos as cartas!')
#    time.sleep(3)

name = ''
root = Tk()
root.tk_setPalette(background = '#2c465b',foreground = '#f4d039')
deck = card_game.deck()
def abrib():
    global name
    #file = filedialog.askopenfilename()
    #saved_deck(deck,file)
    saved_deck(deck,'jogadores')
    name = player_name.get()
    root.destroy()

frame1 = Frame(root)
frame2 = Frame(root)

frame1.pack()
frame2.pack()

Label(frame1,text='Bem vindo ao Python Trunfo',font = ('Arial',50,'bold')).pack()
Label(frame2,text='Nome: ').grid(row = 0, column = 0)
player_name = Entry(frame2)
player_name.grid(row = 0, column = 1)
Button(frame2, text = 'Começar o jooj',command = abrib).grid(row = 1, column = 0, columnspan=2)
root.mainloop()

player = card_game.player(name = name)
computer = card_game.player(name = 'Bot')
shuffle(deck,player,computer)

janela = wci.Window(player,computer)
janela.draw_interface()
janela.draw_start_menu()

while True:
    player_card, computer_card = pick_a_card()
    janela.pcard = player_card
    janela.ccard = computer_card
    janela.start(command = janela.player_choice)
    janela.draw_pcard()
    janela.challenge(command = janela.check_winner)
    janela.draw_ccard()
    if check_winner(janela.choice.get().lower()) == 'izi lixo':
        break
    player_card,computer_card = pick_a_card()
    janela.pcard = player_card
    janela.ccard = computer_card
    janela.start(command = janela.computer_choice)
    janela.draw_pcard()
    janela.challenge(command = janela.check_winner)
    janela.draw_ccard()
    if check_winner(janela.choice.get().lower()) == 'izi lixo':
        break
bob()


##pre_jogo()
##while True:
##    #turno do Player
##    player_card, computer_card = pick_a_card()
##    choice = player_choice()
##    if check_winner(choice) == 'izi lixo':
##        break
##    print('='*50)
##    print('Seu deck tem',len(player.deck),'cartas')
##    print('O deck do Bot tem',len(computer.deck),'cartas')
##    print('='*50)
##    input('Aperte "Enter" para continuar...')
##
##    #turno do IA
##    player_card,computer_card = pick_a_card()
##    choice = computer_choice()
##    if check_winner(choice) == 'izi lixo':
##        break
##    print('='*50)
##    print('Seu deck tem',len(player.deck),'cartas')
##    print('O deck do Bot tem',len(computer.deck),'cartas')
##    print('='*50)
##    input('Aperte "Enter" para continuar...')
##
##
##
##print('Seu deck tem',len(player.deck),'cartas')
##print('O deck do Bot tem',len(computer.deck),'cartas')
##print('='*50)
##time.sleep(2)
