from tkinter import *
import tkinter.messagebox
# First Video: Create a Window That Doesn't Disappear
#root = Tk()
#theLabel = Label(root, text = "this is too easy")
#theLabel.pack() #puts the label in the window
#root.mainloop()

#Second Video: Create a Window With Buttons And Where To Put Them

#root = Tk()

#topFrame = Frame(root) # a invisible rectange
#topFrame.pack()

#botFrame = Frame(root)
#botFrame.pack(side = BOTTOM) #shows where it will be

#button1 = Button(topFrame, text="Button 1", fg="RED") #buttons must be in a frame, have a text , and the text color is optional
#button2 = Button(topFrame, text="Button 2", fg="GREEN")
#button3 = Button(topFrame, text="Button 3", fg="YELLOW")
#button4 = Button(botFrame, text="Button 4", fg="PURPLE")

#button1.pack(side=LEFT)
#button2.pack(side=LEFT)
#button3.pack(side=LEFT)
#button4.pack(side=BOTTOM)

#root.mainloop()

#Video Three: Labels That Stretch And Fill The Window
#root = Tk()
#one = Label(root, text="Oleeeeeeee  ",bg="Black",fg="White")
#two = Label(root, text="Ha?         ",bg="Purple",fg="Yellow")
#three = Label(root, text="HAHAHAHAHA ",bg="green" , fg="orange")

#two.pack(fill=X) #Grows In X Direction If We Stretch The Window In That Direction
#three.pack(side=LEFT , fill=Y) # same for Y
#one.pack()

#root.mainloop()

#Video Four: Entrys, Checkboxes And New Packing : Grids

#root = Tk()

#label1 = Label(root , text="Username:")
#label2 = Label(root , text="Password:")

#entry1 = Entry(root)
#entry2 = Entry(root)

#label1.grid(row=0 , column=0 , sticky=E) #columns and row are 0 by default
#label2.grid(row=1 , column=0 , sticky=E) #Sticky Aligns The Label To The Thing On its right Gets E W S N For East West South North

#entry1.grid(row=0 , column=1)
#entry2.grid(row=1 , column=1)

#c = Checkbutton(root , text="Keep Me Logged In:")
#c.grid(columnspan=2)

#root.mainloop()


#Video Five: GUI Interaction

#root =Tk()

#def printName(event):
#    print("Hello Boys, Im Mehrad!")

##button1 = Button(root , text="Print My Name!" , command = printName) #Method1 : Activates when you release the Button
#button1 = Button(root , text = "Print My Name!")
#button1.bind("<Button-1>",printName) #Method2: Activates when you left click <button-1>
#button1.pack()

#root.mainloop()


#Video 7:Multiple Events

#root = Tk()

#def leftclick(event):
#    print("Left Clicked!")
#def middleclick(event):
#    print("Middle Clicked!")
#def rightclick(event):
#    print("Right Clicked!")

#frame = Frame(root , width = 300 , height=250)
#frame.bind("<Button-1>",leftclick) # Button-1 is left click
#frame.bind("<Button-2>",middleclick) # Button-2 is middleclick
#frame.bind("<Button-3>",rightclick) # button03 is rightclick
#frame.pack()
#root.mainloop()

#Video 8 : Work With Classes
###
#class siktirButtons:

#    def __init__(self, master):
#        frame = Frame(master)
#        frame.pack()
#        self.button1 = Button(frame, text="Print Message" , command = self.Print)
#        self.button1.pack(side=LEFT)
#        self.quitbutton=Button(frame, text="Exit",command = frame.quit)
#        self.quitbutton.pack(side=LEFT)

#    def Print(self):
#        print("SIKTIR")

#root= Tk()

#bot = siktirButtons(root)
#root.mainloop()
###

#Video 9: Drop Down Menus Continued 8

#def doNothing():
#    print("BASHE BABA , BASHE :| ...")
#def doSomething():
#    print("NOOMOOKHAM :(")

#root = Tk()

#menu=Menu()
#root.config(menu = menu)

#subMenu= Menu(menu)
#menu.add_cascade(label="file",menu = subMenu)
#subMenu.add_command(label="New Project...", command = doNothing)
#subMenu.add_command(label="New" , command = doSomething)
#subMenu.add_separator()
#subMenu.add_command(label="Exit", command = root.quit())

#editMenu = Menu(menu)
#menu.add_cascade(label="edit", menu=editMenu)
#editMenu.add_command(label="Redo",command = doNothing())

#****** Video 10: Creating Toolbar of V9 Continued 9

#toolbar = Frame(root, bg="red")

#inButton = Button(toolbar,text="Insert Image",command = doNothing)
#inButton.pack(side=LEFT,padx=2,pady=2)
#printButt = Button(toolbar , text="Print" , command=doNothing)
#printButt.pack(side=LEFT , padx=2 , pady=2)

#toolbar.pack(side=TOP,fill=X)

#Video 11: Creating Status Bar

#status = Label(root , text="Preparing To Do Nothing.",bd=1,relief=SUNKEN,anchor=W)
#status.pack(side=BOTTOM,fill=X)

#Video 12: Creating Messagebox
#root = Tk()

#tkinter.messagebox.showinfo('Window Title', ':/')
#answer = tkinter.messagebox.askquestion('Question1','How Are You?')
#if answer == 'Good':
#    print("Yes")
#elif answer=='not Good':
#    print("No")

#root.mainloop()

#Video 13: Shapes And Graphics
#root = Tk()
#canvas = Canvas(root,width=200,height=100)
#canvas.pack()

#blackline= canvas.create_line(0,0,200,50)
#redline = canvas.create_line(0,100,200,50,fill="red")
#greenBox=canvas.create_rectangle(25,25,130,60,fill="green")

#canvas.delete(redline)
#canvas.delete(ALL)
#root.mainloop()

#Video 14:Images and Icons

#root = Tk()

#photo = PhotoImage(file="246Dota2persian.png")

#label = Label(root,image=photo)
#label.pack()

#root.mainloop()
