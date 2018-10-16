import SimpleITK
import matplotlib.pyplot as plt



def sitk_show(img, title=None, margin=0.0, dpi=40):
    nda = SimpleITK.GetArrayFromImage(img)
    plt.imsave('aaa.jpeg', nda, cmap=plt.cm.gray)
    fig = plt.figure();
    ax = fig.add_axes([margin, margin, 1 - 2 * margin, 1 - 2 * margin])
    plt.set_cmap("gray")
    ax.imshow(nda, interpolation=None)
    plt.show()

filenameT1 = "VSD.Brain.XX.O.MR_Flair.36607.mha"
filenameT2 = "VSD.Brain.XX.O.MR_T1.36608.mha"

idxSlice = 120
labelGrayMatter = 1

imgT1Original = SimpleITK.ReadImage(filenameT1)
imgT2Original = SimpleITK.ReadImage(filenameT2)

sitk_show(SimpleITK.Tile(imgT1Original[:, :, idxSlice],
                         imgT2Original[:, :, idxSlice],
                         (2, 1, 0)))
