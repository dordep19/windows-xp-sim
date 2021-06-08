#15-112: Principles of Programming and Computer Science
#Final Project: Windows XP OS Simulation
#Name      : Dorde Popovic
#AndrewID  : dordep

#Resources Used:
#-https://pythonspot.com/tk-file-dialogs/
#-http://effbot.org/tkinterbook/menu.htm
#-http://effbot.org/tkinterbook/grid.htm
#-http://effbot.org/tkinterbook/scale.htm
#-http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
#-http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/create_line.html
#-https://knowpapa.com/cchoser/
#-https://stackoverflow.com/questions/9886274/how-can-i-convert-canvas-content-
#to-an-image
#-https://www.youtube.com/watch?v=AaGK-fj-BAM
#-https://docs.python.org/2/library/functions.html#__import__
#-https://www.winhistory.de/more/winstart/winstart.htm.en#

#File Created: 18/11/2018
#Modification History:
#Start               End
#18/11 18:00         18/11 22:00
#20/11 11:30         20/11 13:30
#21/11 11:30         21/11 16:30
#22/11 15:00         22/11 19:30
#23/11 09:00         23/11 14:30
#23/11 18:00         23/11 23:30
#24/11 12:00         24/11 17:30

#Libraries used for GUI
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.colorchooser import askcolor

#Libraries used for file management
import os
import os.path
import pathlib

#Libraries used for image processing
import PIL.Image
import PIL.ImageTk
import PIL.ImageGrab
import PIL.ImageDraw

#Library used for clock
import datetime

#Library used for sounds
import subprocess

#Library used for snake game
import random

#Library used for copying files
import shutil

#-----------------------------------Login Screen-------------------------------

