try:
    from Tkinter import Tk, Label, Entry, Toplevel, Canvas
except ImportError:
    from tkinter import Tk, Label, Entry, Toplevel, Canvas,Button

from PIL import Image, ImageDraw, ImageTk, ImageFont
import pickle
def StartUI():
	def close_window():
		# print(entry.get())
		name=entry.get()
		data={"Name":name}
		pickle.dump
		file=open("Name.txt",'wb')
		pickle.dump(data,file)
		root.destroy()
		# quit()
	root = Tk()
		# quit()
	entry_pady = 9
	height_text=5
	photoimage2 = ImageTk.PhotoImage(file='pops.png')
	root.title('Harp')
	canvas = Canvas(root,width=600, height=500,bg="Green",bd="0",highlightthickness=0, relief='ridge')
	canvas.create_image((0,0), image=photoimage2, anchor="nw")
	canvas.pack()
	root.geometry("+250+250")
	root.overrideredirect(True)
	root.wm_attributes("-transparentcolor", "Green")
	root.lift()
	entry = Entry(canvas, background="white")
	button=Button(canvas,background="white",text="Submit",command=close_window)
	canvas.create_window((125, 40 + height_text +entry_pady+90), window=entry, anchor="nw")
	canvas.create_window((265, 40 + height_text +entry_pady+85), window=button, anchor="nw")
	root.mainloop()