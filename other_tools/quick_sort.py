__author__ = 'sunary'


class QuickSort():
    '''
    quicksort for list or dataframe
    '''
    def __init__(self):
        self.array = []
        self.dataframe = {}
        self.fields = []

    def get_list(self, array):
        self.array = array
        self._sort_list(0, len(self.array) - 1)
        return self.array

    def get_dataframe(self, dataframe, fields):
        self.dataframe = dataframe
        self.fields = fields
        self._sort_dataframe(0, len(self.dataframe[self.fields[0]]) - 1)
        return self.dataframe

    def _sort_list(self, left, right):
        i = left
        j = right
        pivot = self.array[left + (right - left)/2]

        while i <= j:
            while self.array[i] < pivot:
                i += 1
            while self.array[j] > pivot:
                j -= 1

            if i <= j:
                temp = self.array[i]
                self.array[i] = self.array[j]
                self.array[j] = temp
                i += 1
                j -= 1

        if left < j:
            self._sort_list(left, j)
        if i < right:
            self._sort_list(i, right)

    def _sort_dataframe(self, left, right):
        i = left
        j = right
        pivot = self.dataframe[self.fields[0]][left + (right - left)/2]

        while i <= j:
            while self.dataframe[self.fields[0]][i] < pivot:
                i += 1
            while self.dataframe[self.fields[0]][j] > pivot:
                j -= 1

            if i <= j:
                for f in self.fields:
                    temp = self.dataframe[f][i]
                    self.dataframe[f][i] = self.dataframe[f][j]
                    self.dataframe[f][j] = temp

                i += 1
                j -= 1

        if left < j:
            self._sort_dataframe(left, j)
        if i < right:
            self._sort_dataframe(i, right)


if __name__ == '__main__':
    quick_sort = QuickSort()
    print quick_sort.get_list([5, 7, 3, 2, 4, 6, 8, 1, 6])