from tkinter import *
import os

class DronesGui:  # Blueprint of our GUI, Class.
    def __init__(self, master):
        self.master = master  
        self.master.title("SS DRONES GUI")
        self.master.geometry("1400x600") # horizontal x vertical size 
        self.master.configure(bg="black")  

        #ESTOP and Safety Switches Here:

        Button_Frame = Frame(self.master, bg="grey", bd=0, highlightthickness=0)  
        Button_Frame.pack(side = TOP, anchor = "ne", padx = 20, pady = 20)  

        self.estop_canvas = Canvas(Button_Frame, width=100, height=100, bg="grey", highlightthickness=0)
        self.estop_canvas.pack(side=LEFT, padx=10, pady=10)
        self.estop_canvas.create_oval(10, 10, 90, 90, fill="red", outline="")  
        self.estop_canvas.create_text(50, 50, text="ESTOP", fill="white")  

        self.estop_canvas.bind("<Button-1>", lambda e: self.estop())

        self.safety_canvas = Canvas(Button_Frame, width=100, height=100, bg="grey", highlightthickness=0)
        self.safety_canvas.pack(side=LEFT, padx=10, pady=10)
        self.safety_canvas.create_oval(10, 10, 90, 90, fill="yellow", outline="")  
        self.safety_canvas.create_text(50, 50, text="SAFETY", fill="black")  

        self.safety_canvas.bind("<Button-1>", lambda e: self.safety())

        self.enable_canvas = Canvas(Button_Frame, width=100, height=100, bg="grey", highlightthickness=0)
        self.enable_canvas.pack(side=LEFT, padx=10, pady=10)
        self.enable_canvas.create_oval(10, 10, 90, 90, fill="green", outline="")
        self.enable_canvas.create_text(50, 50, text="ENABLE", fill="white")

        self.enable_canvas.bind("<Button-1>", lambda e: self.enable())
        
        #Status window

        Status_Frame = Frame(self.master, bg="grey")
        Status_Frame.place(relx=1.0, rely=1.0, anchor="se", width=250, height=400)

        self.response_log = Text(Status_Frame, height=10, bg="black", fg="white", font=("Courier", 12), state=DISABLED)
        self.response_log.pack(padx=10, pady=10, expand=True, fill=BOTH)

        self.log_response("Drone GUI initialized.")

        #Terminal window
        self.terminal_frame = Frame(self.master, bg="black", bd=0, width=350, height=300)
        self.terminal_frame.pack(side=BOTTOM,padx=10, pady=10, anchor="s")  

        self.terminal_input = Text(self.terminal_frame, height=5, width=100, font=("Courier", 12), bg="black", fg="white")
        self.terminal_input.pack(side=BOTTOM, padx=10)

        self.terminal_input.bind("<Return>", self.execute_command)

        self.command_history = []  # Store entered commands here.
        self.history_index = -1   # Track the current position in history

        # Thrustar Command Box

        Thruster_Frame = Frame(self.master, bg="grey")
        Thruster_Frame.place(relx=0, rely=1.0, anchor="sw", width=250, height=400)

        Label(Thruster_Frame, text="Thrusters", bg="black", fg="white", font=("Helvetica", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=(10, 20))

        # Thruster labels and toggle switches
        self.thruster_states = {}  # Dictionary to store each thruster's state (on or off)
        thrusters = ["1A", "1B", "2C", "2D", "1E", "1F", "2G", "2H"]

        for idx, thruster in enumerate(thrusters):
            # Add label for each thruster
            Label(Thruster_Frame, text=thruster, bg="black", fg="white", font=("Helvetica", 10)).grid(row=idx+1, column=0, padx=10, pady=5, sticky="w")
            
            # Add radio buttons for ON and OFF
            self.thruster_states[thruster] = StringVar(value="OFF")  # Default state is OFF
            Radiobutton(Thruster_Frame, text="ON", variable=self.thruster_states[thruster], value="ON", 
                        bg="black", fg="white", selectcolor="gray", activebackground="black", activeforeground="white").grid(row=idx+1, column=1, padx=5, pady=5)
            Radiobutton(Thruster_Frame, text="OFF", variable=self.thruster_states[thruster], value="OFF", 
                        bg="black", fg="white", selectcolor="gray", activebackground="black", activeforeground="white").grid(row=idx+1, column=2, padx=5, pady=5)

        # Test Button to log current states of thrusters (for demonstration)
        #Button(Thruster_Frame, text="Log States", command=self.log_thruster_states, bg="black", fg="white").grid(row=len(thrusters)+1, column=0, columnspan=3, pady=20)


    #TODO: Plan for these functions to call scripts or a script(GUI_commands.py) with actual function definitions
    " ********* We want to make sure that this is our GUI init function and only this to make sure this script isn't 1000+ lines *********"

    def estop(self):
        # TODO: Will need specific code to disconnect Battery from Larger Assembly
        # Feedback can be removed or replaced with some other action
        self.log_response("ESTOP action triggered!")  # or any other action

    def safety(self):
        # TODO: Will need specific code to clear pending and current commands. Drone should begin hovering once pressed
        # TODO: Should also think about disabling proximity sensors around the robot then renabling
        self.log_response("Safety action triggered!")  

    def enable(self):
        #TODO: Enable sensors, should be pressed after safety command
        #TODO: Should also be pressed before drone is able to even move
        self.log_response("Drone Enabled!")
    
    def log_response(self, message):
        """Method to log messages in the response log area."""
        self.response_log.config(state=NORMAL)  
        self.response_log.insert(END, message + "\n")  
        self.response_log.see(END)  
        self.response_log.config(state=DISABLED)

    def execute_command(self, event=None):
        """Process the user command from the terminal input field."""

        #TODO: Again This will call a function (GUI_commands.py)

        # COMMANDS CASE INSENSITIVE can be lower or upper case || Let me know if y'all want case sensitive commands
        command = self.terminal_input.get("1.0", END).strip().lower()  

        # Add the command to history
        self.command_history.append(command)
        self.history_index = len(self.command_history)  # Move the history index to the end

        if command == "move":
            self.log_response("Drone moving!")
        elif command == "clear":
            self.terminal_input.delete("1.0", END)
            self.log_response("Terminal Cleared")
        else:
            self.log_response(f"Unknown command: {command}")

        self.terminal_input.delete("1.0", END)  # Modified: Clears input after execution
        return "break"  # Prevents a newline after pressing Enter because Enter is key sends command

    def recall_command(self, event=None):
        """Recall the previous commands using the arrow keys."""
        if event.keysym == 'Up':
            if self.history_index > 0:
                self.history_index -= 1
                self.terminal_input.delete("1.0", END)
                self.terminal_input.insert("1.0", self.command_history[self.history_index])
        elif event.keysym == 'Down':
            if self.history_index < len(self.command_history) - 1:
                self.history_index += 1
                self.terminal_input.delete("1.0", END)
                self.terminal_input.insert("1.0", self.command_history[self.history_index])

root = Tk()
icon_path = os.path.join(os.getcwd(), "SS_logo.png")
if os.path.exists(icon_path):
    icon = PhotoImage(file=icon_path)
    root.wm_iconphoto(True, icon)

Drones_gui_object = DronesGui(root)  # Instance of Drones GUI Class, Object.

# Bind the Up and Down keys to navigate through command history
root.bind("<Up>", Drones_gui_object.recall_command)
root.bind("<Down>", Drones_gui_object.recall_command)

root.mainloop()
