class   Evaluator:
    
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        zipped = zip(coefs, words)
        res = 0
        for z in zipped:
            res += float(z[0]) * len(z[1])
        return res
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        res = 0
        for i, word in enumerate(words):
            res += len(word) * coefs[i]
        return (res)
        
        
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
