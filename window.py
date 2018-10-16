from tkinter import *
from PIL import Image, ImageTk
import SimpleITK
import matplotlib.pyplot as plt
from skimage.filters import threshold_mean
import numpy as np
import math

filenameT1 = "VSD.Brain.XX.O.MR_Flair.36607.mha"
filenameT2 = "VSD.Brain.XX.O.MR_T1.36608.mha"
value = 0
idxSlice = 20
labelGrayMatter = 1

def increaseSlice():
    global idxSlice
    idxSlice += 1
    print(idxSlice)
    labelSlice.configure(text = idxSlice)

def decreaseSlice():
    global idxSlice
    idxSlice -= 1
    print(idxSlice)
    labelSlice.configure(text=idxSlice)


def sitk_show(img, title=None, margin=0.0, dpi=40):
    nda = SimpleITK.GetArrayFromImage(img)
    thresh = threshold_mean(nda)
    binary = nda > thresh
    count = np.array(binary);
    a = np.count_nonzero(count == True)
    value = 2*math.sqrt(a/math.pi)
    labelFirstValue.configure(text = value)
    plt.imsave('aaa.jpeg', nda, cmap=plt.cm.gray)
    img2 = ImageTk.PhotoImage(Image.open('aaa.jpeg'))
    label.configure(image=img2)
    label.image = img2
    fig = plt.figure()
    ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
    #plt.set_cmap("gray")
    ax.imshow(binary, interpolation=None)
    plt.show()

def showImg():
    imgT1Original = SimpleITK.ReadImage(filenameT1)
    imgT2Original = SimpleITK.ReadImage(filenameT2)

    sitk_show(SimpleITK.Tile(imgT1Original[:, :, idxSlice],
                         imgT2Original[:, :, idxSlice],
                         (2, 1, 0)))


root=Tk()
topFrame = Frame(root)
topFrame.pack()

image = Image.open("aaa.jpeg")
img = ImageTk.PhotoImage(image)
label = Label(root, image=img)
label.pack(side="bottom", fill="both", expand="yes")

labelSlice = Label(topFrame,text = "Slice number:" + str(idxSlice))
labelSlice.pack()

labelFirstValue = Label(topFrame, text=str(value))
labelFirstValue.pack()

button = Button(topFrame, text="ShowIm",command = showImg)
buttonInc = Button(topFrame, text="Next slice",command = increaseSlice)
buttonDec = Button(topFrame, text="Previous slice",command = decreaseSlice)
button.pack()
buttonInc.pack()
buttonDec.pack();


root.mainloop()