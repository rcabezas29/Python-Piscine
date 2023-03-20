import matplotlib.pyplot as plt
import numpy as np

class   ColorFilter:
    def __init__(self) -> None:
        pass
    
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        inverted = 1 - array
        inverted[..., 3:] = array[..., 3:]
        plt.imshow(inverted)
        plt.show()
        
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        b = array.copy()
        b[:, :, 1] = 0
        b[:, :, 2] = 0
        plt.imshow(b)
        plt.show()
        
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        g = array.copy()
        g[:, :, 0] = 0
        g[:, :, 2] = 0
        plt.imshow(g)
        plt.show()
        
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        r = array.copy()
        r[:, :, 0] = 0
        r[:, :, 1] = 0
        plt.imshow(r)
        plt.show()

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        c = array.copy()
        treshholds = np.linspace(0.0, 1.0, num=4, endpoint=False)
        for shade in treshholds:
            c[array >= shade] = shade
        plt.imshow(c)
        plt.show()
        
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        g = array.copy()
        for row in g:
            for col in row:
                if filter == 'm' or filter == 'mean':
                    gray = col.sum() / 3
                    col[0] = gray
                    col[1] = gray
                    col[2] = gray
                elif filter == 'w' or filter == 'weight':
                    weights = np.array(kwargs['weights'])
                    gray = col.sum() / 3
                    for i, weight in enumerate(weights):
                        col[i] = weight * gray
        plt.imshow(g)
        plt.show()