from NumPyCreator import NumPyCreator

npc = NumPyCreator()

print('####### FROM LIST #######')
print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_list([[1,2,3],[6,4]]))
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
print(npc.from_list(((1,2),(3,4))))

print('####### FROM TUPLE #######')
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_tuple(["a", "b", "c"]))

print('####### FROM ITERABLE #######')
print(npc.from_iterable(range(5)))

print('####### FROM SHAPE #######')
print(npc.from_shape((3, 5)))

print('####### RANDOM #######')
print(npc.random((3, 5)))

print('####### IDENTITY #######')
print(npc.identity(4))
