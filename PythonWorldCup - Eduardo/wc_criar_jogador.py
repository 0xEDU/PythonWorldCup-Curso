#################################
### WorldCup Python Card Game ###
########## Interface ############
######## criar jogador ##########
#################################
###### Flávio C D Moraes ########
#################################

from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import csv

def salvar_jogador():
	img_name = 'cards/{:.5}_{:.5}.png'.format(nome.get(),pais.get()).replace(' ','_')
	info = [nome.get(), img_name, pais.get(), att.get(), defesa.get(), res.get(), vel.get(), chute.get()]
	try:
		file = open('jogadores', 'a', newline = '')
	except:
		file = open('jogadores', 'w', newline = '')
	escritor = csv.writer(file, lineterminator='\n')
	escritor.writerow(info)
	file.close()
	imagem.save(img_name)
	j_criar.destroy()

def buscar():
	global tkimagem
	global imagem
	file = filedialog.askopenfilename()
	print(file)
	try:
		imagem = Image.open(file)
	except:
		return 0
	imagem = imagem.resize((150, 200))
	tkimagem = ImageTk.PhotoImage(imagem)
	figura["image"] = tkimagem
	j_criar.update()


j_criar = Tk()
j_criar.winfo_toplevel().title("Criar Jogador")

frame1 = Frame(j_criar, bd = 1, relief = RIDGE)
frame2 = Frame(j_criar, bd = 1, relief = RIDGE)
frame3 = Frame(j_criar, bd = 1, relief = RIDGE)

frame1.grid(row = 0, column = 0, sticky = W+E+N+S)
frame2.grid(row = 0, column = 1, sticky = W+E+N+S)
frame3.grid(row = 1, column = 0, columnspan = 2, sticky = W+E+N+S)

imagem = Image.open("pkbg.png")
imagem = imagem.resize((150, 200))
tkimagem = ImageTk.PhotoImage(imagem)
frame_img = Frame(frame1)
frame_img.pack(pady = 20, padx = 20)
figura = Label(frame_img, image = tkimagem, bd = 2, relief = RAISED)
figura.pack()
Button(frame_img, text = "Carregar Imagem", command = buscar).pack(pady = 10)

info_frame = Frame(frame2)
info_frame.pack(padx = 20, pady = 10)
Label(info_frame, text = "Nome:").grid(row = 0, column = 0, columnspan = 2, sticky = W)
nome = Entry(info_frame, width = 15)
nome.grid(row = 1, column = 0, columnspan = 2)
Label(info_frame, text = "País:").grid(row = 2, column = 0, columnspan = 2, sticky = W)
pais = Entry(info_frame, width = 15)
pais.grid(row = 3, column = 0, columnspan = 2)
Label(info_frame).grid(row = 4, column = 0)
Label(info_frame, text = "HABILIDADES").grid(row = 5, column = 0, columnspan = 2, sticky = W)
Label(info_frame, text = "Ataque:").grid(row = 6, column = 0, sticky = W, pady = 5)
att = Entry(info_frame, width = 4)
att.grid(row = 6, column = 1, sticky = W+E)
Label(info_frame, text = "Defesa:").grid(row = 7, column = 0, sticky = W)
defesa = Entry(info_frame, width = 4)
defesa.grid(row = 7, column = 1, sticky = W+E)
Label(info_frame, text = "Resistência:").grid(row = 8, column = 0, sticky = W, pady = 5)
res = Entry(info_frame, width = 4)
res.grid(row = 8, column = 1, sticky = W+E)
Label(info_frame, text = "Velocidade:").grid(row = 9, column = 0, sticky = W)
vel = Entry(info_frame, width = 4)
vel.grid(row = 9, column = 1, sticky = W+E)
Label(info_frame, text = "Chute:").grid(row = 10, column = 0, sticky = W, pady = 5)
chute = Entry(info_frame, width = 4)
chute.grid(row = 10, column = 1, sticky = W+E)

Button(frame3, text = "CRIAR", command = salvar_jogador).pack(pady = 10)

j_criar.tk_setPalette(background='#2c465b', foreground='#f4d039', activeBackground='#f4d039', activeForeground="#2c465b")

j_criar.mainloop()