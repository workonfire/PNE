# -*- coding: utf-8 -*-

# PNE
# 1.3
# by workonfire

if __name__ == '__main__':

	from random import randrange, choice
	import tkinter as tk
	import tkMessageBox
	from time import strftime

	games = 0
	wins = 0
	loses = 0
	__version__ = '1.3'

	root = tk.Tk()
	root.title("PNE")
	root.resizable(False, False)
	root.iconbitmap('data/icon.ico')
	score_label = tk.Label(root)
	counter_label = tk.Label(root, text="Ilość gier: 0")
	wins_label = tk.Label(root, text="Ilość wygranych: 0", fg='green3')
	loses_label = tk.Label(root, text="Ilość przegranych: 0", fg='red')

	def about():
		tkMessageBox.showinfo("O grze", "Zasady gry:\n\n1. Eukaliptus zawsze wygrywa.\n2. Koala jest silniejsza od eukaliptusa, ale można jej użyć tylko raz dziennie.")
	
	def update_counter():
		global games
		global wins
		global loses
		global counter_label
		games += 1
		counter_label.config(text="Ilość gier: "+str(games))
		
	def cheat(event=None):
		global games
		global counter_label
		global wins_label
		global wins
		global loses
		global score_label
		global loses_label
		games += 123
		wins += 123
		loses = 0
		loses_label.config(text="Ilość przegranych: 0", fg='red')
		counter_label.config(text="Ilość gier: "+str(games))
		wins_label.config(text="Ilość wygranych: "+str(wins), fg='green3')
		what_happened = "Bóg:Komputer. Wygrana."
		score_label.config(text=what_happened, fg='green3')

	def papier(event=None):
		global wins_label
		global loses_label
		global loses
		character = randrange(1, 50)
		if character > 2:
			what_happened = "Papier:Eukaliptus. Przegrana."
			score_label.config(text=what_happened, fg='red')
			loses += 1
			loses_label.config(text="Ilość przegranych: "+str(loses), fg='red')
			update_counter()
		if character == 2:
			what_happened = "Papier:Nożyce. Remis."
			score_label.config(text=what_happened, fg='orange')
			update_counter()
		if character == 1:
			what_happened = "Papier:Papier. Remis."
			score_label.config(text=what_happened, fg='orange')
			update_counter()

	def nozyce(event=None):
		global loses
		global loses_label
		character = randrange(1, 50)
		if character > 2:
			what_happened = "Nożyce:Eukaliptus. Przegrana."
			score_label.config(text=what_happened, fg='red')
			loses += 1
			loses_label.config(text="Ilość przegranych: "+str(loses), fg='red')
			update_counter()
		if character == 2:
			what_happened = "Nożyce:Nożyce. Remis."
			score_label.config(text=what_happened, fg='orange')
			update_counter()
		if character == 1:
			what_happened = "Nożyce:Papier. Remis."
			score_label.config(text=what_happened, fg='orange')
			update_counter()
		
	def eukaliptus(event=None):
		global wins
		global wins_label
		character = randrange(1, 50)
		if character > 2:
			what_happened = "Eukaliptus:Eukaliptus. Remis."
			score_label.config(text=what_happened, fg='orange')
			update_counter()
		if character == 2:
			what_happened = "Eukaliptus:Nożyce. Wygrana."
			score_label.config(text=what_happened, fg='green3')
			wins += 1
			wins_label.config(text="Ilość wygranych: "+str(wins), fg='green3')
			update_counter()
		if character == 1:
			what_happened = "Eukaliptus:Papier. Wygrana."
			score_label.config(text=what_happened, fg='green3')
			wins += 1
			wins_label.config(text="Ilość wygranych: "+str(wins), fg='green3')
			update_counter()
	
	def koala(event=None):
		global wins
		global wins_label
		actual_date = strftime('%Y-%m-%d')
		with open('data/last_use_of_koala.dat', 'r+') as f:
			if actual_date == f.read():
				tkMessageBox.showerror("Błąd", "Koala została już dzisiaj użyta.")
			else:
				what_happened = "> PRZECIWNIK SPRZĄTNIĘTY <"
				score_label.config(text=what_happened, fg='green3')
				wins += 1
				wins_label.config(text="Ilość wygranych: "+str(wins), fg='green3')
				update_counter()
				f.seek(0)
				f.truncate()
				f.write(actual_date)

	welcome_label = tk.Label(root, text="Papier Nożyce Eukaliptus "+__version__, fg='blue').pack()
	author = tk.Label(root, text="by workonfire").pack()
	info_image = tk.PhotoImage(file='data/info.gif')
	about_game = tk.Button(root, text=" O grze", image=info_image, compound='left', command=about).pack(fill='x')
	label1 = tk.Label(root, text="Wybierz postać:").pack()
	label2 = tk.Button(root, text="1. Papier", command=papier).pack(fill='x')
	image1_image = tk.PhotoImage(file="data/papier.gif")
	image1_label = tk.Label(root, image=image1_image).pack()
	label3 = tk.Button(root, text="2. Nożyce", command=nozyce).pack(fill='x')
	image2_image = tk.PhotoImage(file="data/nozyce.gif")
	image2_label = tk.Label(root, image=image2_image).pack()
	label4 = tk.Button(root, text="3. Eukaliptus", command=eukaliptus).pack(fill='x')
	image3_image = tk.PhotoImage(file="data/eukaliptus.gif")
	image3_label = tk.Label(root, image=image3_image).pack()
	label5 = tk.Button(root, text="4. Koala", command=koala).pack(fill='x')
	image4_image = tk.PhotoImage(file="data/koala.gif")
	image4_label = tk.Label(root, image=image4_image).pack()
	score_label.pack()
	counter_label.pack()
	wins_label.pack()
	loses_label.pack()
	root.bind('p', papier)
	root.bind('n', nozyce)
	root.bind('e', eukaliptus)
	root.bind('k', koala)
	root.bind('/', cheat)
	root.mainloop()

