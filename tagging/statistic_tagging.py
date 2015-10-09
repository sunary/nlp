__author__ = 'sunary'

import os

class StatisticTagging():

    def __init__(self):
        self.current_dir = os.path.dirname(__file__)

    def create_model(self):

        pass

    def read_model(self):

        pass

    def read_text_train(self):

        pass

    def statistic(self):

        pass

    def statistic_doc(self):

        pass

    def save_model(self):

        pass


if __name__ == '__main__':
    statistic_tagging = StatisticTagging()
    statistic_tagging.read_model()
    statistic_tagging.read_text_train()
    statistic_tagging.statistic()
    statistic_tagging.save_model()