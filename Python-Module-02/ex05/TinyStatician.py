from math import sqrt

class   TinyStatician:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def mean(x) -> float:
        s = 0
        for i in x:
            s += i
        return s / len(x)
    
    @staticmethod
    def median(x) -> float:
        x.sort()
        return float(x[int(len(x) / 2)])
    
    @staticmethod
    def quartile(x) -> tuple:
        x.sort()
        return float(x[int(len(x) / 4)]), float(x[int(len(x) - len(x) / 4)])
    
    @staticmethod
    def var(x) -> float:
        var = 0.0
        for i in x:
            var += ((i - (sum(x) / len(x)))**2 / len(x))    
        return var
    
    @staticmethod
    def std(x) -> float:
        return sqrt(TinyStatician.var(x))

tstat = TinyStatician()

a = [1, 42, 300, 10, 59]

print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartile(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.81263465868862