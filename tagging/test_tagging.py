__author__ = 'sunary'

import os
from statistic_tagging import StatisticTagging


class TestTagging(StatisticTagging):
    
    def __init__(self):
        self.current_dir = os.path.dirname(__file__)

    def read_model(self):
        StatisticTagging.read_model(self)

    def read_data_test(self):

        pass

if __name__ == '__main__':
    test_tagging = TestTagging()
    test_tagging.read_model()
    test_tagging.read_data_test()