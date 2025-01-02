from customtkinter import *
import webbrowser as wb
from PIL import Image

# Paths
icon_path = os.path.join(os.path.dirname(__file__), 'data/icon/rng_icon.ico')

# Window Setup
root = CTk()
root.geometry("300x300")
root.title("Operations RNG")
root.iconbitmap(icon_path)
root.resizable(False, False)
root.grid()

# Functions

def randnum(event):
	import random
	value = random.randint(1, 999999999999)

	updateDisplay(value)

def updateDisplay(myString):
	displayVariable.set(myString)

def git_link():
	wb.open('http://github.com/ultrain-dv')

# Tabs Setup
tabview = CTkTabview(master=root)
tabview.pack(padx=20, pady=20)
# Tabs
roll_tab = tabview.add("Roll")
abt_tab = tabview.add("About")
# Set Tab
tabview.set("Roll")


# Roll Tab
# Output
displayVariable = StringVar()
displayLabel = CTkLabel(roll_tab, textvariable=displayVariable)
displayLabel.pack(pady=50)
# Roll Button
roll_but = CTkButton(roll_tab, text="Roll")
roll_but.bind("<Button-1>",randnum)
roll_but.pack()


# About Tab
# Image
abt_image = CTkImage(Image.open(icon_path),
                                  size=(40, 40))
abt_image_label = CTkLabel(abt_tab, image=abt_image, text="")
abt_image_label.pack(pady=25)
# Title & Version
abt_title = CTkLabel(abt_tab, text="Operations RNG")
abt_v = CTkLabel(abt_tab, text="Version: 0.5")
abt_title.pack()
abt_v.pack()
# Credits
abt_label = CTkLabel(abt_tab, text="Made By: Ultrain")
abt_label.pack()
# Links
link_btn = CTkButton(abt_tab, text="Github", command=git_link)
link_btn.pack()

# Run Program
root.mainloop()