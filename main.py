# importing tkinter for gui
import configparser
import tkinter as tk
from tkinter import PhotoImage
from tkinter import font
import paho.mqtt.client as mqtt

class GameDescription(object):
    pass

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, bg='black', bd='0')
        self.canvas.pack(fill='both', expand=True)

        # Initialize images
        self.backgroundImage = PhotoImage(file="images/background.gif")

        self.startp1_image = PhotoImage(file="images/controls/startp1.png")
        self.startp1_imageoff = PhotoImage(file="images/controls/startp1-off.png")
        self.coin_image = PhotoImage(file="images/controls/coin.png")
        self.coin_imageoff = PhotoImage(file="images/controls/coin-off.png")

        self.movement_joystick = PhotoImage(file="images/controls/joystick.png")
        self.movement_trackball = PhotoImage(file="images/controls/trackball.png")
        self.movement_spinner = PhotoImage(file="images/controls/spinner.png")


        self.y_button_image = PhotoImage(file="images/controls/y-button.png")
        self.y_button_imageoff = PhotoImage(file="images/controls/y-button-off.png")
        self.x_button_image = PhotoImage(file="images/controls/x-button.png")
        self.x_button_imageoff = PhotoImage(file="images/controls/x-button-off.png")
        self.l1_button_image = PhotoImage(file="images/controls/l1-button.png")
        self.l1_button_imageoff = PhotoImage(file="images/controls/l1-button-off.png")
        self.r1_button_image = PhotoImage(file="images/controls/r1-button.png")
        self.r1_button_imageoff = PhotoImage(file="images/controls/r1-button-off.png")

        self.a_button_image = PhotoImage(file="images/controls/a-button.png")
        self.a_button_imageoff = PhotoImage(file="images/controls/a-button-off.png")
        self.b_button_image = PhotoImage(file="images/controls/b-button.png")
        self.b_button_imageoff = PhotoImage(file="images/controls/b-button-off.png")
        self.l2_button_image = PhotoImage(file="images/controls/l2-button.png")
        self.l2_button_imageoff = PhotoImage(file="images/controls/l2-button-off.png")
        self.r2_button_image = PhotoImage(file="images/controls/r2-button.png")
        self.r2_button_imageoff = PhotoImage(file="images/controls/r2-button-off.png")

        self.controller_image_none = PhotoImage(file="images/controllers/none.png")
        self.controller_image_psx = PhotoImage(file="images/controllers/psx.png")
        self.controller_image_snes = PhotoImage(file="images/controllers/snes.png")
        self.controller_image_arcade = PhotoImage(file="images/controllers/arcade.png")

        self.gameImage = PhotoImage(file="logo.png").subsample(3,3)

        # Draw background
        self.canvas.create_image(0, 0, image=self.backgroundImage, anchor='nw')

        # Draw game image and title
        self.gameImagePlaceholder =  self.canvas.create_image(20,35, image=self.gameImage, anchor='nw')
        self.gameNamePlaceholder = self.canvas.create_text(865, 22, text="Bruudt's Arcade to Go", font=("Adumu", 42), fill="white", anchor="center", width=700)

        # Draw game buttons
        self.start_button_placeholder = self.canvas.create_image(320, 100, image=self.startp1_imageoff, anchor='nw')
        self.select_button_placeholder = self.canvas.create_image(320, 184, image=self.coin_imageoff, anchor='nw')

        self.movement_placeholder = self.canvas.create_image(420, 100, image=self.movement_joystick, anchor='nw')

        self.y_button_placeholder = self.canvas.create_image(600, 100, image=self.y_button_imageoff, anchor='nw')
        self.x_button_placeholder = self.canvas.create_image(725, 100, image=self.x_button_imageoff, anchor='nw')
        self.l1_button_placeholder = self.canvas.create_image(850, 100, image=self.l1_button_imageoff, anchor='nw')
        self.r1_button_placeholder = self.canvas.create_image(975, 100, image=self.r1_button_imageoff, anchor='nw')

        self.a_button_placeholder = self.canvas.create_image(600, 184, image=self.a_button_imageoff, anchor='nw')
        self.b_button_placeholder = self.canvas.create_image(725, 184, image=self.b_button_imageoff, anchor='nw')
        self.l2_button_placeholder = self.canvas.create_image(850, 184, image=self.l2_button_imageoff, anchor='nw')
        self.r2_button_placeholder = self.canvas.create_image(975, 184, image=self.r2_button_imageoff, anchor='nw')

        self.controller_image_placeholder = self.canvas.create_image(1150, 20, image=self.controller_image_none, anchor='nw')

        # Add texts
        self.start_text = self.canvas.create_text(382, 78, text="", font=("Arial", 16), fill="white", anchor="center")
        self.select_text = self.canvas.create_text(382, 290, text="", font=("Arial", 16), fill="white", anchor="center")

        self.movement_text = self.canvas.create_text(500, 290, text="", font=("Arial", 16), fill="white", anchor="center")
        
        self.y_button_text = self.canvas.create_text(662, 78, text="", font=("Arial", 16), fill="white", anchor="center")
        self.x_button_text = self.canvas.create_text(787, 78, text="", font=("Arial", 16), fill="white", anchor="center")
        self.l1_button_text = self.canvas.create_text(912, 78, text="", font=("Arial", 16), fill="white", anchor="center")
        self.r1_button_text = self.canvas.create_text(1037, 78, text="", font=("Arial", 16), fill="white", anchor="center")

        self.a_button_text = self.canvas.create_text(662, 290, text="", font=("Arial", 16), fill="white", anchor="center")
        self.b_button_text = self.canvas.create_text(787, 290, text="", font=("Arial", 16), fill="white", anchor="center")
        self.l2_button_text = self.canvas.create_text(912, 290, text="", font=("Arial", 16), fill="white", anchor="center")
        self.r2_button_text = self.canvas.create_text(1037, 290, text="", font=("Arial", 16), fill="white", anchor="center")

        self.attributes('-fullscreen', True) #1480x320

    def connect_mqtt(self, host, port):
        mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message
        print("Trying to connect MQTT")
        mqttc.loop_start()
        mqttc.connect_async(host, port, 60)
    
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        client.subscribe("$SYS/#")
        client.subscribe("/BruudtArcade/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        if (msg.topic == "/BruudtArcade/rungame"):
            self.resetController()
            game = self.messageToGameDescription(msg)
            print(game.game)
            self.canvas.itemconfigure(self.gameNamePlaceholder, text = game.game)

            if (game.systemid == "psx"):
                self.canvas.itemconfig(self.controller_image_placeholder, image=self.controller_image_psx)
            elif (game.systemid == "snes"):
                self.canvas.itemconfig(self.controller_image_placeholder, image=self.controller_image_snes)
            elif (game.systemid == "mame"):
                self.canvas.itemconfig(self.controller_image_placeholder, image=self.controller_image_arcade)
            else:
                self.canvas.itemconfig(self.controller_image_placeholder, image=self.controller_image_none)

        # Game image
        elif (msg.topic == "/BruudtArcade/currentimage"):
            self.gameImage = tk.PhotoImage(data=msg.payload).subsample(3,3)
            self.canvas.itemconfig(self.gameImagePlaceholder,image=self.gameImage)
            print("image replaced")

        # Game config
        elif (msg.topic == "/BruudtArcade/currentconfig"):
            self.resetButtons()
            if (msg.payload!=""):
                self.gameConfig = configparser.ConfigParser()
                self.gameConfig.read_string(msg.payload.decode(encoding="utf-8"))

                if "Movement" in self.gameConfig:
                    if "Type" in self.gameConfig["Movement"]:
                        if (self.gameConfig["Movement"]["Type"]):
                            if (self.gameConfig["Movement"]["Type"] == "joystick"):
                                self.canvas.itemconfig(self.movement_placeholder,image=self.movement_joystick)
                            if (self.gameConfig["Movement"]["Type"] == "trackball"):
                                self.canvas.itemconfig(self.movement_placeholder,image=self.movement_trackball)
                            if (self.gameConfig["Movement"]["Type"] == "spinner"):
                                self.canvas.itemconfig(self.movement_placeholder,image=self.movement_spinner)
                        if (self.gameConfig["Movement"]["Text"]):
                            self.canvas.itemconfigure(self.movement_text, text = self.gameConfig["Movement"]["Text"])

                if "Keys" in self.gameConfig:
                    if "Start" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.start_button_placeholder,image=self.startp1_image)
                        self.canvas.itemconfigure(self.start_text, text = self.gameConfig["Keys"]["Start"])
                    if "Select" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.select_button_placeholder,image=self.coin_image)
                        self.canvas.itemconfigure(self.select_text, text = self.gameConfig["Keys"]["Select"])
                
                    if "Y" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.y_button_placeholder,image=self.y_button_image)
                        self.canvas.itemconfigure(self.y_button_text, text = self.gameConfig["Keys"]["Y"])
                    if "X" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.x_button_placeholder,image=self.x_button_image)
                        self.canvas.itemconfigure(self.x_button_text, text = self.gameConfig["Keys"]["X"])
                    if "L1" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.l1_button_placeholder,image=self.l1_button_image)
                        self.canvas.itemconfigure(self.l1_button_text, text = self.gameConfig["Keys"]["L1"])
                    if "R1" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.r1_button_placeholder,image=self.r1_button_image)
                        self.canvas.itemconfigure(self.r1_button_text, text = self.gameConfig["Keys"]["R1"])

                    if "B" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.b_button_placeholder,image=self.b_button_image)
                        self.canvas.itemconfigure(self.b_button_text, text = self.gameConfig["Keys"]["B"])
                    if "A" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.a_button_placeholder,image=self.a_button_image)
                        self.canvas.itemconfigure(self.a_button_text, text = self.gameConfig["Keys"]["A"])
                    if "L2" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.l2_button_placeholder,image=self.l2_button_image)
                        self.canvas.itemconfigure(self.l2_button_text, text = self.gameConfig["Keys"]["L2"])
                    if "R2" in self.gameConfig["Keys"]:
                        self.canvas.itemconfig(self.r2_button_placeholder,image=self.r2_button_image)
                        self.canvas.itemconfigure(self.r2_button_text, text = self.gameConfig["Keys"]["R2"])
                print("config replaced")

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


    def resetController(self):
        self.canvas.itemconfig(self.controller_image_placeholder, image=self.controller_image_none)
    
    def resetButtons(self):
        self.canvas.itemconfig(self.start_button_placeholder, image=self.startp1_imageoff)
        self.canvas.itemconfigure(self.start_text, text = "")
        self.canvas.itemconfig(self.select_button_placeholder, image=self.coin_imageoff)
        self.canvas.itemconfigure(self.select_text, text = "")

        self.canvas.itemconfig(self.movement_placeholder,image=self.movement_joystick)

        self.canvas.itemconfig(self.y_button_placeholder,image=self.y_button_imageoff)
        self.canvas.itemconfigure(self.y_button_text, text = "")
        self.canvas.itemconfig(self.x_button_placeholder,image=self.x_button_imageoff)
        self.canvas.itemconfigure(self.x_button_text, text = "")
        self.canvas.itemconfig(self.l1_button_placeholder,image=self.l1_button_imageoff)
        self.canvas.itemconfigure(self.l1_button_text, text = "")
        self.canvas.itemconfig(self.r1_button_placeholder,image=self.r1_button_imageoff)
        self.canvas.itemconfigure(self.r1_button_text, text = "")

        self.canvas.itemconfig(self.b_button_placeholder,image=self.b_button_imageoff)
        self.canvas.itemconfigure(self.b_button_text, text = "")
        self.canvas.itemconfig(self.a_button_placeholder,image=self.a_button_imageoff)
        self.canvas.itemconfigure(self.a_button_text, text = "")
        self.canvas.itemconfig(self.l2_button_placeholder,image=self.l2_button_imageoff)
        self.canvas.itemconfigure(self.l2_button_text, text = "")
        self.canvas.itemconfig(self.r2_button_placeholder,image=self.r2_button_imageoff)
        self.canvas.itemconfigure(self.r2_button_text, text = "")
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config.ini')

    app = App()
    app.connect_mqtt(config['Mqtt']['Server'], int(config['Mqtt']['Port']))
    app.mainloop()