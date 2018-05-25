from Tkinter import *
import tkMessageBox as mBox
import main

def end():
        sys.exit()

def clear(root):
	for i in root.pack_slaves():
		i.destroy()

class window():

	root=Tk()
	set_of_set = []
	work_set = []
	color_bg, color_text, style_text = "white", "black", "arial 14"

	def start(self):
		clear(self.root)
		self.root.title("TextRecognition")

		rec = Button(self.root,text='Recognize',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = self.choose_recog)
		rec.pack()

		set = Button(self.root,text='Sets of letters',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = self.show_set)
		set.pack()

		help = Button(self.root,text='Help',width=20,height=1,bg = self.color_bg,fg = self.color_text,font = self.style_text, command = self.help)
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

		next = Button(self.root, text = "Next", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = lambda: self.recog_start(list_of_choose))
		next.pack()

		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.start)
		cancel.pack()

		self.root.mainloop()

	def recog_start(self, lbox):
		select = list(lbox.curselection())
		clear(self.root)
		for i in select:
			self.work_set.extend(self.set_of_set[i][1])

		label = Label(text = "Enter path of recognized file from Home")
		label.pack()

		path = StringVar()
		entry = Entry(textvariable = path)
		entry.pack()

		start = Button(self.root, text = "Start", bg = self.color_bg, fg = self.color_text, font = self.style_text, 
		command = lambda: self.do_recog(path)) 		#start recognition

		start.pack()
		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.choose_recog)
		cancel.pack()
	def do_recog(self, path):
		clear(self.root)

		label = Label(text = "Wait, please")
		label.pack()

		main.text(self.work_set, path.get())
		self.work_set = []
		self.start()

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
		show = []
		select = list(lbox.curselection())
		for i in select:
			for j in self.set_of_set[i][1]:
				show.append(j[0])

		mBox.showinfo("Choosed Sets", show)

	def add_set(self):
		clear(self.root)
		label1 = Label(text = "Input directory with new set")
		label1.pack()

		#Input directory

		#new window with creating links

		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.show_set)
		cancel.pack()

	def help(self):
		clear(self.root)
		label1 = Label(text = "There must be help for users. But there is not it:)")
		label1.pack()

		label2 = Label(text = "Please pick \"Cancel\" and don't worry")
		label2.pack()

		cancel = Button(self.root, text = "Cancel", bg = self.color_bg, fg = self.color_text, font = self.style_text,
		command = self.start)
		cancel.pack()
