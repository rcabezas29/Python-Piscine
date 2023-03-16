class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.file = open(filename, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        self.header_line = []
        if self.header:
            self.header_line = [h.strip('" \n') for h in self.file.readline().split(',')]
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        self.file.seek(0)
        file_contents = self.file.read()
        lines = file_contents.split('\n')
        
        if self.header:
            lines = lines[1:]
        lines = lines[self.skip_top:len(lines)-self.skip_bottom]

        data = [[value.strip('" ') for value in line.split(',')] for line in lines]
        return data


    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header:
            return self.header_line
        else:
            return None
        
if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        data = file.getdata()
        header = file.getheader()

    with CsvReader('bad.csv') as file:
        if file == None:
            print("File is corrupted")