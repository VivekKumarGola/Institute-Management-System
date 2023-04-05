# Import module
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = PhotoImage(file = "xyz.gif")

# Create Canvas
canvas1 = Canvas( root, width = 400,
				height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg,
					anchor = "nw")


# Execute tkinter
root.mainloop()
