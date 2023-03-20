import pandas as pd

class   FileLoader:
    def __init__(self) -> None:
        pass
    
    def load(self, path):
        data = pd.read_csv(path)
        print(f'Loading dataset of dimensions {data.shape[0]} x {data.shape[1]}')
        return data
        
    
    def display(self, df, n):
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(n*-1))
