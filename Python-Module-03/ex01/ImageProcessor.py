import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class   ImageProcessor:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def load(path):
        img = mpimg.imread(path)
        imgplot = plt.imshow(img)
        plt.show()
        print('Loading image of dimensions {} x {}'.format(imgplot.get_size()[0], imgplot.get_size()[1]))
        return img
    
    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()
        
    
imp = ImageProcessor() 
arr = imp.load("../resources/42AI.png")