#Window allowing users to log in to existing accounts or create a new account
class loginWindow():
    
    def __init__(self, window):

        #Setting up attributes of class
        self.parent = window
        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()
        self.username = ""
        self.password = ""

        #Defining layout and widgets of login window
        self.parent.geometry("%dx%d+0+0" % (self.width, self.height))
        self.parent.configure(bg = 'light blue')
        self.parent.title("Login")
        self.frame = Frame(self.parent)
        self.usernameLabel = Label(self.frame, text = "Username")
        self.passwordLabel = Label(self.frame, text = "Password")
        self.loginButton = Button(self.frame, text = "Login",
                                  command = self.loginClicked)
        self.registerButton = Button(self.frame, text = "Register",
                                     command = self.registerClicked)
        self.usernameEntry = Entry(self.frame)
        self.passwordEntry = Entry(self.frame, show = "*")

        #Inserting and organizing all widgets inside the login window
        self.frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.usernameLabel.pack()
        self.usernameEntry.pack()
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        self.loginButton.pack(side = LEFT, padx = 20, pady = 10)
        self.registerButton.pack(side = RIGHT, padx = 20, pady = 10)
        
        #Process and store all existing usernames and passwords from data file
        self.loginData = {}
        usersData = open("LoginData.txt", "r")
        self.information = usersData.readlines()
        for i in range(1, len(self.information), 2):
            self.loginData[self.information[i].strip()] = self.information[
                i+1].strip()

    #Function logs user in if username/password combination is correct           
    def loginClicked(self):
        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()

        #Reject loggin attempt if username or password wasn't entered        
        if self.username == "" or self.password == "":
            subprocess.call(
                ["afplay",
                 str(pathlib.Path(__file__).parent.absolute())+"/sounds/error.wav"])
            showinfo("Error", "Invalid username/password combination")
        else:
    
            #Check that both username and password exist and that they match 
            if self.username in self.loginData:
                if self.password == self.loginData[self.username]:
                    
                    #Close login window and open home screen
                    self.parent.destroy()
                    secondWindow = Tk()
                    home = homeWindow(secondWindow, self.username)
                    subprocess.call(
                        ["afplay",
                         str(pathlib.Path(__file__).parent.absolute())+"/sounds/oxp.wav"])
                    secondWindow.mainloop()
                    
                #Reject login attempt if username and password don't match
                else:
                    self.usernameEntry.delete(0, 'end')
                    self.passwordEntry.delete(0, 'end')
                    subprocess.call(
                        ["afplay",
                         str(pathlib.Path(__file__).parent.absolute())+"/sounds/error.wav"])
                    showinfo("Error", "Invalid username/password combination")
            else:
                self.usernameEntry.delete(0, 'end')
                self.passwordEntry.delete(0, 'end')
                subprocess.call(
                    ["afplay",
                     str(pathlib.Path(__file__).parent.absolute())+"/sounds/error.wav"])
                showinfo("Error", "Invalid username/password combination")

    #Function creates new account and folder for user if username doesn't exist
    def registerClicked(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        self.username = self.usernameEntry.get()
        self.password = self.passwordEntry.get()
        
        #Reject new user registration if username or password wasn't entered        
        if self.username == "" or self.password == "":
            subprocess.call(
                ["afplay",
                 str(pathlib.Path(__file__).parent.absolute())+"/sounds/error.wav"])
            showinfo("Message", "Invalid username/password combination")
        else:
            
            #Reject new user registration if username already exists
            if self.username in self.loginData:
                self.usernameEntry.delete(0, 'end')
                self.passwordEntry.delete(0, 'end')
                subprocess.call(
                    ["afplay",
                     str(pathlib.Path(__file__).parent.absolute())+"/sounds/error.wav"])
                showinfo("Message", "User already exists")
            else:
                
                #Add new user's username and password to users data file
                usersData = open("LoginData.txt", "a")
                usersData.write("\n"+self.username+"\n"+self.password)
                usersData.close()
                
                #Create directory under title of user's username
                os.mkdir(self.username)
                
                #Close login window and open home screen
                self.parent.destroy()
                secondWindow = Tk()
                home = homeWindow(secondWindow, self.username)
                subprocess.call(
                    ["afplay",
                     str(pathlib.Path(__file__).parent.absolute())+"/sounds/oxp.wav"])
                secondWindow.mainloop()

#-----------------------------------Home Screen--------------------------------

#Window of home screen holding the taskbar, applications and clock 
class homeWindow():

    def __init__(self, window, username):

        #Setting up attributes of class        
        self.parent = window
        self.username = username
        self.width = self.parent.winfo_screenwidth()
        self.height = self.parent.winfo_screenheight()
        self.time = ""
        self.startOpen = False
        self.files = []
        self.filenameToken = 0

        #Loading, resizing and setting background image
        image = PIL.Image.open("images/windows.gif")
        imageResized = image.resize((self.width, self.height-180),
                                    PIL.Image.ANTIALIAS)
        backgroundImage = PIL.ImageTk.PhotoImage(imageResized)

        #Defining layout and widgets of home screen window        
        self.parent.geometry("%dx%d+0+0" % (self.width, self.height))
        self.parent.title("")
        self.taskbar = Frame(self.parent, bg = "#339FFF")
        self.clock = Label(self.taskbar, text = self.time, bg = "#339FFF")
        self.background = Label(self.parent, image = backgroundImage,
                                width = self.width-5, height = self.height-187)
        self.background.image = backgroundImage

        #Defining layout of button for start menu
        self.startButton = Button(self.taskbar, command = self.openMenu)
        self.startButton.configure(height = 55, width = 120)
        startIcon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/startPic.gif")
        startIcon = startIcon.subsample(7,7)
        self.startButton.configure(image = startIcon)
        self.startButton.image = startIcon

        #Inserting and organizing all widgets inside the home screen window
        self.background.grid(row = 0, column = 0)
        self.taskbar.grid(row = 1, column = 0, sticky = W+E)
        self.clock.pack(side = RIGHT, padx = 10, pady = 9)
        self.startButton.pack(side = LEFT)

        #Initiate timed event
        self.createClock()

        self.parent.protocol("WM_DELETE_WINDOW", self.quit)
                
    #Timed event function that displays date and time in taskbar 
    def createClock(self):
        
        self.updatedInfo = datetime.datetime.now()
        newTime = self.updatedInfo.strftime("%m/%d/%Y\n %H:%M")
        
        if self.time != newTime:
            
            self.time = newTime
            self.clock.configure(text = newTime)
            
        self.clock.after(200, self.createClock)

    def openMenu(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        
        if self.startOpen == False:
            
            self.startOpen = True
            self.startMenu = Frame(self.background, width = 250, height = 330, bg = "white")
            self.startMenu.place(x = 0, y = 400)
            self.startMenu.grid_propagate(0)

            #Defining layout of button for notepad button
            self.notepadButton = Button(self.startMenu, command = self.runNotepad)
            self.notepadButton.configure(height = 60, width = 60)
            notepadIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/notepadIcon.gif")
            notepadIcon = notepadIcon.subsample(5,5)
            self.notepadButton.configure(image = notepadIcon)
            self.notepadButton.image = notepadIcon

            #Defining layout of button for calculator button
            self.calculatorButton = Button(self.startMenu, command = self.runCalculator)
            self.calculatorButton.configure(height = 60, width = 60)
            calculatorIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/calculatorIcon.gif")
            calculatorIcon = calculatorIcon.subsample(5,5)
            self.calculatorButton.configure(image = calculatorIcon)
            self.calculatorButton.image = calculatorIcon

            #Defining layout of button for paint button
            self.paintButton = Button(self.startMenu, command = self.runPaint)
            self.paintButton.configure(height = 60, width = 60)
            paintIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/paintIcon.gif")
            paintIcon = paintIcon.subsample(5,5)
            self.paintButton.configure(image = paintIcon)
            self.paintButton.image = paintIcon

            #Defining layout of button for snake button
            self.snakeButton = Button(self.startMenu, command = self.runSnake)
            self.snakeButton.configure(height = 60, width = 60)
            snakeIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/snakeIcon.gif")
            snakeIcon = snakeIcon.subsample(7,7)
            self.snakeButton.configure(image = snakeIcon)
            self.snakeButton.image = snakeIcon

            #Defining layout of button for browse button
            self.browseButton = Button(self.startMenu, command = self.browsePrograms)
            self.browseButton.configure(height = 60, width = 60)
            browseIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/browseIcon.gif")
            browseIcon = browseIcon.subsample(5,5)
            self.browseButton.configure(image = browseIcon)
            self.browseButton.image = browseIcon

            #Defining layout of button for shut down button
            self.shutdownButton = Button(self.startMenu, command = self.quit)
            self.shutdownButton.configure(height = 40, width = 40)
            shutdownIcon = PhotoImage(
                file = os.path.dirname(os.path.abspath(__file__))+"/images/offIcon.gif")
            shutdownIcon = shutdownIcon.subsample(5,5)
            self.shutdownButton.configure(image = shutdownIcon)
            self.shutdownButton.image = shutdownIcon

            self.notepadLabel = Label(self.startMenu, text = "Notepad", font=("Helvetica", 20))
            self.calculatorLabel = Label(self.startMenu, text = "Calculator", font=("Helvetica", 20))
            self.paintLabel = Label(self.startMenu, text = "Paint", font=("Helvetica", 20))
            self.snakeLabel = Label(self.startMenu, text = "Snake", font=("Helvetica", 20))
            self.browseLabel = Label(self.startMenu, text = "Browse Files", font=("Helvetica", 20))
            
            self.notepadButton.grid(column = 0, row = 0)
            self.calculatorButton.grid(column = 0, row = 1)
            self.paintButton.grid(column = 0, row = 2)
            self.snakeButton.grid(column = 0, row = 3)
            self.browseButton.grid(column = 0, row = 4)
            self.notepadLabel.grid(column = 1, row = 0, padx = 2)
            self.calculatorLabel.grid(column = 1, row = 1, padx = 2)
            self.paintLabel.grid(column = 1, row = 2, padx = 2)
            self.snakeLabel.grid(column = 1, row = 3, padx = 2)
            self.browseLabel.grid(column = 1, row = 4, padx = 2)
            self.shutdownButton.grid(column = 2, row = 4, padx = 10)

        else:
            self.startMenu.place_forget()
            self.startOpen = False
            
    #Runs calculator program on click
    def runCalculator(self):

        self.startMenu.place_forget()
        self.startOpen = False

        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        #Open window with calculator program
        calculatorWindow = Toplevel()
        calculatorWindow.attributes('-topmost', 'true')
        calculatorWindow.lift()
        calculator = Calculator(calculatorWindow)

    #Runs notepad program on click
    def runNotepad(self):

        self.startMenu.place_forget()
        self.startOpen = False

        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        #Open window with notepad program
        notepadWindow = Toplevel()
        notepadWindow.attributes('-topmost', 'true')
        notepadWindow.lift()
        notepad = Notepad(notepadWindow, self.username)

    #Runs paint program on click
    def runPaint(self):

        self.startMenu.place_forget()
        self.startOpen = False

        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        #Open window with paint program
        paintWindow = Toplevel()
        paintWindow.attributes('-topmost', 'true')
        paintWindow.lift()
        paint = Paint(paintWindow, self.username)

    #Runs snake program on click
    def runSnake(self):

        self.startMenu.place_forget()
        self.startOpen = False
        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        #Open window with snake program
        snakeWindow = Toplevel()
        snakeWindow.attributes('-topmost', 'true')
        snakeWindow.lift()
        snake = Snake(snakeWindow)

    #Displays files for user to open
    def browsePrograms(self):

        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        self.startMenu.place_forget()
        self.startOpen = False

        #Access file from computer at specified location from user's directory
        filePath = askopenfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__))+"/"+
            self.username, title = "Select file", filetypes =
            (("text files","*.txt"),("python files","*.py"),("all files","*.*")))
        steps = filePath.split("/")
        filename = steps[-1]
        
        if filename[-3:] == "txt":

            #Open window with notepad program
            notepadWindow = Toplevel()
            notepadWindow.attributes('-topmost', 'true')
            notepadWindow.lift()
            notepad = Notepad(notepadWindow, self.username)
            notepad.openDirect(filename, filePath)

        elif filename[-4:] == "text":

            paintWindow = Toplevel()
            paintWindow.attributes("-topmost", "true")
            paintWindow.lift()
            paint = Paint(paintWindow, self.username)
            paint.openDirect(filename, filePath)

        elif filename[-2:] == "py":
            
            currentName = steps[-1]
            shutil.copy(filePath, currentName)
            __import__(currentName)

    def quit(self):
        subprocess.call([
            "afplay", str(pathlib.Path(__file__).parent.absolute())+"/sounds/shutdown.wav"])
        self.parent.destroy()
        
