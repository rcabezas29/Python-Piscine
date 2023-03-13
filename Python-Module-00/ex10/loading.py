from tqdm import tqdm
from time import sleep

def ft_progress(lst):
    bar = ""
    for i in lst:
        perc = (100 * i) / len(lst)
        if perc % 2 == 0:
            bar += "="
        print("ETA: {:.2f}s [{:3.0f}%][{: <51}] {}/{} | elapsed time {:.2f}s".format(7.82, perc, bar + ">", i + 1, len(lst), 2.5), end="\r")
        yield i
    print()

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
