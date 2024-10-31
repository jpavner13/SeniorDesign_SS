import tkinter as tk
import os
 
class DronesGui:  # Blueprint of our GUI, Class.
    def __init__(self, master):
        self.master = master  # Store the master window reference
        self.master.title("SS DRONES GUI")
        self.master.geometry("600x200")
        self.master.configure(bg="black")
 
        myFrame = tk.Frame(self.master, bg="grey")  # Reference Frame as tk.Frame
        myFrame.pack(pady=20)  # Add some padding for aesthetics
 
        # self.label = tk.Label(myFrame, text="Welcome to SS Drones!", font=("Times New Roman", 16))  # Reference Label as tk.Label
        # self.label.pack(pady=10)
 
        self.blackout_button = tk.Button(myFrame, text="BLACKOUT", command=self.Blackout, bg="red", fg="white")  # Reference Button as tk.Button
        self.blackout_button.pack(pady=10)
 
        self.brownout_button = tk.Button(myFrame, text="BROWNOUT", command=self.Brownout, bg="yellow", fg="white")  # Reference Button as tk.Button
        self.brownout_button.pack(pady=10)
 
    def Blackout(self):
        # TODO: Will need specific code to disconnect Battery from Larger Assembly
        print("Blackout Button Triggered")  
    
    def Brownout(self):
        # TODO: Will need specific code to clear pending and current commands. Drone will be hovering
        print("Brownout Button Triggered")
 
 
root = tk.Tk()
# icon_path = os.path.join(os.getcwd(), "SS_logo.png")
# icon = tk.PhotoImage(file=icon_path)
# root.wm_iconphoto(True, icon)
 
Drones_gui_object = DronesGui(root)  # Instance of Drones GUI Class, Object.
root.mainloop()