#---------------------------------Calculator Code------------------------------

#Window of calculator program
class Calculator():

    def __init__(self, window):

        #Setting up attributes of class        
        self.parent = window
        self.height = 515
        self.width = 412
        self.expression = ""
        self.result = 0
        
        #Defining layout and widgets of calculator window                
        self.parent.resizable(False, False)
        self.parent.title("Calculator")
        self.parent.geometry("%dx%d+0+0" % (self.width, self.height))
        self.displayFrame = Frame(self.parent, width = self.width)
        self.display = Listbox(self.displayFrame, width = self.width,
                               height = 3, bg = "black", fg = "white",
                               font = ("Helvetica", 25))
        self.buttonsFrame = Frame(self.parent, width = self.width)
        self.buttonAC = Button(self.buttonsFrame, text = "AC", width = 11,
                               height = 5, command = self.clear)
        self.buttonExponent = Button(self.buttonsFrame, text = "^", width = 11,
                                     height = 5,
                                     command = lambda: self.buttonClicked("**"))
        self.buttonMOD = Button(self.buttonsFrame, text = "MOD", width = 11,
                                height = 5,
                                command = lambda: self.buttonClicked("%"))
        self.buttonDEL = Button(self.buttonsFrame, text = "DEL", width = 11,
                                height = 5, command = self.delete)
        self.button0 = Button(self.buttonsFrame, text = "0", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("0"))
        self.button1 = Button(self.buttonsFrame, text = "1", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("1"))
        self.button2 = Button(self.buttonsFrame, text = "2", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("2"))
        self.button3 = Button(self.buttonsFrame, text = "3", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("3"))
        self.button4 = Button(self.buttonsFrame, text = "4", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("4"))
        self.button5 = Button(self.buttonsFrame, text = "5", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("5"))
        self.button6 = Button(self.buttonsFrame, text = "6", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("6"))
        self.button7 = Button(self.buttonsFrame, text = "7", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("7"))
        self.button8 = Button(self.buttonsFrame, text = "8", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("8"))
        self.button9 = Button(self.buttonsFrame, text = "9", width = 11,
                              height = 5, command = lambda:
                              self.buttonClicked("9"))
        self.buttonDivide = Button(self.buttonsFrame, text = "÷", width = 11,
                                   height = 5, command = lambda:
                                   self.buttonClicked("/"))
        self.buttonMultiply = Button(self.buttonsFrame, text = "x", width = 11,
                                     height = 5, command = lambda:
                                     self.buttonClicked("*"))
        self.buttonAdd = Button(self.buttonsFrame, text = "+", width = 11,
                                height = 5, command = lambda:
                                self.buttonClicked("+"))
        self.buttonSubtract = Button(self.buttonsFrame, text = "-", width = 11,
                                     height = 5, command = lambda:
                                     self.buttonClicked("-"))
        self.buttonEqual = Button(self.buttonsFrame, text = "=", width = 11,
                                  height = 5, command = self.calculate)
        self.buttonDecimal = Button(self.buttonsFrame, text = ".", width = 11,
                                    height = 5, command = lambda:
                                    self.buttonClicked("."))

        #Inserting and organizing all widgets inside the paint window
        self.displayFrame.pack()
        self.buttonsFrame.pack()
        self.display.pack()
        self.buttonAC.grid(row = 0, column = 0)
        self.buttonDEL.grid(row = 0, column = 1)
        self.buttonExponent.grid(row = 0, column = 2)
        self.buttonMOD.grid(row = 0, column = 3)
        self.button7.grid(row = 1, column = 0)
        self.button8.grid(row = 1, column = 1)
        self.button9.grid(row = 1, column = 2)
        self.buttonDivide.grid(row = 1, column = 3)
        self.button4.grid(row = 2, column = 0)
        self.button5.grid(row = 2, column = 1)
        self.button6.grid(row = 2, column = 2)
        self.buttonMultiply.grid(row = 2, column = 3)
        self.button1.grid(row = 3, column = 0)
        self.button2.grid(row = 3, column = 1)
        self.button3.grid(row = 3, column = 2)
        self.buttonSubtract.grid(row = 3, column = 3)
        self.button0.grid(row = 4, column = 0)
        self.buttonDecimal.grid(row = 4, column = 1)
        self.buttonAdd.grid(row = 4, column = 2)
        self.buttonEqual.grid(row = 4, column = 3)

    #Adds value of clicked button to active expression 
    def buttonClicked(self, character):
        
        self.expression = self.expression + character
        self.display.delete(0, END)
        self.display.insert(END, self.expression)

    #Evaluates the current expression if it is valid and deletes expression
    def calculate(self):

        try:
            self.result = eval(self.expression)
        except:
            self.result = ""
        self.display.delete(0, END)
        self.display.insert(END, str(self.result))
        #Result is kept to be used for further calculations
        self.expression = str(self.result)

    #Deletes whole expression
    def clear(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])        
        self.expression = ""
        self.result = ""
        self.display.delete(0, END)

    #Deletes last character entered into expression    
    def delete(self):

        self.expression = self.expression[0:-1]
        self.display.delete(0, END)
        self.display.insert(END, self.expression)

