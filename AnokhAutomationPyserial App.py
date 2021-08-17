# Button status display app
import serial
from tkinter import *
arduinoData=serial.Serial('com11' ,9600)
window=Tk()
window.title("pyserial app")
window.geometry("550x200")
Appname=Label(window,text='ANOKHAUTOMATION PYSERIAL APP',fg='white',bg='purple',font="Times 20 bold")
Appname.grid(row=0,column=0,columnspan=4,pady=10)
#Function for led1 ON
def led1_on():
    arduinoData.write(b'a')
    Labelforled1.config(text="LED1 is  ON")
# Function for led1 OFF
def led1_off():
    arduinoData.write(b'b')
    Labelforled1.config(text="LED1 is  OFF")
# Function for led2 ON
def led2_on():
    arduinoData.write(b'c')
    Labelforled2.config(text="LED2 is  ON")
    # Function for led2 OFF
def led2_off():
    arduinoData.write(b'd')
    Labelforled2.config(text="LED2 is  OFF")
#Label for LED1 Status
Labelforled1=Label(window,text= "LED1 ",bg="yellow",bd=8,relief="sunken",fg='blue',font=('Arial',14,'bold'))
Labelforled1.grid(row=2,column=0,pady=20,columnspan=2)
#Label for LED2 Status
Labelforled2=Label(window,text="LED2",bg="yellow",bd=8,relief="sunken",fg='blue',font=('Arial',14,'bold'))
Labelforled2.grid(row=2,column=2,columnspan=2)
#Button for LED1 ON
button1=Button(window,text=" LED1 ON",command = led1_on,bd=16,relief="ridge",bg="red",fg='blue',font=('Arial',14))
button1.grid(row=1,column=0)
#Button for LED1 OFF
button2=Button(window,text=" LED1 OFF",command = led1_off,bd=16,relief="ridge",bg="green",fg='blue',font=('Arial',14))
button2.grid(row=1,column=1,)
#Button for LED2 ON
button3=Button(window,text=" LED2 ON",command = led2_on,bd=16,relief="ridge",bg="red",fg='blue',font=('Arial',14))
button3.grid(row=1,column=2)
#Button for LED2 OFF
button4=Button(window,text=" LED2OFF",command = led2_off,bd=16,relief="ridge",bg="green",fg='blue',font=('Arial',14))
button4.grid(row=1,column=3)

window.mainloop()