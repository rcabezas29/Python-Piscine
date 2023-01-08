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
        """"""
        
    def from_shape(self, shape, value):
        """"""
        
    def random(self, shape):
        """"""
        
    def identity(self, n):
        """"""
        
npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_list([[1,2,3],[6,4]]))
print(npc.from_list([[1,2,3],['a','b','b'],[6,4,7]]))
print(npc.from_list(((1,2),(3,4))))

print(npc.from_tuple(("a", "b", "c")))
print(npc.from_tuple(["a", "b", "c"]))
