from tkinter import *
from PIL import Image
from PIL import ImageTk
class Window(Tk):
	def __init__(self, player, computer):
		super(Window,self).__init__()
		self.player = player
		self.computer = computer
		self.bgimage = Image.open("pkbg.png")
		self.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")


	def draw_interface(self):
		self.frame_jog = Frame(self, bd = 1, relief = RIDGE)
		self.frame_jog.grid(column = 0, row = 0)
		self.frame_com = Frame(self, bd = 1, relief = RIDGE)
		self.frame_com.grid(column = 1, row = 0)
		self.frame_action = Frame(self, bd = 1, relief = RIDGE)
		self.frame_action.grid(column = 0, row = 1, columnspan = 2, sticky = N+S+W+E)

		cab_jog = Frame(self.frame_jog, bd = 1, relief = RIDGE)
		cab_jog.pack(side = TOP, fill = X)

		info_jog = Frame(self.frame_jog, bd = 1, relief = RIDGE)
		info_jog.pack(side = TOP, fill = X)

		frame_escolha = Frame(self.frame_jog)
		frame_escolha.pack(side = TOP)

		cab_com = Frame(self.frame_com, bd = 1, relief = RIDGE)
		cab_com.pack(side = TOP, fill = X)

		info_com = Frame(self.frame_com, bd = 1, relief = RIDGE)
		info_com.pack(side = TOP, fill = X)

		cards_jog = Label(cab_jog, text = str(len(self.player.deck)), font = (20))
		cards_jog.pack(side = LEFT, padx = 20)
		Label(cab_jog, text = self.player.name.upper(), font = (20)).pack(side = LEFT)

		cards_com = Label(cab_com, text = str(len(self.computer.deck)), font = (20))
		cards_com.pack(side = RIGHT, padx = 20)
		Label(cab_com, text = 'COMPUTER', font = (20)).pack(side = RIGHT)


		imagem = self.bgimage.resize((150, 200))
		self.jtkimage = ImageTk.PhotoImage(imagem)
		self.ctkimage = ImageTk.PhotoImage(imagem)

		frame_img_jog = Frame(info_jog, bd = 1, relief = RIDGE)
		frame_img_jog.grid(row = 0, column = 0, sticky = N+S+W+E)
		self.foto_jog = Label(frame_img_jog, image = self.jtkimage, bd = 2, relief = RAISED)
		self.foto_jog.pack(padx = 10, pady = 10)
		frame_dados_jog = Frame(info_jog, bd = 1, relief = RIDGE)
		frame_dados_jog.grid(row = 0, column = 1, sticky = N+S+W+E)
		frame_info_jog = Frame(frame_dados_jog)
		frame_info_jog.pack(side = LEFT, padx = 10)

		self.nome_jog = Label(frame_info_jog, text = "Name", font = ('arial',10,'bold'))
		self.nome_jog.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		self.pais_jog = Label(frame_info_jog, text = "Country", font = ('arial',10,'bold'))
		self.pais_jog.grid(row = 1, column = 0, columnspan = 2, sticky = W)
		Label(frame_info_jog).grid(row = 2, column = 0)
		Label(frame_info_jog, text = "SKILLS", font = ('arial',10,'bold')).grid(row = 3, column = 0, columnspan = 2, sticky = W)
		Label(frame_info_jog, text = "Attack:").grid(row = 4, column = 0, sticky = W, pady = 5)
		att_jog = Label(frame_info_jog, width = 4)
		att_jog.grid(row = 4, column = 1, sticky = W+E)
		Label(frame_info_jog, text = "Defense:").grid(row = 5, column = 0, sticky = W)
		defesa_jog = Label(frame_info_jog, width = 4)
		defesa_jog.grid(row = 5, column = 1, sticky = W+E)
		Label(frame_info_jog, text = "Resistance:").grid(row = 6, column = 0, sticky = W, pady = 5)
		res_jog = Label(frame_info_jog, width = 4)
		res_jog.grid(row = 6, column = 1, sticky = W+E)
		Label(frame_info_jog, text = "Speed:").grid(row = 7, column = 0, sticky = W)
		vel_jog = Label(frame_info_jog, width = 4)
		vel_jog.grid(row = 7, column = 1, sticky = W+E)
		Label(frame_info_jog, text = "Kick:").grid(row = 8, column = 0, sticky = W, pady = 5)
		chute_jog = Label(frame_info_jog, width = 4)
		chute_jog.grid(row = 8, column = 1, sticky = W+E)
		self.fjog = frame_info_jog
		self.pav = Label(self.fjog, text = '  ')
		self.pav.grid(row = 4, column = 1)
		self.pdv = Label(self.fjog, text = '  ')
		self.pdv.grid(row = 5, column = 1)
		self.prv = Label(self.fjog, text = '  ')
		self.prv.grid(row = 6, column = 1)
		self.psv = Label(self.fjog, text = '  ')
		self.psv.grid(row = 7, column = 1)
		self.pkv = Label(self.fjog, text = '  ')
		self.pkv.grid(row = 8, column = 1)

		frame_img_com = Frame(info_com, bd = 1, relief = RIDGE)
		frame_img_com.grid(row = 0, column = 1, sticky = N+S+W+E)
		self.foto_com = Label(frame_img_com, image = self.ctkimage, bd = 2, relief = RAISED)
		self.foto_com.pack(padx = 10, pady = 10)
		frame_dados_com = Frame(info_com, bd = 1, relief = RIDGE)
		frame_dados_com.grid(row = 0, column = 0, sticky = N+S+W+E)
		frame_info_com = Frame(frame_dados_com)
		frame_info_com.pack(side = RIGHT, padx = 10)

		self.nome_com = Label(frame_info_com, text = "Name", font = ('arial',10,'bold'))
		self.nome_com.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		self.pais_com = Label(frame_info_com, text = "Country", font = ('arial',10,'bold'))
		self.pais_com.grid(row = 1, column = 0, columnspan = 2, sticky = W)
		Label(frame_info_com).grid(row = 2, column = 0)
		Label(frame_info_com, text = "SKILLS", font = ('arial',10,'bold')).grid(row = 3, column = 0, columnspan = 2, sticky = W)
		Label(frame_info_com, text = "Attack:").grid(row = 4, column = 0, sticky = W, pady = 5)
		att_com = Label(frame_info_com, width = 4)
		att_com.grid(row = 4, column = 1, sticky = W+E)
		Label(frame_info_com, text = "Defense:").grid(row = 5, column = 0, sticky = W)
		defesa_com = Label(frame_info_com, width = 4)
		defesa_com.grid(row = 5, column = 1, sticky = W+E)
		Label(frame_info_com, text = "Resistance:").grid(row = 6, column = 0, sticky = W, pady = 5)
		res_com = Label(frame_info_com, width = 4)
		res_com.grid(row = 6, column = 1, sticky = W+E)
		Label(frame_info_com, text = "Speed:").grid(row = 7, column = 0, sticky = W)
		vel_com = Label(frame_info_com, width = 4)
		vel_com.grid(row = 7, column = 1, sticky = W+E)
		Label(frame_info_com, text = "Kick:").grid(row = 8, column = 0, sticky = W, pady = 5)
		chute_com = Label(frame_info_com, width = 4)
		chute_com.grid(row = 8, column = 1, sticky = W+E)
		self.fcom = frame_info_com
		self.cav = Label(self.fcom, text = '  ')
		self.cav.grid(row = 4, column = 1)
		self.cdv = Label(self.fcom, text = '  ')
		self.cdv.grid(row = 5, column = 1)
		self.crv = Label(self.fcom, text = '  ')
		self.crv.grid(row = 6, column = 1)
		self.csv = Label(self.fcom, text = '  ')
		self.csv.grid(row = 7, column = 1)
		self.ckv = Label(self.fcom, text = '  ')
		self.ckv.grid(row = 8, column = 1)

	def draw_start_menu(self):
		self.start_button = Button(self.frame_action, text = 'START', font = ('arial', 20, 'bold'))
		self.start_button.pack(pady = 20)

	def start(self, command = None):
		if command != None:
			self.start_button['command'] = command
		self.wait = IntVar()
		self.wait_variable(self.wait)

	def player_choice(self):
		self.start_button.destroy()
		frame_start = Frame(self.frame_action)
		frame_start.pack(side = TOP, pady = 20)

		self.choice = StringVar(self)
		OM = OptionMenu(frame_start, self.choice, 'Attack', 'Defense', 'Resistance', 'Speed', 'Kick')
		OM.config(width = 15)
		OM.pack(side = LEFT, padx = 20)
		self.choice_button = Button(frame_start, text = 'Challenge')
		self.choice_button.pack(side = LEFT)
		resposta = Label(frame_start, text = '', width = 20)
		resposta.pack(side = LEFT)
		self.wait.set(1)

	def draw_pcard(self):
		self.nome_jog['text'] = self.pcard.name
		self.pais_jog['text'] = self.pcard.properties['country']
		self.pav['text'] = self.pcard.properties['attack']
		self.pdv['text'] = self.pcard.properties['defense']
		self.prv['text'] = self.pcard.properties['resistance']
		self.psv['text'] = self.pcard.properties['speed']
		self.pkv['text'] = self.pcard.properties['kick']

		imagem = Image.open(self.pcard.image)
		imagem = imagem.resize((150, 200))
		self.jtkimage = ImageTk.PhotoImage(imagem)
		self.foto_jog['image'] = self.jtkimage

	def draw_ccard(self):
		self.nome_com['text'] = self.ccard.name
		self.pais_com['text'] = self.ccard.properties['country']
		self.cav['text'] = self.ccard.properties['attack']
		self.cdv['text'] = self.ccard.properties['defense']
		self.crv['text'] = self.ccard.properties['resistance']
		self.csv['text'] = self.ccard.properties['speed']
		self.ckv['text'] = self.ccard.properties['kick']

		imagem = Image.open(self.ccard.image)
		imagem = imagem.resize((150, 200))
		self.ctkimage = ImageTk.PhotoImage(imagem)
		self.foto_com['image'] = self.ctkimage

		self.update()
		self.wait = IntVar()
		self.wait_variable(self.wait)

	def challenge(self, command = None):
		if command != None:
			self.choice_button['command'] = command
		self.wait = IntVar()
		self.wait_variable(self.wait)

	def check_winner(self):
		if self.choice.get() == 'Attack':
			self.test('attack','attack')
		elif self.choice.get() == 'Defense':
			self.test('defense','defense')
		elif self.choice.get() == 'Resistance':
			self.test('resistance','resistance')
		elif self.choice.get() == 'Speed':
			self.test('speed','speed')
		elif self.choice.get() == 'Kick':
			self.test('kick','kick')
		self.wait.set(1)

	def test(self, pchoice, cchoice):
		self.frame_action.destroy()
		self.frame_action = Frame(self, bd = 1, relief = RIDGE)
		self.frame_action.grid(column = 0, row = 1, columnspan = 2, sticky = N+S+W+E)
		pstrength = self.pcard.properties[pchoice]
		print("you are going to fight your enemy whith", pchoice)
		print("your player has", pstrength, "strength on this ability")

		cstrength = self.ccard.properties[cchoice]
		print("the computer is going to play with", cchoice)
		print('his player has', cstrength, "strength on this ability")

		### imprimindo o resultado
		if pstrength > cstrength:
			Label(self.frame_action, text = "your player won").pack()
			self.player.deck.insert("bottom", self.pcard, self.ccard)
		elif pstrength < cstrength:
			Label(self.frame_action, text = 'the computer player won').pack()
			self.computer.deck.insert("bottom", self.ccard, self.pcard)
		else:
			Label(self.frame_action, text = "nobody won").pack()
			self.player.deck.insert("bottom", self.pcard)
			self.computer.deck.insert("bottom", self.ccard)

		Button(self.frame_action, text = 'next round', command = self.restart).pack(pady = 10)

	def restart(self):
		self.frame_jog.destroy()
		self.frame_com.destroy()
		self.frame_action.destroy()
		self.draw_interface()
		self.draw_start_menu()
		self.wait.set(1)

	def computer_choice(self):
		self.start_button.destroy()
		frame_start = Frame(self.frame_action)
		frame_start.pack(side = TOP, pady = 20)
		choice = self.ccard.max_prop().title()
		Label(frame_start, text = 'computer choosed: '+ choice).pack(side= LEFT)
		self.choice = StringVar(self)
		self.choice.set(choice)
		self.choice_button = Button(frame_start, text = 'Next')
		self.choice_button.pack(side = LEFT, padx = 20)
		self.wait.set(1)



