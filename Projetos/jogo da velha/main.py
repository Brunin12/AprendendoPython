from tkinter import ttk
from tkinter import *
import tkinter
import os


def cls():
    os.system('cls')


p1 = "bruno"
p2 = "jurandir"

cls()
# p1 = input("nome do jogador 1\n")
# cls()
# p2 = input("nome do jogador 2\n")
# cls()


# ----------------cores pra ficar ⭐bunito⭐

co0 = "#ffffff"
co1 = "#333333"
co2 = "#fcc058"
co3 = "#38576b"
co4 = "#3297a8"
co5 = "#fff837"
co6 = "#fcc058"
co7 = "#e85151"
co8 = co4
co10 = "#fcfbf7"
fundo = "#4e4e4e"

# ---------------- criando a janela usando tkinter 😐

janela = Tk()
janela.title('jogo da velha')
janela.geometry('260x370')
janela.configure(bg=fundo)

# ---------------- Dividindo a janela

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, stick=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, stick=NW)

# ---------------- Criando Logica do app











# ---------------- Config do Frame Cima

# ------------- Config X

app_x = Label(frame_cima, text="X", height=1, relief='flat',
              anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co7)
app_x.place(x=28, y=15)

app_x = Label(frame_cima, text=p1, height=1, relief='flat',
              anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_x.place(x=28, y=70)

points = Label(frame_cima, text="0", height=1, relief='flat',
               anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
points.place(x=75, y=20)

# ------------- Config Y


points2 = Label(frame_cima, text=": 0", height=1, relief='flat',
                anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
points2.place(x=105, y=20)


app_y = Label(frame_cima, text="O", height=1, relief='flat',
              anchor='center', font=('Ivy 40 bold'), bg=co1, fg=co4)
app_y.place(x=160, y=15)

app_y = Label(frame_cima, text=p2, height=1, relief='flat',
              anchor='center', font=('Ivy 7 bold'), bg=co1, fg=co0)
app_y.place(x=162, y=70)


def play():
  # -------------------- O Jogo

  # ---------------- Linhas Verticais

  app_ = Label(frame_baixo, text="", pady=5, height=23, relief='flat',
              anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
  app_.place(x=90, y=15)
  app_ = Label(frame_baixo, text="", pady=5, height=23, relief='flat',
              anchor='center', font=('Ivy 5 bold'), bg=co0, fg=co7)
  app_.place(x=155, y=15)

  # ---------------- Linhas Horizontais

  app_ = Label(frame_baixo, text="", padx=2, width=185, relief='flat',
              anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
  app_.place(x=30, y=73)

  app_ = Label(frame_baixo, text="", padx=2,  width=185, relief='flat',
              anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co7)
  app_.place(x=30, y=133)

  # ------------------- Botoes
  # ---------------- Linha 0
  b_0 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_0.place(x=30, y=17)

  b_1 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_1.place(x=95, y=17)

  b_2 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_2.place(x=160, y=17)

  # ---------------- Linha 1
  b_3 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_3.place(x=30, y=79)

  b_4 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_4.place(x=95, y=79)

  b_5 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_5.place(x=160, y=79)
  # ---------------- Linha 2
  b_6 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_6.place(x=30, y=140)

  b_7 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_7.place(x=95, y=140)

  b_8 = Button(frame_baixo, text="", width=3, height=1, overrelief=RIDGE, relief='flat', font=('Ivy 20 bold'), bg=fundo, fg=co7)
  b_8.place(x=160, y=140)

# ---------------- Jogar
b_play = Button(frame_baixo, text="Jogar", width=6, overrelief=RIDGE, relief="raised",
                height=2, font=('Ivy 8 bold'), bg=fundo, fg=co0, anchor='center')
b_play.place(x=98, y=200)

#---------------- final
janela.mainloop()
