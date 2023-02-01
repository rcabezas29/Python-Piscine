from Kmeans import *
import sys
from matplotlib import pyplot as plt

def data_representation(X):
    x = []
    y = []
    z = []
    for datum in X:
        x.append(datum[1])
        y.append(datum[2])
        z.append(datum[3])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
    

if __name__ == "__main__":
    X = pd.read_csv(sys.argv[1]).to_numpy()

    kmc = KmeansClustering()
    # data_representation(X)
    kmc.fit(X)

    