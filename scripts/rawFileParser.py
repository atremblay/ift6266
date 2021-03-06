import os
import pandas as pd
from pandas import DataFrame, Series

class Parser(object):
    """Parser for phoneme files"""

    def __init__(self, path):
        self.path = path
        self.fileName, self.fileExtension = os.path.splitext(path)
        self.fileName = self.fileName.split('/')[-1].lower()
        
    def get_data(self):
        if self.fileExtension == '.PHN':
            return self.get_phonemes()
        elif self.fileExtension == '.TXT':
            return self.get_prompt()
        elif self.fileExtension == '.WRD':
            return self.get_words()
        else:
            raise Exception("Unsupported file format.")

    def get_phonemes(self):
        df = pd.read_csv(self.path, sep=' ', header=None)
        df.columns = (['start','end','phoneme'])
        df.index = pd.MultiIndex.from_tuples(zip([self.fileName] * df.index.shape[0], df.index))
        return df

    def get_prompt(self):
        try:
            fp = open(self.path)
        except Exception, e:
            print "\033[1,31mCould not open the file\033[0m"
            raise e

        line = fp.readlines()[0]
        line = line.strip('\n')
        line = line.split()
        start = line[0]
        end = line[1]
        prompt = " ".join(line[2:])

        df = DataFrame([(start, end, prompt)], columns=['start','end','prompts'], index=[self.fileName])
        return df

    def get_words(self):
        df = pd.read_csv(self.path, sep=' ', header=None)
        df.columns = (['start','end','phoneme'])
        df.index = pd.MultiIndex.from_tuples(zip([self.fileName] * df.index.shape[0], df.index))
        return df      