import matplotlib.image as mpimg
import matplotlib.pyplot as plt

class   ImageProcessor:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def load(path):
        try:
            img = mpimg.imread(path)
            imgplot = plt.imshow(img)
            plt.show()
            print('Loading image of dimensions {} x {}'.format(imgplot.get_size()[0], imgplot.get_size()[1]))
            return img
        except FileNotFoundError as e:
            print(e)
            
    
    @staticmethod
    def display(array):
        plt.imshow(array)
        plt.show()
