from Tkinter import *
from PIL import Image, ImageTk
import SimpleITK
import matplotlib.pyplot as plt

filenameT1 = "VSD.Brain.XX.O.MR_Flair.36607.mha"
filenameT2 = "VSD.Brain.XX.O.MR_T1.36608.mha"

idxSlice = 20;
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
    plt.imsave('aaa.jpeg', nda, cmap=plt.cm.gray)
    img2 = ImageTk.PhotoImage(Image.open('aaa.jpeg'))
    label.configure(image=img2)
    label.image = img2
    #fig = plt.figure()
    #ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
    #plt.set_cmap("gray")
    #ax.imshow(nda, interpolation=None)
    #plt.show()

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

button = Button(topFrame, text="ShowIm",command = showImg)
buttonInc = Button(topFrame, text="Next slice",command = increaseSlice)
buttonDec = Button(topFrame, text="Previous slice",command = decreaseSlice)
button.pack()
buttonInc.pack()
buttonDec.pack();


root.mainloop()