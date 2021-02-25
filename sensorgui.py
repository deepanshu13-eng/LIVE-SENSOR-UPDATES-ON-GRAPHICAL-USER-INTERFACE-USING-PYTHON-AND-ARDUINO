import tkinter as  tk  # It is used to make Graphical User Interface.
import serial          # It is used for communication between Arduino and Python.
import time            # It is used to set some delay time in the program when required.
import threading       # Threading in python is used to run multiple task or functions at the same time.

arduinoData = serial.Serial('com6',9600) #Setting arduino port to COM6 and serial rate at 9600 bits per second.
arduinoData.timeout = 1


root = tk.Tk()                           # The root window is created. The root window is a main application window in our program.
root.title("SENSOR VALUE")               # Giving title to our Graphical User Interface.
root.geometry("500x400")                 # Setting up Geometry of our Graphical User Interface.
root.configure(bg = 'yellow')            # Setting up the Background Colour of our Graphical User Interface.

def arduino():                           # Defining a function called arduino.
    while True:                          # Starting up a while loop.
        data = arduinoData.readline().decode('ascii').strip() # Decoding values coming from arduino.

        if data.startswith("Temperature:"):                   # If data in Serial will start from a word Temperature then it will take the value of Temperature by performing a operation called Spliting.  
            temperature.set(data.split(":")[1])                
        elif data.startswith("Humidity:"):                    # If data in Serial will start from a word Humidity then it will take the value of Humidity by performing a operation called Spliting.   
            humidity.set(data.split(":")[1])
        elif data.startswith("Percentvalue:"):                # If data in Serial will start from a word Percentvalue then it will take the value of Percentvalue by performing a operation called Spliting.
            percentvalue.set(data.split(":")[1])              # You can change the name to whatever you want but you should also change the name in the Serial.print(" ") in arduino otherwise it will not read the data. 

tk.Label(root)                                                # Defining a label
tk.Label(root, text = "Displaying All Values",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row=0,column = 1, sticky ='w') #Setting up Font size, Colour ,row ,Font type, Row and Column of a Label. 

tk.Label(root, text="Humidity      :", font =('Ink free',20,'bold'),bg = "yellow",fg = "blue").grid(row=1, column=0, sticky='w')           
humidity = tk.StringVar()                                                                                                                  # Taking the Humidity values and storing it in a string (humidity).
tk.Label(root, textvariable=humidity , font =('Ink free',20,'bold'),bg = "yellow").grid(row=1, column=1, sticky='w')                       # Displaying the humidity value on GUI.

tk.Label(root, text="Temperature:" ,font =('Ink free',20,'bold'),bg = "yellow",fg = "green").grid(row=2, column=0, sticky='w')             # Sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
temperature = tk.StringVar()                                                                                                               # Taking the Temperature values and storing it in a string (temperature).
tk.Label(root, textvariable=temperature, font =('Ink free',20,'bold'),bg = "yellow").grid(row=2, column=1, sticky='w')                     # Displaying the temperature value on GUI.

tk.Label(root, text= "Soil Moisture:", font = ('Ink free',20,'bold'), bg = "yellow", fg = "orange").grid(row = 3, column = 0,sticky = 'w') # Displaying a label (Soil Moisture) in GUI.
percentvalue = tk.StringVar()                                                                                                              # Taking the Soil Moistue values and storing it in a string (percentvalue).
tk.Label(root, textvariable = percentvalue, font = ('Ink free',20, 'bold'),bg = "yellow").grid(row =3, column=1, sticky='w')


threading.Thread(target=arduino, daemon=True).start()                                                                                      # Doing threading in arduino function. 

root.mainloop()                                                # Finally we enter the mainloop. The event handling starts from this point. The mainloop receives events from the window system and dispatches them to the application widgets.
        