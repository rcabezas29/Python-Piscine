import pandas as pd
import numpy as np
import math

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        
    def init_centroids(self, X):
        for _ in range(self.ncentroid):
            self.centroids.append(X[np.random.randint(0, X.__len__() - 1)])
            
        print(self.centroids)
        
    def distance_between_two_points(x, y):
        return math.sqrt((y[1] - x[1])**2 + (y[2] - x[2])**2 + (y[3] - x[3])**2)
        
    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        """
        self.init_centroids(X)
        for _ in range(self.max_iter):
            
    
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        """
            
        