from tkinter import *
import os

class DronesGui:  # Blueprint of our GUI, Class.
    def __init__(self, master):
        self.master = master  # Store the master window reference
        self.master.title("SS DRONES GUI")
        self.master.geometry("600x200")
        self.master.configure(bg="black")  # Set the master background to black

        Button_Frame = Frame(self.master, bg="grey", bd=0, highlightthickness=0)  
        Button_Frame.pack(padx = 0, pady = 30)  

        # Button for Blackout with red background
        self.blackout_button = Button(
            Button_Frame, 
            text="BLACKOUT",
            command=self.Blackout,
            fg="black",
            bg="grey",   # Background color for the button
            bd=0,        # Remove border
            relief="flat",  # Remove 3D effect
            highlightthickness=0  # Remove highlight border 
            )
        self.blackout_button.pack(pady=10)

        # Button for Brownout with yellow background
        self.brownout_button = Button(
            Button_Frame, 
            text="BROWNOUT", 
            command=self.Brownout, 
            fg="black", 
            #bg ="yellow",
            #highlightbackground="grey"
        )
        self.brownout_button.pack(pady=10)
        

    def Blackout(self):
        # TODO: Will need specific code to disconnect Battery from Larger Assembly
        # Feedback can be removed or replaced with some other action
        print("Blackout action triggered!")  # or any other action

    def Brownout(self):
        # TODO: Will need specific code to clear pending and current commands. Drone will be hovering
        print("Brownout action triggered!")  # or any other action


root = Tk()
icon_path = os.path.join(os.getcwd(), "SS_logo.png")
icon = PhotoImage(file=icon_path)
root.wm_iconphoto(True, icon)

Drones_gui_object = DronesGui(root)  # Instance of Drones GUI Class, Object.
root.mainloop()