#-----------------------------------Notepad Code-------------------------------

#Window of notepad program
class Notepad():

    def __init__(self, window, username):

        #Setting up attributes of class
        self.parent = window
        self.username = username
        self.height = 500
        self.width = 500
        self.filename = ""
        
        #Defining layout and widgets of paint window
        self.parent.resizable(False, False)
        self.parent.title("Notepad")
        self.parent.geometry("%dx%d+0+0" % (self.width, self.height))
        self.textBox = Text(self.parent, width = self.width,
                            height = self.height)
        self.parent.grid_rowconfigure(0, weight=1) 
        self.parent.grid_columnconfigure(0, weight=1)
        self.scrollBar = Scrollbar(self.textBox)
        self.scrollBar.configure(command = self.textBox.yview)
        self.textBox.configure(yscrollcommand = self.scrollBar.set)

        #Setting up all configurations for the window's menu
        self.menuBar = Menu(self.parent)
        self.fileMenu = Menu(self.menuBar, tearoff = 0)
        self.editMenu = Menu(self.menuBar, tearoff=0) 
        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
        self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)
        self.fileMenu.add_command(label="New File", command = self.newFile)     
        self.fileMenu.add_command(label="Open File", command = self.openFile) 
        self.fileMenu.add_command(label="Save File", command = self.saveFile)     
        self.editMenu.add_command(label = "Copy", command = self.copy)          
        self.editMenu.add_command(label = "Paste", command = self.paste)
        self.editMenu.add_command(label = "Cut", command = self.cut)
        self.parent.configure(menu = self.menuBar)

        #Inserting and organizing all widgets inside the paint window      
        self.textBox.grid(sticky = N + E + S + W) 
        self.scrollBar.pack(side = RIGHT, fill = Y)

    #Funcion allows user to open existing file from computer
    def openFile(self):

        #Access file from computer at specified location from user's directory
        filePath = askopenfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__))+"/"+
            self.username, title = "Select file", filetypes =
            (("text files","*.txt"),("all files","*.*")))
        
        #Identify filename
        pathInfo = filePath.split("/")
        filename = pathInfo[-1]

        #If the file exists at specified location, read and load the file's
        #contents into the window and name the window by the filename
        if filePath != "":   
            self.parent.title(filename) 
            self.textBox.delete(1.0,END) 
            activeFile = open(filePath,"r") 
            self.textBox.insert(1.0, activeFile.read()) 
            activeFile.close() 

    #Funcion opens new window of notepad with empty contents     
    def newFile(self):
        
        self.parent.title("New File") 
        self.textBox.delete(1.0,END) 

    #Function saves contents from current notepad window as text file in user
    #directory
    def saveFile(self):

        #Establish location where file is to be saved 
        filePath =  asksaveasfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__))+"/"+
            self.username, title = "Select file",filetypes =
            (("text files","*.txt"),("all files","*.*")))
        
        #Identify file name 
        pathInfo = filePath.split("/")
        self.filename = pathInfo[-1]
        
        #Place contents from current notepad window into new file created in
        #user directory
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__))+"/"
                               +self.username+"/"+self.filename), "w") as temp:
            fileData = self.textBox.get(1.0,END) 
            temp.write(fileData)
        self.parent.title(self.filename)

    #Allows user to copy items in notepad window
    def copy(self):
        
        self.textBox.event_generate("<<Copy>>") 

    #Allows user to paste items in notepad window  
    def paste(self):
        
        self.textBox.event_generate("<<Paste>>")

    #Allows user to cut items in notepad window
    def cut(self):
        
        self.textBox.event_generate("<<Cut>>")

    #Allows user to open file from browse files
    def openDirect(self, filename, filePath):

        self.parent.title(filename) 
        self.textBox.delete(1.0,END) 
        activeFile = open(filePath,"r") 
        self.textBox.insert(1.0, activeFile.read())
        activeFile.close() 

