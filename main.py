# importing tkinter for gui
import tkinter as tk
from tkinter import PhotoImage

# creating window
window = tk.Tk()

# prepare canvas and images
backgroundImage = PhotoImage(file="background.gif")
player1ControlsImage = PhotoImage(file="buttons-player1.gif")

canvas = tk.Canvas(window, bg='white')
canvas.pack(fill='both', expand=True)

# draw background
canvas.create_image(0, 0, image=backgroundImage, anchor='nw')

# draw controls player 1
canvas.create_image(0, 0, image=player1ControlsImage, anchor='nw')

# Add texts
p1_y_button_text = canvas.create_text(315, 60, text="Jump &\nRun", font=("Arial", 16), fill="white", anchor="center")
p1_x_button_text = canvas.create_text(396, 60, text="", font=("Arial", 16), fill="white", anchor="center")
p1_l1_button_text = canvas.create_text(476, 60, text="None", font=("Arial", 16), fill="white", anchor="center")
p1_r1_button_text = canvas.create_text(557, 60, text="None", font=("Arial", 16), fill="white", anchor="center")


p1_b_button_text = canvas.create_text(315, 264, text="Jump &\n Run", font=("Arial", 16), fill="white", anchor="center")
p1_a_button_text = canvas.create_text(396, 264, text="None", font=("Arial", 16), fill="white", anchor="center")
p1_l2_button_text = canvas.create_text(476, 264, text="None", font=("Arial", 16), fill="white", anchor="center")
p1_r2_button_text = canvas.create_text(557, 264, text="None", font=("Arial", 16), fill="white", anchor="center")

p1_joystick_bottom_text = canvas.create_text(152, 240, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
p1_joystick_top_text = canvas.create_text(152, 100, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
p1_joystick_left_text = canvas.create_text(80, 170, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
p1_joystick_right_text = canvas.create_text(224, 170, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")


# setting attribute
#window.attributes('-fullscreen', True) #1480x320

window.mainloop()