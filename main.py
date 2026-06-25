# importing tkinter for gui
import tkinter as tk
from tkinter import PhotoImage
import paho.mqtt.client as mqtt

class GameDescription(object):
    pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # prepare canvas and images
        self.canvas = tk.Canvas(self, bg='black')
        self.canvas.pack(fill='both', expand=True)

        self.backgroundImage = PhotoImage(file="background.gif")
        self.player1ControlsImage = PhotoImage(file="buttons-player1.gif")
        self.gameImage = PhotoImage(file="logo.png").subsample(3,3)

        # draw background
        self.canvas.create_image(0, 0, image=self.backgroundImage, anchor='nw')

        self.gameImagePlaceholder =  self.canvas.create_image(620,10, image=self.gameImage, anchor='nw')
        self.gameNamePlaceholder = self.canvas.create_text(744, 290, text="Bruudt's Arcade To Go", font=("Arial", 24), fill="white", anchor="center", width=300)
        # draw controls player 1
        self.canvas.create_image(0, 0, image=self.player1ControlsImage, anchor='nw')

        # Add texts
        self.p1_y_button_text = self.canvas.create_text(315, 60, text="Jump &\nRun", font=("Arial", 16), fill="white", anchor="center")
        self.p1_x_button_text = self.canvas.create_text(396, 60, text="", font=("Arial", 16), fill="white", anchor="center")
        self.p1_l1_button_text = self.canvas.create_text(476, 60, text="None", font=("Arial", 16), fill="white", anchor="center")
        self.p1_r1_button_text = self.canvas.create_text(557, 60, text="None", font=("Arial", 16), fill="white", anchor="center")


        self.p1_b_button_text = self.canvas.create_text(315, 264, text="Jump &\n Run", font=("Arial", 16), fill="white", anchor="center")
        self.p1_a_button_text = self.canvas.create_text(396, 264, text="None", font=("Arial", 16), fill="white", anchor="center")
        self.p1_l2_button_text = self.canvas.create_text(476, 264, text="None", font=("Arial", 16), fill="white", anchor="center")
        self.p1_r2_button_text = self.canvas.create_text(557, 264, text="None", font=("Arial", 16), fill="white", anchor="center")

        self.p1_joystick_bottom_text = self.canvas.create_text(152, 240, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
        self.p1_joystick_top_text = self.canvas.create_text(152, 100, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
        self.p1_joystick_left_text = self.canvas.create_text(80, 170, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")
        self.p1_joystick_right_text = self.canvas.create_text(224, 170, text="Jump / \nRun", font=("Arial", 16), fill="white", anchor="center")

        self.attributes('-fullscreen', True) #1480x320

    def connect_mqtt(self):
        mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        print("Trying to connect MQTT")
        mqttc.connect("10.0.1.115", 1883, 60)
        mqttc.subscribe("/BruudtArcade/#")
        mqttc.loop_start()

    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        client.subscribe("$SYS/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if (msg.topic == "/BruudtArcade/rungame"):
            game = self.messageToGameDescription(msg)
            print(game.game)
            self.canvas.itemconfigure(self.gameNamePlaceholder, text = game.game)
        elif (msg.topic == "/BruudtArcade/currentimage"):
            self.gameImage = tk.PhotoImage(data=msg.payload).subsample(3,3)
            self.canvas.itemconfig(self.gameImagePlaceholder,image=self.gameImage)
            print("image replaced")

    def messageToGameDescription(self, msg):
        lines = msg.payload.decode(encoding="utf-8").splitlines()
        gd = GameDescription()

        for line in lines:
                splittedline = line.split('=')
                key = splittedline[0]

                if (key!="Image"):
                    value = splittedline[1]

                setattr(gd, key.lower(), value)
        
        return gd

if __name__ == "__main__":
    app = App()
    app.connect_mqtt()
    app.mainloop()