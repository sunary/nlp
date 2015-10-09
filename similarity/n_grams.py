__author__ = 'sunary'


import os
import hashlib
from other_tools.preprocessor import Preprocessor


class NGramSimilarity():

    def __init__(self):
        self.preprocessor = Preprocessor()
        self.current_dir = os.path.dirname(__file__)

    def check(self, doc1, doc2):
        checksum1 = self.three_grams(self.preprocessor.remove_mark(doc1))
        checksum2 = self.three_grams(self.preprocessor.remove_mark(doc2))

        return len(checksum1 & checksum2)* 1.0/min(len(checksum1), len(checksum2))

    def three_grams(self, doc):
        checksums = set()

        doc = doc.split(' ')
        for i in range(len(doc) - 2):
            checksums.add(hashlib.md5(' '.join(doc[i:i + 3])).digest())

        return checksums

if __name__ == '__main__':
    check_similarity = NGramSimilarity()
    doc1 = "Again I strongly question your use of MD5. You should be at least using SHA1. Some people think that as long as you're not using MD5 for 'cryptographic' purposes, you're fine. But stuff has a tendency to end up being broader in scope than you initially expect, and your casual vulnerability analysis may prove completely flawed. It's best to just get in the habit"
    doc2 = "But stuff has a tendency to end up being broader in scope than you initially expect, and your casual vulnerability analysis may prove completely flawed. It's best to just get in the habit of using the right algorithm out of the gate. It's just typing a different bunch of letters is all. It's not that hard."
    print check_similarity.check(doc1, doc2)