#-----------------------------------Paint Code---------------------------------

#Window of paint program
class Paint():

    def __init__(self, window, username):

        #Setting up attributes of class        
        self.parent = window
        self.username = username
        self.height = 500
        self.width = 500
        self.x = None
        self.y = None
        self.color = "black"
        self.brushWidth = 1
        self.composition = []

        #Creating empty image where painting is to be saved
        self.savedImage = PIL.Image.new(
            "RGB", (500, 450), (255,255,255))
        self.updateSavedImage = PIL.ImageDraw.Draw(self.savedImage)

        #Defining layout and widgets of paint window
        self.parent.resizable(False, False)
        self.parent.title("Paint")
        self.parent.geometry("%dx%d+0+0" % (self.width, self.height))
        self.toolbar = Frame(self.parent, bg = "grey", width =
                             self.width, height = self.height/10)
        self.canvas = Canvas(self.parent, width = self.width, height
                             = 450)

        #Setting up all configurations for the window's menu
        self.menuBar = Menu(self.parent)
        self.fileMenu = Menu(self.menuBar, tearoff = 0)
        self.editMenu = Menu(self.menuBar, tearoff=0) 
        self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
        self.fileMenu.add_command(label="New File", command = self.newFile)
        self.fileMenu.add_command(label="Open File", command = self.openFile) 
        self.fileMenu.add_command(label="Save File", command = self.saveFile)     
        self.parent.configure(menu = self.menuBar)
        

        #Defining layout of button for brush
        self.brushButton = Button(self.toolbar, command = self.brush)
        self.brushButton.configure(height = 50, width = 50)
        brushIcon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/brushIcon.gif")
        brushIcon = brushIcon.subsample(6,6)
        self.brushButton.configure(image = brushIcon)
        self.brushButton.image = brushIcon

        #Defining layout of button for eraser
        self.eraserButton = Button(self.toolbar, command = self.eraser)
        self.eraserButton.configure(height = 50, width = 50)
        eraserIcon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/eraserIcon.gif")
        eraserIcon = eraserIcon.subsample(6,6)
        self.eraserButton.configure(image = eraserIcon)
        self.eraserButton.image = eraserIcon

        #Defining layout of button for color wheel        
        self.colorButton = Button(self.toolbar, command = self.changeColor)
        self.colorButton.configure(height = 50, width = 50)
        colorIcon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/colorIcon.png")
        colorIcon = colorIcon.subsample(6,6)
        self.colorButton.configure(image = colorIcon)
        self.colorButton.image = colorIcon

        #Defining layout of button for first thickness
        self.thickness1 = Button(self.toolbar,
                                 command = lambda: self.changeWidth(1))
        self.thickness1.configure(height = 50, width = 50)
        thickness1Icon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/thickness1.png")
        thickness1Icon = thickness1Icon.subsample(6,6)
        self.thickness1.configure(image = thickness1Icon)
        self.thickness1.image = thickness1Icon

        #Defining layout of button for second thickness
        self.thickness2 = Button(self.toolbar,
                                 command = lambda: self.changeWidth(4))
        self.thickness2.configure(height = 50, width = 50)
        thickness2Icon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/thickness2.png")
        thickness2Icon = thickness2Icon.subsample(6,6)
        self.thickness2.configure(image = thickness2Icon)
        self.thickness2.image = thickness2Icon

        #Defining layout of button for third thickness
        self.thickness3 = Button(self.toolbar,
                                 command = lambda: self.changeWidth(7))
        self.thickness3.configure(height = 50, width = 50)
        thicknes3Icon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/thickness3.png")
        thicknes3Icon = thicknes3Icon.subsample(6,6)
        self.thickness3.configure(image = thicknes3Icon)
        self.thickness3.image = thicknes3Icon

        #Defining layout of button for fourth thickness        
        self.thickness4 = Button(self.toolbar,
                                 command = lambda: self.changeWidth(10))
        self.thickness4.configure(height = 50, width = 50)
        thickness4Icon = PhotoImage(
            file = os.path.dirname(os.path.abspath(__file__))+"/images/thickness4.png")
        thickness4Icon = thickness4Icon.subsample(6,6)
        self.thickness4.configure(image = thickness4Icon)
        self.thickness4.image = thickness4Icon

        #Inserting and organizing all widgets inside the paint window
        self.toolbar.grid(row = 0, column = 0, sticky = N + E + S + W)
        self.canvas.grid(row = 1, column = 0)
        self.brushButton.grid(row = 0, column = 0, padx = 9, pady = 9)
        self.eraserButton.grid(row = 0, column = 1, padx = 9, pady = 9)
        self.colorButton.grid(row = 0, column = 2, padx = 9, pady = 9)
        self.thickness1.grid(row = 0, column = 3, padx = 9, pady = 9)
        self.thickness2.grid(row = 0, column = 4, padx = 9, pady = 9) 
        self.thickness3.grid(row = 0, column = 5, padx = 9, pady = 9) 
        self.thickness4.grid(row = 0, column = 6, padx = 9, pady = 9) 

        #Bind functions to events 
        self.canvas.bind('<B1-Motion>', self.pendown)
        self.canvas.bind('<ButtonRelease-1>', self.penup)

    #Open new empty canvas     
    def newFile(self):
        
        self.parent.title("New File") 
        self.canvas.delete("all")

    def openDirect(self, filename, filePath):
        
        self.parent.title(filename) 
        activeFile = open(filePath,"r")
        piece = []
        masterPiece = []
        segments = activeFile.readlines()
        counter = 0
        for segment in segments:
            if counter == 6:
                masterPiece.append(piece)
                piece = []
                counter = 0
            piece.append(segment)
            counter += 1
            activeFile.close()
        self.canvas.delete("all")
        for instruction in masterPiece:
            self.canvas.create_line(instruction[0].strip(), instruction[1].strip(), instruction[2].strip(), instruction[3].strip(), width = instruction[4].strip(), fill = instruction[5].strip(), capstyle = ROUND)
        
    #Funcion allows user to open existing file from computer
    def openFile(self):

        #Access file from computer at specified location from user's directory
        filePath = askopenfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__))+"/"+
            self.username, title = "Select file", filetypes =
            (("text files","*.text"),("all files","*.*")))
        
        #Identify filename
        pathInfo = filePath.split("/")
        filename = pathInfo[-1]

        #If the file exists at specified location, read and load the file's
        #contents into the window and name the window by the filename
        if filePath != "":   
            self.parent.title(filename) 
            activeFile = open(filePath,"r")
            piece = []
            masterPiece = []
            segments = activeFile.readlines()
            counter = 0
            for segment in segments:
                if counter == 6:
                    masterPiece.append(piece)
                    piece = []
                    counter = 0
                piece.append(segment)
                counter += 1
            activeFile.close()
            self.canvas.delete("all")
            for instruction in masterPiece:
                self.canvas.create_line(instruction[0].strip(), instruction[1].strip(), instruction[2].strip(), instruction[3].strip(), width = instruction[4].strip(), fill = instruction[5].strip(), capstyle = ROUND)
            
    #Function saves contents from current pain window as text file in user
    #directory
    def saveFile(self):

        #Establish location where file is to be saved 
        filePath =  asksaveasfilename(
            initialdir = os.path.dirname(os.path.abspath(__file__))+"/"+
            self.username, title = "Select file",filetypes =
            (("text files","*.text"),("all files","*.*")))
        
        #Identify file name 
        pathInfo = filePath.split("/")
        self.filename = pathInfo[-1]
        
        #Place instructions for current contents of paint window into new file
        #created in user directory
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__))+"/"
                               +self.username, self.filename), "w") as temp:
            for instruction in self.composition:
                for segment in instruction:
                    temp.write(str(segment)+"\n")
        self.parent.title(self.filename)

    #Draws onto canvas when mouse is clicked    
    def pendown(self, event):

        #Draws a line following path of brush (cursor) for as long as the
        #mouse is clicked
        if self.x != None:
            if self.y != None:
                self.canvas.create_line(self.x, self.y, event.x, event.y,
                               width = self.brushWidth, fill =
                                        self.color, capstyle = ROUND)
                
                self.composition.append([self.x, self.y, event.x, event.y, self.brushWidth, self.color])

                #Draw the same line on the image that is to be saved
                self.updateSavedImage.line(
                    [self.x, self.y, event.x, event.y],
                    fill = self.color, width = self.brushWidth)

        #Update current x and y coordinates of brush (cursor)
        self.x = event.x
        self.y = event.y

    #Stops drawing onto canvas when mouse is unclicked
    def penup(self, event):

        #Set x and y coordinates of brush (cursor) to be off the canvas
        #when mouse is unclicked
        self.x = None
        self.y = None

    #Changes color of brush
    def changeColor(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])

        #Retrieve hexadecimal code of color selected      
        self.color = askcolor(color = self.color)[1]

    #Changes width of brush
    def changeWidth(self, width):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        
        if self.color == "white":
            self.brushWidth = width + 4
        else:
            self.brushWidth = width

    #Selects eraser for erasing
    def eraser(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        
        self.color = "white"

    #Selects brush for drawing
    def brush(self):

        subprocess.call(
            ["afplay",
             str(pathlib.Path(__file__).parent.absolute())+"/sounds/click.wav"])
        
        self.color = "black"

#-----------------------------------Snake Code---------------------------------

class Snake():

    def __init__(self, window):

        self.parent = window
        self.height = 600
        self.width = 600

        self.x = 0
        self.y = 0
        self.xSpeed = 1
        self.ySpeed = 0
        self.scale = 20
        self.row = 0
        self.column = 0
        self.goldX = 0
        self.goldY = 0
        self.goldExists = False
        self.score = 0
        self.active = False
        self.total = 0
        self.tail = [(800,50)]
        self.result = False

        self.parent.resizable(False, False)
        self.parent.title("Snake")

        self.infoBar = Frame(self.parent, bg = "grey", width =
                             self.width, height = self.height/10)
        self.field = Canvas(self.parent, width = self.width, height
                             = self.height, bg = "black")
        self.startButton = Button(self.infoBar, text = "START",
                                  command = self.start)
        self.startButton.configure(height = 1, width = 10)
        self.scoreLabel = Label(self.infoBar, text = "Score:", bg = "grey")
        self.scoreLabel.configure(height = 1, width = 10)
        self.scoreBoard = Listbox(self.infoBar)
        self.scoreBoard.configure(height = 1, width = 10)

        self.infoBar.grid(row = 0, column = 0, sticky = E + W)
        self.field.grid(row = 1, column = 0)
        self.startButton.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.scoreLabel.grid(row = 0, column = 1, pady = 15)
        self.scoreBoard.grid(row = 0, column = 2, pady = 15)

        self.parent.bind('<Left>', self.turnWest)
        self.parent.bind('<Right>', self.turnEast)
        self.parent.bind('<Up>', self.turnNorth)
        self.parent.bind('<Down>', self.turnSouth)

    def start(self):
        
        if self.result == True:
            self.loser1.place_forget()
            self.loser2.place_forget()
            self.loser1.destroy()
            self.loser2.destroy()
            
        self.active = True
        self.run()

    def run(self):
        
        if self.active == True:
            self.suicide()
            self.show()
            self.update()
            self.collectGold()
            if self.goldExists == False:
                self.generateGold()
            else:
                self.field.create_rectangle(self.goldX, self.goldY,
                                            self.goldX+self.scale,
                                            self.goldY+self.scale, fill = "gold")
            self.field.after(100, self.run)

    def turnWest(self, event):
        
        if self.xSpeed != 1:
            self.direction(-1, 0)
        
    def turnEast(self, event):
        
        if self.xSpeed != -1:
            self.direction(1, 0)
        
    def turnNorth(self, event):
        
        if self.ySpeed != 1:
            self.direction(0, -1)
            
    def turnSouth(self, event):
        
        if self.ySpeed != -1:
            self.direction(0,1)

    def direction(self, x, y):
        
        self.xSpeed = x
        self.ySpeed = y

    def generateGold(self):
        
        self.row = random.randint(0, int(self.height/self.scale-1))
        self.column = random.randint(0, int(self.width/self.scale-1))
        self.goldX = self.column*self.scale
        self.goldY = self.row*self.scale
        self.field.create_rectangle(self.goldX, self.goldY,
                                    self.goldX+self.scale, self.goldY+self.scale,
                                    fill = "gold") 
        self.goldExists = True

    def collectGold(self):
        
        if self.goldX == self.x and self.goldY == self.y:
            self.score += 10
            self.total += 1
            self.tail.append((800,50))
            self.goldExists = False
        
    def update(self):
        
        if 0<=self.x<=self.width-self.scale and 0<=self.y<=self.height-self.scale:
            for i in range(len(self.tail)-1):
                self.tail[i] = self.tail[i+1]
            if self.total > 0:
                self.tail[self.total-1] = (self.x, self.y)
                
            self.x += self.xSpeed*self.scale
            self.y += self.ySpeed*self.scale
            self.scoreBoard.delete(0, END)
            self.scoreBoard.insert(0, self.score)
        else:
            self.result = True
            self.loser1 = Label(self.field, width = 15, height = 5, text = "GAME OVER...", background = "black", foreground = "#17FF00", font=("Helvetica", 15))
            self.loser1.place(x = 50, y = 50)
            self.loser2 = Label(self.field, width = 20, height = 5, text = "YOUR SCORE:\t"+str(self.score), background = "black", foreground = "#17FF00", font=("Helvetica", 15))
            self.loser2.place(x = 350, y = 450)
            self.restart()

    def suicide(self):
        
            for i in range(len(self.tail)-1):
                if self.tail[i][0] == self.x and self.tail[i][1] == self.y:
                    self.active = False
                    self.result = True
                    self.loser1 = Label(self.field, width = 15, height = 5, text = "GAME OVER...", background = "black", foreground = "#17FF00", font=("Helvetica", 15))
                    self.loser1.place(x = 50, y = 50)
                    self.loser2 = Label(self.field, width = 20, height = 5, text = "YOUR SCORE:\t"+str(self.score), background = "black", foreground = "#17FF00", font=("Helvetica", 15))
                    self.loser2.place(x = 350, y = 450)
                    self.restart()
            
    def restart(self):

        self.field.delete("all")
        self.score = 0
        self.active = False
        self.x = 0
        self.y = 0
        self.xSpeed = 1
        self.ySpeed = 0
        self.total = 0
        self.tail = [(800,0)]
        self.goldExists = False
        
    def show(self):

        self.field.delete("all")
        for i in range(len(self.tail)):
            self.field.create_rectangle(self.tail[i][0], self.tail[i][1],
                                        self.tail[i][0]+self.scale,
                                        self.tail[i][1]+self.scale,
                                        fill = "#17FF00") 
        self.field.create_rectangle(self.x, self.y, self.x+self.scale,
                                     self.y+self.scale, fill = "#17FF00")
        
#-----------------------------------Main Code----------------------------------
       
firstWindow = Tk()
login = loginWindow(firstWindow)
firstWindow.mainloop()
