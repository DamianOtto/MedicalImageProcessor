from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import SimpleITK
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
refPt = []
idxSlice = 1
def ImageShow():
    imgT1Original = SimpleITK.ReadImage(path)
    print(imgT1Original.GetSize())
    spacing = np.array(list(reversed(imgT1Original.GetSpacing())))
    nda = SimpleITK.GetArrayFromImage(SimpleITK.Tile(imgT1Original[:, :, idxSlice]));
    plt.imsave('aaa.jpeg', nda, cmap=plt.cm.gray);
    #photo = ImageTk.PhotoImage(Image.open('aaa.jpeg'));
    return ImageTk.PhotoImage(Image.open('aaa.jpeg'));
    #WindowInit(photo)

def ChangeImage():
    img = ImageShow();
    label.configure(image=img)
    label.image = img;
    label.pack(side="bottom", fill="both", expand="yes")

def WindowInit(photo):
    label.configure(image=photo)
    label.image = photo;
    label.pack(side="bottom", fill="both", expand="yes")
    labelSlice.pack(side=LEFT)
    buttonDec.pack(side=LEFT)
    buttonInc.pack(side=LEFT)


def increaseSlice():
        global idxSlice
        idxSlice += 1
        labelSlice.configure(text="Slice number: " + str(idxSlice))
        ChangeImage()

def decreaseSlice():
        global idxSlice
        idxSlice -= 1
        labelSlice.configure(text="Slice number: " + str(idxSlice))
        ChangeImage()


def OpenFile():
    global path
    path = askopenfilename(initialdir=os.getcwd(),
                           filetypes =(("mha file", "*.mha"),("All Files","*.mha*")),
                           title = "Choose a file."
                           )
    WindowInit(ImageShow())

def callbackX1Y1(event):
    global refPt
    topFrame.focus_set()
    refPt = [( event.x,  event.y)]
    print ("clicked at", event.x, event.y)

def callbackX2Y2(event):
    global refPt
    topFrame.focus_set()
    print("clicked at", event.x, event.y)
    refPt.append((event.x, event.y))
    image = cv2.imread('aaa.jpeg')
    clone = image.copy()
    roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
    cv2.imshow("ROI", roi)

root=Tk()
topFrame = Frame(root)
topFrame.pack()

menu = Menu(root)
root.config(menu=menu)

file = Menu(menu)
file.add_command(label = 'Open', command = OpenFile)
file.add_command(label = 'Exit', command = lambda:exit())
menu.add_cascade(label = 'File', menu = file)

label = Label(root);
label.bind("<Button-1>", callbackX1Y1)
label.bind("<ButtonRelease-1>", callbackX2Y2)
labelSlice = Label(topFrame,text = "Slice number: " + str(idxSlice))
buttonInc = Button(topFrame, text="Next slice",command=increaseSlice)
buttonDec = Button(topFrame, text="Previous slice",command=decreaseSlice)


root.mainloop()
