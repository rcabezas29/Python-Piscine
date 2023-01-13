import numpy as np

class   NumPyCreator:
    def __init__(self) -> None:
        pass
    
    def from_list(self, lst):
        try:
            return np.array(lst)
        except:
            return None
        
    def from_tuple(self, tpl):
        try:
            return np.array(tpl)
        except:
            return None
        
    def from_iterable(self, itr):
        try:
          return np.fromiter(itr, type(itr))
        except:
          None
        
    def from_shape(self, shape, value=0):
        try:
          return np.full(shape, value)
        except:
          return None
        
    def random(self, shape):
        try:
          return np.random.rand(shape[0], shape[1])
        except:
          return None
        
    def identity(self, n):
        try:
          return np.identity(n)
        except:
          return None



