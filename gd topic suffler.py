from tkinter import *
from tkinter import ttk
import random, time


class App:

	def __init__(self, master):
		master.title("GD Topic")
		master.geometry("200x200")
		master.resizable(False,False)

		self.menubar = Menu(master)
		master.config(menu = self.menubar)


		self.frame1 = ttk.Frame(master, height=200, width= 200)
		self.frame2 = ttk.Frame(master, height=200, width= 200)
		self.frame1.place(x=0, y=0)
		self.frame2.place(x=0, y=0)


		self.Add = Menu(self.menubar)
		self.Shuffle = Menu(self.menubar)

		self.menubar.add_cascade(menu = self.Add, label= "Add")
		self.menubar.add_cascade(menu = self.Shuffle, label= "Shuffle")

		self.Add.add_command(label= 'Add topic', command= self.add_topic)
		self.Shuffle.add_command(label=  'Shuffle', command= self.Suffle_)


		#adding things in frame1 for add function
		self.add_label = ttk.Label(self.frame1, text="Enter Topic:", font= ('Calibri Light', 10, "bold", "italic"))
		self.add_label.place(x=15, y= 50)
		self.add_entry = ttk.Entry(self.frame1, width = 28)
		self.add_entry.place(x=16, y= 67)
		self.add_entry.bind('<Return>', lambda e: self.add_item())
		self.add_button = ttk.Button(self.frame1, text = "Add", command = self.add_item)
		self.add_button.place(x=15, y= 92)


		#adding things in frame2 for suffle function
		self.suffle_label = ttk.Label(self.frame2, text= "", font= ('Calibri Light', 13, "bold"), anchor= "center")
		self.suffle_label.place(x=100, y=100, anchor="center")


		# file = open("topics.txt")
		file = open("topics.dat")
		linees = file.readlines()
		self.lines = list(map(lambda x: x.rstrip("\n"), linees))
		file.close()

	#defining a global variable for list items
	def add_topic(self):
		self.frame1.lift()


	def Suffle_(self):
		self.frame2.lift()
		if self.lines == []:
			self.suffle_label.config(text="Please add topics first")
		else:
			for i in range(500):
				self.frame2.after(20, self.shuffle_repeat)
			self.suffle_label.config(text=f"{random.choice(self.lines)}")

	def shuffle_repeat(self):
			self.suffle_label.config(text=f"{random.choice(self.lines)}")
			

	def add_item(self):
		ss = self.add_entry.get()
		ss = ss.strip()
		if ss == "":
			pass
		else:
			# file = open("topics.txt", "a")
			file = open("topics.dat", "a")
			file.write(f"\n{ss}")
			file.close()
			self.lines.append(ss)
			self.add_entry.delete(0, END)




def main():
	root = Tk()
	root.option_add('*tearOff', False)
	app = App(root)
	root.mainloop()

if __name__ == "__main__": main()
