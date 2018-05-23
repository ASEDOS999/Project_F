from Tkinter import *

def end():
        sys.exit()

def clear(root):
	for i in root.pack_slaves():
		i.destroy()

class window():

	root=Tk()
	set_of_set = []
	color_bg, color_text, style_text = "white", "black", "arial 14"

	def start(self):
		clear(self.root)
		self.root.title("TextRecognition")
#		self.root.geometry("300x250")

		rec = Button(self.root,text='Recognize',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = self.choose_recog)
		rec.pack()

		set = Button(self.root,text='Sets of letters',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = self.show_set)
		set.pack()

		help = Button(self.root,text='Help',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text)
		help.pack()

		exit = Button(self.root,text='Exit',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = end)
		exit.pack()

		self.root.mainloop()

	def choose_recog(self):
		clear(self.root)
		label = Label(text = "Choose sets for recognition")
		label.pack()

		list_of_choose = Listbox(self.root, height = 5, width = 20, selectmode = EXTENDED)
		for i in self.set_of_set:
			list_of_choose.insert(END, i[0])
		list_of_choose.pack()


		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.start)
		cancel.pack()

		self.root.mainloop()

	def show_set(self):
		clear(self.root)
		label = Label(text = "Choose set that you want to see")
		label.pack()

		list_of_choose = Listbox(self.root, height = 5, width = 20, selectmode = EXTENDED)
		for i in self.set_of_set:
			list_of_choose.insert(END, i[0])
		list_of_choose.pack()

		show = Button(self.root, text = "Show choosed set", width = 20, bg = self.color_bg, fg = self.color_text, font = self.style_text, 
		command = lambda: self.show_it(list_of_choose))
		show.pack()

		add = Button(self.root, text = "Add new set", width = 20, bg = self.color_bg, fg = self.color_text, font = self.style_text, command = self.add_set)
		add.pack()

		cancel = Button(self.root, text = "Cancel", width = 20, bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.start)
		cancel.pack()

	def show_it(self, lbox):
		select = list(lbox.curselection())


	def add_set(self):
		clear(self.root)
		label1 = Label(text = "Input directory with new set")
		label1.pack()

		#Input directory

		#new window with creating links

		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.show_set)
		cancel.pack()

